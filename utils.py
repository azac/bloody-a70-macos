import os, sys, subprocess

def get_resource_path(filename):
    base = os.environ.get('RESOURCEPATH') if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base or "", filename)

def get_python_exe():
    exe = sys.executable
    if "Contents/MacOS/" in exe:
        alt = os.path.join(os.path.dirname(exe), "python")
        if os.path.exists(alt):
            return alt
    return exe

def run_as_root(command):
    escaped_cmd = command.replace('\\', '\\\\').replace('"', '\\"')
    applescript = f'do shell script "{escaped_cmd}" with administrator privileges'
    return subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True, check=True)
