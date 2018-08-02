import os, microfs, sys

code_dir = os.path.join(os.path.dirname(__file__), 'main.py')
print('写入当前代码...', flush=True, end='')
try:
    microfs.put(code_dir)
except Exception as e:
    sys.stderr.write('\n%s: %s' % (type(e).__name__, str(e)))
    sys.exit(1)
print('完成')