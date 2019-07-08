from thonny import get_workbench,get_runner,THONNY_USER_DIR
from tkinter.messagebox import showerror
from thonny.ui_utils import SubprocessDialog

import serial.tools.list_ports
import ast
import re
import subprocess
import sys
import traceback
import os

def execute_command(cmd, title):
    """执行命令并监控输出结果"""
    env = os.environ.copy()
    env["PYTHONUSERBASE"] = THONNY_USER_DIR
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        env=env)
    dlg = SubprocessDialog(get_workbench(), proc, title, autoclose=False)
    dlg.wait_window()


from tkinter import Button, Frame, Label
import re, tempfile
from thonny import get_runner
from .panels import GBTranslator, GithubVisiter

if 'Buttons':

    def flash_current_script():
        """将当前脚本保存为main.py并写入"""
        current_editor = get_workbench().get_editor_notebook(
        ).get_current_editor()
        code = current_editor.get_text_widget().get("1.0", "end")
        try:
            ast.parse(code)
            file_dir = os.path.join(tempfile.gettempdir(), 'main.py')
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

    def flash_subnode():
        """写入子节点控制代码"""
        list = [
            sys.executable.replace("thonny.exe", "python.exe"),
            os.path.join(
                os.path.dirname(__file__), 'flash_module', 'flash_subnode.py')
        ]
        execute_command(list, "写入子节点控制代码...")

    def flash_enabled():
        """Return false if flashing is not possible."""
        return get_workbench().get_option("run.backend_name") != 'GenericMicroPython'

    def switch_interpreter():
        target='GenericMicroPython'
        if target==get_workbench().get_option("run.backend_name"):
            target="SameAsFrontend"
        get_workbench().set_option("run.backend_name", target)
        get_runner().restart_backend(1)


if 'Entry':

    def load_plugin():
        """Adds flash button on GUI and commands under Tools menu."""
        image_path = os.path.join(
            os.path.dirname(__file__), "res", "run.%s.gif")
        workbench = get_workbench()

        workbench.add_command(
            "flashmicrobitrepl",
            "tools",
            "写入运行环境",
            flash_repl,
            tester=flash_enabled,
            group=120,
            caption='Test',
            image=image_path % 'flash_env',
            include_in_toolbar=True)

        workbench.add_command(
            "flashmicrobit",
            "tools",
            "写入当前代码",
            flash_current_script,
            tester=flash_enabled,
            group=120,
            caption='Test',
            image=image_path % 'flash_code',
            include_in_toolbar=True)

        workbench.add_command(
            "flashmicrobitsubnode",
            "tools",
            "写入子节点控制代码",
            flash_subnode,
            tester=flash_enabled,
            group=120,
            caption='Test',
            image=image_path % 'flash_subnode',
            include_in_toolbar=True)

        workbench.add_command(
            "switchmicrobitinterpreter",
            "tools",
            "切换命令行解释器",
            switch_interpreter,
            group=120,
            caption='Test',
            image=image_path % 'switch',
            include_in_toolbar=True)

        workbench.add_view(GBTranslator, 'GB2312编码转换器', 's')
        workbench.add_view(GithubVisiter, '案例库(抓取github)', 'e')