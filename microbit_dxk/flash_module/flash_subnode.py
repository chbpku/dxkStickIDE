import os, uflash, sys

# 1. uflash empty python environment
print('写入子节点控制代码...')
try:
    uflash.flash(os.path.join(os.path.dirname(__file__),'slave.py'))
except Exception as e:
    sys.stderr.write('\n%s: %s' % (type(e).__name__, str(e)))
    sys.exit(1)