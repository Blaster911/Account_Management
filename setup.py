from cx_Freeze import setup, Executable
base = None

executables = [Executable("account-management.py", base=base)]
packages = ["configparser", "crayons"]
options = {
    'build_exe': {
        'packages': packages,
    },
}
setup(
    name="account management",
    options=options,
    version="1.0",
    description='Voici mon programme de gestion de compte',
    executables=executables
)
