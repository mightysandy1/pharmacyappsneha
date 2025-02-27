import os
import subprocess
import time
import webbrowser

def find_venv_path(project_directory):
    """Find the virtual environment inside the project directory."""
    possible_dirs = ["myenv", ".venv", "env", ".env"]  # Common venv names
    for venv in possible_dirs:
        venv_path = os.path.join(project_directory, venv, "Scripts", "activate")
        if os.path.exists(venv_path):
            return venv_path
    return None  # No venv found

def run_django_server():
    project_directory = os.getcwd()  # Get current working directory
    manage_py_path = os.path.join(project_directory, "manage.py")

    if not os.path.exists(manage_py_path):
        print(f"Error: manage.py not found in {project_directory}")
        return
    
    venv_path = find_venv_path(project_directory)
    if not venv_path:
        print("Error: No virtual environment found in the project directory.")
        return
    
    while True:
        try:
            print("Starting Django server...")
            webbrowser.open("http://127.0.0.1:8000/")  # Open in browser
            
            # Run Django server within virtual environment
            process = subprocess.Popen(
                f'cmd.exe /k "{venv_path} & python manage.py runserver"',
                cwd=project_directory,
                shell=True
            )
            
            process.wait()  # Wait for the process to exit
        except KeyboardInterrupt:
            print("Server manually stopped.")
            break
        except Exception as e:
            print(f"Error: {e}")
        
        print("Restarting server in 5 seconds...")
        time.sleep(5)

if __name__ == "__main__":
    run_django_server()
