import os
import sys
import config

def install_dep(dev=False):
    config_dep = 'dependency'
    dep_text = ''
    if dev:
        config_dep = 'devDependency'
        dep_text = 'development'

    if config.get_config('dependency'):
        print(f"Installing {dep_text} dependencies from {config.get_config(config_dep)}...")
        os.system(sys.executable + f" -m pip install -r {config.get_config(config_dep)}")