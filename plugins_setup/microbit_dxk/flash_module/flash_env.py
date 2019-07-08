import os, uflash, microfs, sys

# 1. uflash empty python environment
try:
    uflash.flash()
except Exception as e:
    sys.stderr.write('\n%s: %s' % (type(e).__name__, str(e)))
    sys.exit(1)

# 2. find & put required files
dxk_folder = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'dxk_ext'))

commands=[]
for file in os.listdir(dxk_folder):
    if file.endswith('.py'):
        commands.append("fd = open('{}', 'wb')".format(file))
        commands.append("f = fd.write")
        with open(os.path.join(dxk_folder, file), 'rb') as local:
            content = local.read()
        while content:
            line = content[:64]
            if microfs.PY2:
                commands.append('f(b' + repr(line) + ')')
            else:
                commands.append('f(' + repr(line) + ')')
            content = content[64:]
        commands.append('fd.close()')
print('Flashing modules...')
microfs.execute(commands)
print('Done.')