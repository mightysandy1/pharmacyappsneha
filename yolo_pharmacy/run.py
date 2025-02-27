import os
import webbrowser
from threading import Timer
from django.core.management import execute_from_command_line

def open_browser():
    webbrowser.open("http://127.0.0.1:8000/")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yolo_pharmacy.settings")
    Timer(1.5, open_browser).start()  # Open the browser after 1.5 seconds
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000", "--noreload"])

