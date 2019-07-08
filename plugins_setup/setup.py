import os, shutil, traceback
try:
    import thonny
    thonny_dir = (os.path.dirname(thonny.__file__))
    plugin_dir = os.path.join(thonny_dir, 'plugins')
except Exception as e:
    traceback.print_exc()
    print('找不到Thonny安装目录, 请确认使用Thonny3与默认解释器运行该文件')
    os.sys.exit(1)


def install_file(src, dst):
    try:
        os.remove(dst)
    except:
        pass
    shutil.copy2(src, dst)


def install_folder(src, dst):
    shutil.rmtree(dst, 1)
    shutil.copytree(src, dst)


src_dir = '.'
targets = [
    ('thonny_translate', 'thonny_translate'),
    ('microbit_dxk', 'microbit_dxk'),
]

for s, d in targets:
    src_path = os.path.join(src_dir, s)
    dst_path = os.path.join(plugin_dir, d)
    if os.path.isfile(src_path):
        install_file(src_path, dst_path)
    else:
        install_folder(src_path, dst_path)
print('安装完成, 重启以生效')