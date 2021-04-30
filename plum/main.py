import argparse
import config
import os
import sys
import dependency

def main():
    parser = argparse.ArgumentParser('plum')
    parser.add_argument('--init', help='Create new plum config file', action='store_true')
    parser.add_argument('--run', help='Run commands defined in config file', action='store', nargs='?')
    parser.add_argument('--install', help='Install requirements', action='store_true')
    parser.add_argument('--install-dev', help='Install dev requirements', action='store_true')


    if parser.parse_args().init:
        config.create_new_file()

    if parser.parse_args().run:
        for script in config.get_config('scripts'):
            if parser.parse_args().run in script:
                print(f'Running {script[parser.parse_args().run]}...')
                os.system(script[parser.parse_args().run])
            else:
                print(f'Cannot find {parser.parse_args().run} in plum.json')

    if parser.parse_args().install:
        dependency.install_dep()
    if parser.parse_args().install_dev:
        dependency.install_dep(dev=True)

if __name__ == '__main__':
    main()