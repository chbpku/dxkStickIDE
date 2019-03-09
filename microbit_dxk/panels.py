from tkinter import *
from thonny import get_workbench
from thonny.code import Editor
from thonny.tktextext import TweakableText
from urllib.request import urlopen, URLError
import re, threading


class GBTranslator(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.textl = TweakableText(self, height=10, width=40)
        self.textl.pack(side='left', fill='both', padx=5, pady=5)
        self.textr = TweakableText(self, height=10, width=40)
        self.textr.pack(side='right', fill='both', padx=5, pady=5)
        frame = Frame(self)
        frame.pack(fill='both')
        Button(
            frame, text='=文本解码为GB2312=>', command=self.encode_gb).pack(
                side='top', pady=5, fill='x')
        Button(
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


if 'Course Examples':

    class _GithubNode:
        def __init__(self, master, link, name, root):
            # basic tkinter widgets
            self.root_frame = Frame(master, border=2, relief='groove')
            self.root_frame.pack(fill='x')

            self.title_text = StringVar(self.root_frame, value=name)
            self.title_label = Label(
                self.root_frame, textvariable=self.title_text, anchor='w')
            self.title_label.pack(fill='x')
            self.title_label.bind('<Button-1>', self.click)

            # github link preparer
            self.link = link
            self.name = name
            self.status = 0
            self.content = None
            if root is None:
                self.root = '/'.join(link.split('/')[:3])
            else:
                self.root = root

        def request_github(self, expand_after=False):
            self.status = 1
            self.title_text.set(self.name + ' (加载中)')

            def checker():
                if self.status == 0:
                    if isinstance(self.data, URLError):
                        err_type = '无法连接网络'
                    else:
                        err_type = type(self.data).__name__
                    self.title_text.set('%s (打开失败 %s)' % (self.name, err_type))
                elif self.status == 2:
                    self.title_text.set(self.name)
                    self.loader()
                    if expand_after:
                        self.click(0)
                else:
                    self.root_frame.after(100, checker)

            self.root_frame.after(100, checker)

            def func():
                try:
                    self.data = urlopen(self.get_link()).read().decode('utf-8')
                    self.status = 2
                except Exception as e:
                    self.data = e
                    self.status = 0

            threading.Thread(target=func).start()

        def click(self, e):
            pass

        def loader(self):
            pass

    class GithubFolder(_GithubNode):
        pattern = re.compile(r'<a.*?href="(.+?)".*?>(.+?)</a>')
        get_link = lambda self: 'https://github.com' + self.link

        def __init__(self, master, link, name, root, expand_load=False):
            super().__init__(master, link, name, root)
            self.name = '<%s>' % self.name

            # sub links display
            self.sub_frame = Frame(self.root_frame)
            self.open_folder = False
            self.request_github(expand_load)

        def click(self, e):
            if self.status == 0:
                self.request_github(1)
            elif self.status == 2:
                self.open_folder = not self.open_folder
                if self.open_folder:
                    self.sub_frame.pack(fill='x', padx=(5, 0), pady=5)
                else:
                    self.sub_frame.pack_forget()

        def loader(self):
            self.content = []
            links = self.pattern.findall(self.data)
            for raw in links:
                if self.link.startswith(raw[0]):
                    continue
                if raw[0].startswith(self.root + '/tree/master/'):
                    self.content.append(
                        GithubFolder(self.sub_frame, *raw, self.root))
                elif raw[0].startswith(self.root + '/blob/master/'):
                    self.content.append(
                        GithubFile(self.sub_frame, *raw, self.root))

    class GithubFile(_GithubNode):
        get_link=lambda self:'https://raw.githubusercontent.com'+self.link.replace('/blob/master','/master')

        def __init__(self, master, link, name, root):
            super().__init__(master, link, name, root)
            self.root_frame['relief'] = 'raised'
            self.root_frame['border'] = 1
            self.request_github()

        def click(self, e):
            if self.status == 0:
                self.request_github(1)
            elif self.status == 2:
                workbench = get_workbench()
                panel = workbench.get_editor_notebook()

                editor = Editor(panel)
                editor.get_filename = lambda *a, **kw: '案例: ' + self.name
                panel.add(editor, text='案例: ' + self.name)
                panel.select(editor)
                editor.focus_set()

                editor._code_view.set_content(self.data)
                editor._code_view.focus_set()
                editor._code_view.text.edit_modified(True)

    class GithubVisiter(Frame):
        def __init__(self, master):
            super().__init__(master)
            canvas = Canvas(self)
            frame_left = Frame(canvas)
            vertscroll = Scrollbar(
                canvas, orient='vertical', command=canvas.yview)
            vertscroll.pack(side=RIGHT, fill=Y)
            canvas.configure(yscrollcommand=vertscroll.set)

            canvas.pack(side=LEFT, fill=BOTH, expand=1)
            canvas_frame = canvas.create_window(
                (4, 4), window=frame_left, anchor="nw")

            self.tree_root = GithubFolder(
                frame_left, '/chbpku/dxkStickIDE/tree/master/Lessons', '案例',
                None, True)

            def onFrameConfigure():
                canvas.configure(scrollregion=canvas.bbox("all"))

            def chat_width(e):
                canvas_width = e.width
                canvas.itemconfig(canvas_frame, width=canvas_width)

            frame_left.bind('<Configure>', lambda e: onFrameConfigure())
            canvas.bind('<Configure>', lambda e: chat_width(e))

            # def mouse_scroll(e):
            #     tmp = canvas.bbox("all")
            #     if int(canvas['height']) > tmp[3] - tmp[1] or not (
            #             tmp[0] <= e.x <= tmp[2] and tmp[1] <= e.y <= tmp[3]):
            #         return
            #     if e.delta:
            #         canvas.yview_scroll(-1 * (e.delta // 120), 'units')
            #     else:
            #         if e.num == 5:
            #             move = 1
            #         else:
            #             move = -1
            #         canvas.yview_scroll(move, 'units')

            # canvas.bind_all('<MouseWheel>', lambda e: mouse_scroll(e))
            # canvas.bind_all('<Button-4>', lambda e: mouse_scroll(e))
            # canvas.bind_all('<Button-5>', lambda e: mouse_scroll(e))
