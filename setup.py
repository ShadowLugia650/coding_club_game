from cx_Freeze import setup, Executable
import sys, os

__version__ = ""
include_files = ['data/','dependencies/','resources/','Rooms/',
                 'Mtesting.py', 'main.py']

ex = Executable(
    script="main_pygame.py",
    base="Win32GUI",
    icon='resources/icon.ico' #add this in
    )

setup(
    name = "Coding Club Game", #Give me a good name
    description = "A text-based dungeon crawler with visual effects.",
    version = __version__,
    options = {"build_exe": {
        'include_files': include_files,
        'include_msvcr': True
        }},
    executables = [ex]
    )
