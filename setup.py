from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('runner.py', base=base)
]

build_exe_options = {
    "include_files":["utils","upgrading"],        #包含外围的ini、jpg文件，以及data目录下所有文件，以上所有的文件路径都是相对于cxsetup.py的路径。
    "packages": ["os","requests","json","re","queue"],
    "includes":["lxml","lxml.etree"]#包含用到的包
};

setup(name='test',
      version = '1.0',
      description = 'ceshi',
      options = dict(build_exe = build_exe_options),
      executables = executables)
