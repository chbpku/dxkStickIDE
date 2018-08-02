import os, uflash, microfs, sys

# 1. uflash empty python environment
print('写入Python解释器...',end='',flush=True)
try:
    uflash.flash()
except Exception as e:
    sys.stderr.write('\n%s: %s' % (type(e).__name__, str(e)))
    sys.exit(1)
print('完成')

# 2. find & put required files
dxk_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'dxk_ext'))

for file in os.listdir(dxk_folder):
    if file.endswith('.py'):
        print('加入模块: %s...' % file, end='', flush=True)
        try:
            microfs.put(os.path.join(dxk_folder, file))
        except Exception as e:
            sys.stderr.write('\n%s: %s' % (type(e).__name__, str(e)))
            sys.exit(1)
        print('完成')