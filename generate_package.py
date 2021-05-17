import subprocess
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.call(['python', 'setup.py', 'sdist'])
