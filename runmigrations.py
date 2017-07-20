import os
import subprocess
if "i5" in os.path.expandvars("%userprofile%"):
    userfolder='C:/Users/tomer-i5-PC/Desktop/myproject/'
else:
    userfolder = 'C:\Users\Tomerco\Desktop\python\seleniummm\myproject'

if __name__ == '__main__':
    subprocess.call('python {}/manage.py makemigrations'.format(userfolder))
    subprocess.call('python {}/manage.py migrate'.format(userfolder))