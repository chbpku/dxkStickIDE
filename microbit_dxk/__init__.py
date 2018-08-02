from thonny.running import BackendProxy
from thonny.globals import get_workbench
from tkinter.messagebox import showerror
from queue import Queue
from thonny.ui_utils import SubprocessDialog
from serial import SerialException
from thonny.shared.thonny.common import ToplevelCommand
from thonny import THONNY_USER_BASE

import serial.tools.list_ports
import time
import ast
import re
import subprocess
import sys
import traceback
import jedi
import os
import textwrap


MICROBIT_PID = 516
MICROBIT_VID = 3368
BAUDRATE = 115200
TIMEOUT = 0.1
RAW_PROMPT = '\x04>'
THONNY_START = "<ForThonny>"
THONNY_END = "</ForThonny>"
NEWLINE = "\n"

BUILTINS = ['abs', 'all', 'any', 'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'bin', 'bool',
            'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'dict', 'dir', 'divmod', 'Ellipsis', 'enumerate',
            'EOFError', 'eval', 'Exception', 'exec', 'filter', 'float', 'frozenset', 'GeneratorExit', 'getattr',
            'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'ImportError', 'IndentationError', 'IndexError', 'input',
            'int', 'isinstance', 'issubclass', 'iter', 'KeyboardInterrupt', 'KeyError', 'len', 'list', 'locals',
            'LookupError', 'map', 'max', 'MemoryError', 'min', 'NameError', 'next', 'NotImplementedError', 'object',
            'oct', 'open', 'ord', 'OSError', 'OverflowError', 'pow', 'print', 'range', 'repr', 'reversed', 'round',
            'RuntimeError', 'set', 'setattr', 'sorted', 'staticmethod', 'StopIteration', 'str', 'sum', 'super', 'SyntaxError',
            'SystemExit', 'tuple', 'type', 'TypeError', 'UnicodeError', 'ValueError', 'ZeroDivisionError', 'zip']
STRING_FUNCTIONS = ['count', 'endswith', 'find', 'format', 'index', 'isalpha', 'isdigit', 'islower', 'isspace', 'isupper',
                    'join', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rpartition', 'rsplit', 'rstrip',
                    'split', 'startswith', 'strip', 'upper']
FROZENSET_FUNCTIONS = ['add', 'clear', 'copy', 'discard', 'difference', 'difference_update', 'intersection',
                        'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
                        'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
BYTES_FUNCTIONS = ['find', 'rfind', 'index', 'rindex', 'join', 'split', 'rsplit', 'startswith', 'endswith', 'strip',
                   'lstrip', 'rstrip', 'format', 'replace', 'count', 'partition', 'rpartition', 'lower', 'upper',
                   'isspace', 'isalpha', 'isdigit', 'isupper', 'islower']
MODULES = ['antigravity', 'array', 'audio', 'love', 'math', 'microbit', 'micropython', 'music',
           'neopixel', 'os', 'radio', 'random', 'speech', 'sys', 'this', 'ustruct']
DICTIONARY_FUNCTIONS = ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
SET_FUNCTIONS = ['add', 'clear', 'copy', 'discard', 'difference', 'difference_update', 'intersection', 'intersection_update',
                 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
                 'symmetric_difference_update', 'union', 'update']
LIST_FUNCTIONS = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
INT_FUNCTIONS = ['from_bytes', 'to_bytes']
BYTEARRAY_FUNCTIONS = ['append', 'extend']
TUPLE_FUNCTIONS = ['count', 'index']

class MicrobitProxy(BackendProxy):
    def __init__(self, configuration_option):
        self.cwd = get_workbench().get_option("run.working_directory")
        self._read_buffer = bytearray()
        self._message_queue = Queue()
        # if not None, then following message will be emitted after current execution
        self._toplevel_completion_message = None
        self._serial = self.get_serial()
        self._prepare_microbit()
        self._execute("from os import uname\n__print_msg__({'message_type':'ToplevelResult', 'welcome_text' : 'MicroPython ' + uname()[3]})\ndel globals()['uname']")


    @classmethod
    def get_configuration_options(cls):
        return [""]

    def get_description(self):
        """Returns a string that describes the backend"""
        return "BBC micro:bit"

    def find_microbit(self):
        """Tries to find micro:bit and returns port number. None if not found."""
        for port in list(serial.tools.list_ports.comports()):
            if port.pid == MICROBIT_PID and port.vid == MICROBIT_VID:
                return str(port.device)
        return None

    def get_serial(self):
        """Tries to open serial communication. Returns serial object or None, if unable to connect."""
        port = self.find_microbit()
        if port == None:
            self._message_queue.put_nowait({"message_type": "ProgramOutput",
                                            "stream_name": "stderr",
                                            "data": "Can't find micro:bit. Is it plugged in?\nReconnect micro:bit and wait about 5 to 10 seconds. Then press Ctrl+F2.\n"})
            return None
        try:
            ser = serial.Serial(port, baudrate=BAUDRATE, timeout=TIMEOUT)
        except SerialException as error:
            if error.errno == 13:
                message = message = textwrap.dedent("""
                Micro:bit found, but unable to connect.
                If you are a Linux user, try adding yourself to the 'dialout' group.
                sudo usermod -a -G dialout <username>
                Then relog or reboot you machine.
                """)
            elif error.errno == 16:
                message =  textwrap.dedent("""
                Micro:bit found but the device is busy.
                Press the restart button on micro:bit
                """)
            else:
                message = textwrap.dedent("""
                Micro:bit found but unable to connect.
                Error type: %s
                """ % str(error.errno))
            self._message_queue.put_nowait({"message_type": "ProgramOutput",
                                            "stream_name": "stderr",
                                            "data": message})
            return None
        return ser

    def reconnect(self):
        """Tries to reconnect micro:bit."""
        serial = self.get_serial()
        if serial != None:
            self._serial = serial
            self._message_queue.put_nowait({"message_type": "ProgramOutput",
                                            "stream_name": "stdout",
                                            "data": "Micro:bit connected.\n"})
            self._prepare_microbit()


    def _prepare_microbit(self):
        """Prepares micro:bit for further communication. Stops running program and switches micro:bit to raw REPL."""
        if self._serial is None:
            return None

        #self._message_queue = Queue() # Emptying queue
        self._serial.readall()  # Trying to clear buffer before preparaton.
        self._serial.write(b'\x03\x01')  # Ctrl-C: interrupt, Ctrl-A: switch to raw REPL
        self._serial.read_until(b'\r\n>OK')  # Flush buffer until raw mode prompt.
        self._execute("def __print_msg__(msg):\n    print('<ForThonny>'+repr(msg)+'</ForThonny>', end='')")
        self._serial.read_until(b'\x04\r\n>')

    def _reset_microbit(self):
        """Restarts micro:bit. Clears RAM and stops running program."""
        try:
            self._serial.write(b'\x04\x03')
        except Exception:
            self.reconnect()

    def _execute(self, script):
        """Executes given MicroPython script on micro:bit"""
        try:
            # https://github.com/ntoll/microfs/blob/master/microfs.py
            chunk_size = 32
            command_bytes = script.encode('utf-8')
            for i in range(0, len(command_bytes), chunk_size):
                self._serial.write(command_bytes[i:min(i + chunk_size, len(command_bytes))])
                time.sleep(0.01)
            self._serial.write(b'\x04')
            self._serial.read_until(b'OK')  # OK shows microbit has received the command
        except (AttributeError, SerialException):
            self._serial = None
            return None

    def send_command(self, cmd):
        """Executes different Thonny commands."""
        # ToplevelCommand needs a ToplevelResult later.
        self._toplevel_completion_message = isinstance(cmd, ToplevelCommand)

        # Restarts micro:bit
        if cmd.command == "Reset":
            self._reset_microbit()
            self._prepare_microbit()
            self._execute("__print_msg__({'message_type':'ToplevelResult'})")

        # Takes script from editor and executes it on micro:bit
        elif cmd.command == "Run":
            self._reset_microbit()
            self._prepare_microbit()
            self._execute(cmd.source)

        # Executes Shell commands on micro:bit
        elif cmd.command == "execute_source":
            try:
                # Try to parse as expression
                ast.parse(cmd.source, mode="eval")
                # If it didn't fail then source is an expression
                msg_template = """{'message_type':'ToplevelResult', 'value_info':{'repr':repr(v),
                                'type_name':str(type(v))[8:-2], 'id':id(v)}}"""
                self._execute("__print_msg__([%s for v in [%s]][0])" % (msg_template, cmd.source.strip()))
            except SyntaxError:
                # source is a statement (or invalid syntax)
                self._execute(cmd.source)

        # Try to get info about variables in global scope.
        elif cmd.command == "get_globals":
            self._execute("__print_msg__({'message_type':'Globals', 'module_name' : '__main__', 'globals':{x:repr(globals()[x]) for x in globals() if not x.startswith('__')}})")

        # Autocompleting word in editor
        elif cmd.command == "editor_autocomplete":
            msg = {'source': cmd.source, 'row':cmd.row, 'column':cmd.column,
                                            'message_type': 'EditorCompletions', 'command_context': 'waiting_toplevel_command',
                                            'error': None, 'command': 'editor_autocomplete'}
            chosen_completions = []
            path = os.path.join(os.path.dirname(__file__), "dummy_modules")
            script = jedi.Script(cmd.source, cmd.row, cmd.column, sys_path=[path])
            try:
                completions = script.completions()
            except Exception:
                msg['error'] = "Autocomplete error"
                self._message_queue.put_nowait(msg)
                return False
            for completion in completions:
                # Remove everything which starts with '_'
                if completion.name.startswith('_'):
                    continue

                parent_name = completion.parent().name
                name = completion.name
                root = completion.full_name.split(".")[0]
                complete = completion.complete
                if parent_name == 'str' and name in STRING_FUNCTIONS or \
                                        parent_name == 'builtins' and (name in BUILTINS or completion.is_keyword) or \
                                        root == 'int' and name in INT_FUNCTIONS or \
                                        root == 'bytearray' and name in BYTEARRAY_FUNCTIONS or \
                                        root == 'frozenset' and name in FROZENSET_FUNCTIONS or \
                                        root == 'bytes' and name in BYTES_FUNCTIONS or \
                                        root == 'tuple' and name in TUPLE_FUNCTIONS or \
                                        root == 'list' and name in LIST_FUNCTIONS or \
                                        root == 'set' and name in SET_FUNCTIONS or \
                                        root == 'dict' and name in DICTIONARY_FUNCTIONS or \
                                        root in MODULES or \
                                        root == '__main__': # Things that user has created
                    chosen_completions.append({'name': name, 'complete': complete})
            msg['completions'] = chosen_completions
            self._message_queue.put_nowait(msg)

        # Autocompleting word in Shell
        elif cmd.command == "shell_autocomplete":
            source = cmd.source
            regex = re.search('(\w+\.)*(\w+)?$', source) #https://github.com/takluyver/ubit_kernel/blob/master/ubit_kernel/kernel.py
            if regex:
                n = regex.group()
                if '.' in n:
                    obj, n = n.rsplit('.', 1)
                    self._execute("__print_msg__({'message_type': 'ShellCompletions', 'match':"+repr(n)+", 'source':"+repr(source)+", 'names':dir("+obj+")})")
                else:
                    self._execute("__print_msg__({'message_type': 'ShellCompletions', 'match':"+repr(n)+", 'source':"+repr(source)+", 'names':dir()})")
            else:
                return False

        else:
            # Ignoring other commands
            return False

    def fetch_next_message(self):
        """Reads messages/responses sent by micro:bit and acts accordingly"""
        # First read all available messages to queue
        while True:
            block_bytes = self._read_block()
            block = block_bytes.decode("utf-8")
            if len(block_bytes) == 0:
                break
            if block.endswith(THONNY_END):
                assert block.startswith(THONNY_START)
                msg_str = block[len(THONNY_START): -len(THONNY_END)]
                msg = ast.literal_eval(msg_str)

                if msg["message_type"] == "ToplevelResult":
                    # save it for later
                    self._toplevel_completion_message = msg
                # Response for Shell autocomplete. Also need to do a small modification to the original message.
                elif msg["message_type"] == "ShellCompletions":
                    names = msg['names']
                    match = msg['match']
                    msg['command_context'] = 'waiting_toplevel_command'
                    msg['command'] = 'shell_autocomplete'
                    del msg['names']
                    matches = [{'name': n, 'complete': n[len(match):]} for n in names if n.startswith(match) and not n.startswith('__')]
                    msg['completions'] = matches
                    self._message_queue.put_nowait(msg)
                else:
                    self._message_queue.put_nowait(msg)

            # stdout + stderr
            elif block.endswith(RAW_PROMPT):
                data = block[: -len(RAW_PROMPT)]
                out, err = data.split('\x04', 1)  # Split to stdout, stderr
                if len(out) > 0:
                    self._message_queue.put_nowait({"message_type": "ProgramOutput",
                                                    "stream_name": "stdout",
                                                    "data": out})

                if len(err) > 0:
                    self._message_queue.put_nowait({"message_type": "ProgramOutput",
                                                    "stream_name": "stderr",
                                                    "data": err})

                # Need to notify the completion of this execution
                # (for Runner to update the state and in cases for Shell to show new prompt)
                if self._toplevel_completion_message is True:
                    self._message_queue.put_nowait({'message_type':'ToplevelResult',
                                                    'command_context' : 'waiting_toplevel_command'})
                elif isinstance(self._toplevel_completion_message, dict):
                    # The message is prepared already
                    self._toplevel_completion_message["command_context"] = "waiting_toplevel_command"
                    self._message_queue.put_nowait(self._toplevel_completion_message)
                else:
                    # Not-toplevel command issued in toplevel context
                    self._message_queue.put_nowait({"message_type" : "InlineResult",
                                                    'command_context' : 'waiting_toplevel_command'})

            elif block.endswith(NEWLINE):
                assert "\x04" not in block
                self._message_queue.put_nowait({"message_type": "ProgramOutput",
                                                "stream_name": "stdout",
                                                "data": block})
                # If micro:bit sends welcome message (not in raw mode) then prepare it for further communication.
                if 'Type "help()" for more information.' in block:
                    self._prepare_microbit()
                    self._message_queue.put_nowait({'message_type': 'ToplevelResult', 'command_context': 'waiting_toplevel_command'})

        # There may be multiple messages which were all added to the queue and now I take the first one out.
        if not self._message_queue.empty():
            return self._message_queue.get_nowait()
        else:
            return None

    def _read_block(self):
        """Reads first block of info (eg. program output or message to Thonny) from microbit output."""
        if self._serial == None:
            return b''
        # https://github.com/ntoll/microfs/blob/master/microfs.py

        # First read all available bytes to buffer

        try:
            self._read_buffer.extend(self._serial.read_all())
        except SerialException:
            self._message_queue = Queue()
            self._message_queue.put_nowait({"message_type": "ProgramOutput",
                                            "stream_name": "stderr",
                                            "data": "Lost connection to micro:bit.\nReconnect and wait about 5 to 10 seconds. Then press Ctrl+F2.\n"})
            self._serial = None
            return b""

        if len(self._read_buffer) == 0:
            return b""

        for i in range(len(self._read_buffer) + 1):
            for marker in [RAW_PROMPT, THONNY_END, NEWLINE]:
                if isinstance(marker, str):
                    marker = marker.encode()
                if (self._read_buffer[:i].endswith(marker)
                    # don't allow \x04 in block unless it ends with raw prompt
                    and (b"\x04" not in self._read_buffer[:i] or marker == b'\x04>')
                    ):
                    block = self._read_buffer[:i]
                    del self._read_buffer[:i]
                    return block

            for marker in [THONNY_START]:
                if isinstance(marker, str):
                    marker = marker.encode()
                if self._read_buffer[i:].startswith(marker) and i > 0:
                    block = self._read_buffer[:i]
                    del self._read_buffer[:i]
                    return block

        return b""

    def send_program_input(self, data):
        """Send input data to backend"""

    def kill_current_process(self):
        """Kill the backend"""

    def interrupt(self):
        """Interrupts running script on micro:bit"""
        try:
            self._serial.write(b'\x03')
        except Exception:
            self.reconnect()


def execute_command(cmd, title):
    """执行命令并监控输出结果"""
    env = os.environ.copy()
    env["PYTHONUSERBASE"] = THONNY_USER_BASE
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        env=env)
    dlg = SubprocessDialog(get_workbench(), proc, title, autoclose=False)
    dlg.wait_window()


def flash_current_script():
    """将当前脚本保存为main.py并写入"""
    current_editor = get_workbench().get_editor_notebook().get_current_editor()
    code = current_editor.get_text_widget().get("1.0", "end")
    try:
        ast.parse(code)
        file_dir = os.path.join(os.path.dirname(__file__), 'flash_module', 'main.py')
        with open(file_dir, 'w', encoding='utf-8') as file:
            file.write(code)
        list = [
            sys.executable.replace("thonny.exe", "python.exe"),
            os.path.join(
                os.path.dirname(__file__), 'flash_module', 'flash_code.py')
        ]
        execute_command(list, "写入当前脚本...")
    except Exception:
        error_msg = traceback.format_exc(0) + '\n'
        showerror("错误", error_msg)


def flash_repl():
    """写入Python解释器与套件接口"""
    list = [
        sys.executable.replace("thonny.exe", "python.exe"),
        os.path.join(
            os.path.dirname(__file__), 'flash_module', 'flash_env.py')
    ]
    execute_command(list, "写入运行环境...")


def flash_current_script_enabled():
    """Return false if flashing is not possible."""
    #TODO
    return True


def load_early_plugin():
    """Adds micro:bit backend."""
    get_workbench().add_backend("BBC micro:bit", MicrobitProxy)


def load_plugin():
    """Adds flash button on GUI and commands under Tools menu."""
    image_path = os.path.join(
        os.path.dirname(__file__), "res", "run.flash_microbit.gif")
    get_workbench().add_command(
        "flashmicrobit",
        "tools",
        "写入当前代码",
        flash_current_script,
        flash_current_script_enabled,
        default_sequence="<Control-m>",
        group=120,
        image_filename=image_path,
        include_in_toolbar=True)

    get_workbench().add_command(
        "flashmicrobitrepl",
        "tools",
        "写入运行环境",
        flash_repl,
        group=120,
        image_filename=image_path,
        include_in_toolbar=False)

    get_workbench().add_view(GBTranslator, 'GB2312编码转换器', 's')


import tkinter as tk
from thonny.tktextext import TweakableText
import re


class GBTranslator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.textl = TweakableText(self, height=10, width=40)
        self.textl.pack(side='left', fill='both', padx=5, pady=5)
        self.textr = TweakableText(self, height=10, width=40)
        self.textr.pack(side='right', fill='both', padx=5, pady=5)
        frame = tk.Frame(self)
        frame.pack(fill='both')
        tk.Button(
            frame, text='=文本解码为GB2312=>', command=self.encode_gb).pack(
                side='top', pady=5, fill='x')
        tk.Button(
            frame, text='<=GB2312编码为文本=', command=self.decode_gb).pack(
                side='top', pady=(0, 5), fill='x')

    def encode_gb(self):
        raw = self.textl.get('0.0', 'end').split('\n')[:-1]
        output = [str(line.encode('GB2312')) if line else '' for line in raw]
        self.textr.set_content('\n'.join(output))

    valid_b_seq = re.compile(r"""^(b"[^"]+")|(b'[^']+')""")

    def decode_gb(self):
        raw = self.textr.get('0.0', 'end').split('\n')[:-1]
        output = []
        for line in raw:
            if self.valid_b_seq.match(line):
                try:
                    output.append(eval(line).decode('GB2312'))
                except:
                    output.append('')
            else:
                output.append('')
        self.textl.set_content('\n'.join(output))