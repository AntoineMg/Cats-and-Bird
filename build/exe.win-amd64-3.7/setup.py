from cx_Freeze import setup, Executable
base = None

executables = [Executable("main.py", base=base)]

packages = ["idna","os","sys","pygame","random","time"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}

setup(
    name = "Cat's & Bird",
    options = options,
    version = "0.4.3",
    description = 'Un super jeu !',
    executables = executables
)