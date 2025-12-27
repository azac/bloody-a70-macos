from setuptools import setup

APP = ['app.py']
DATA_FILES = ['driver.py', 'libusb-1.0.dylib', 'utils.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'LSUIElement': True, 
        'CFBundleName': 'BloodyController',
        'CFBundleDisplayName': 'Bloody Controller',
        'CFBundleGetInfoString': "Bloody Mouse Controller",
        'CFBundleIdentifier': "com.adrian.bloodycontroller",
        'CFBundleVersion': "0.1",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': u"free software"
    },
    'packages': ['rumps', 'usb'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
