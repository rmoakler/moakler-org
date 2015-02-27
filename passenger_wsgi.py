import sys, os
virt_binary = "/home/moaklero/pyenv/bin/python"
if sys.executable != virt_binary: os.execl(virt_binary, virt_binary, *sys.argv)
sys.path.append(os.getcwd())
from app.views import app as application
