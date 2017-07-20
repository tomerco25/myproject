import os
import subprocess
userfolderwork='C:\Users\Tomerco\Desktop\python\seleniummm\myproject'
userfolderhome='C:/Users/tomer-i5-PC/Desktop/myproject/'

subprocess.call('python {}/manage.py makemigrations'.format(userfolderwork))
subprocess.call('python {}/manage.py migrate'.format(userfolderwork))

# os.system('start python C:/Users/tomer-i5-PC/Desktop/myproject/manage.py makemigrations')
# os.system('start python C:/Users/tomer-i5-PC/Desktop/myproject/manage.py migrate')

