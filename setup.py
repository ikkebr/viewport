import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Simple VLC ViewPort Generator",
        version = "0.1",
        description = "Generates a ViewPort using VLC that can then be used to share a portion of the screen on MS Teams",
        options = {"build_exe": build_exe_options},
        executables = [Executable("simple.py", base=base)])
