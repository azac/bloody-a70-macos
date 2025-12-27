import os, sys
import rumps
import utils

MENU_CONFIG = [
    ("Bloody A70 Mouse", None),
    None,
    ("Brightness", None),
    ("Off", "brightness_off"),
    ("Low", "brightness_low"),
    ("Medium", "brightness_medium"),
    ("High", "brightness_high"),
    None,
    ("Color Mode", None),
    ("Lights Off", "colors_lightsoff"),
    ("Neon Glare System", "colors_neonglare"),
    ("Constant Light", "colors_constant"),
    ("Breathing", "colors_breathing"),
    None,
]

DRIVER_PATH = utils.get_resource_path("driver.py")
PYTHON_EXE = utils.get_python_exe()
PYTHON_PATH_ENV = ":".join(sys.path)

def run_usb_sequence(sequence_name):
    cmd = f'export PYTHONPATH="{PYTHON_PATH_ENV}"; "{PYTHON_EXE}" "{DRIVER_PATH}" "{sequence_name}"'
    try:
        utils.run_as_root(cmd)
    except Exception:
        rumps.alert("Connection Error", "Please ensure the mouse is properly connected.")

def build_menu_items():
    items = []
    for entry in MENU_CONFIG:
        if entry is None:
            items.append(rumps.separator)
        else:
            label, sequence = entry
            callback = (lambda _, s=sequence: run_usb_sequence(s)) if sequence else None
            items.append(rumps.MenuItem(label, callback=callback))
    return items

def run_app():
    app = rumps.App("🖱️", quit_button="Quit")
    app.menu = build_menu_items()
    app.run()

if __name__ == "__main__":
    run_app()
