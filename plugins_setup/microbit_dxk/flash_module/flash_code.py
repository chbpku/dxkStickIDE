import os, microfs, sys, tempfile

code_dir = os.path.join(tempfile.gettempdir(), 'main.py')
print('Flashing current code...', end='')
sys.stdout.flush()
try:
    microfs.put(code_dir)
except Exception as e:
    sys.stderr.write('\n%s: %s' % (type(e).__name__, str(e)))
    sys.exit(1)
print('Done.')