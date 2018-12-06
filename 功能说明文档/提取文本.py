import os, sys, re
from os import path
func_name = re.compile(r'(?<=def )([A-Za-z0-9_]+)\((.*)\)')
code_dir = '../microbit_dxk/dxk_ext'

output = open('Document_raw.md', 'w', encoding='utf-8')
fprint = lambda *args, **kwargs: print(*args, **kwargs, file=output)
fprint('# dxkStick 开发者文档')
for filename in os.listdir(code_dir):
    if not filename.endswith('.py'):
        continue
    fprint(f'## 模块：{path.splitext(filename)[0]}')
    with open(path.join(code_dir, filename), encoding='utf-8') as file:
        for name, args in func_name.findall(file.read()):
            fprint(f"1. ### {name}({args.replace(',',', ')})")
            if args:
                fprint(f'    #### 参数:')
                args = args.split(',')
                for arg in args:
                    if '=' in arg:
                        a, b = arg.split('=')
                        fprint(f'    - {a}(默认为{b}): ')
                    else:
                        fprint(f'    - {arg}: ')
            else:
                fprint(f'    #### 参数: 无')
            fprint(f'    #### 返回值: ')
    fprint('---')
output.close()