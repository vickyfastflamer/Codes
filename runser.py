'''import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application()
call_command('runserver',  '127.0.0.1:8000')'''

import subprocess

def start_django_server():
    # Replace 'path_to_manage_py' with the actual path to your 'manage.py' file
    manage_py_path = "C:\\Users\\vicky\\Desktop\\Main project\\Code\\webv\\log\\manage.py"

    # Change 'your_project_name' to your Django project name
    # Optionally, you can specify the host and port
    subprocess.Popen(['python', manage_py_path, 'runserver', '127.0.0.1:8000'])

if __name__ == "__main__":
    start_django_server()


