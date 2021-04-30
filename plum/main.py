import argparse
import config
import os

def main():
    parser = argparse.ArgumentParser('plum')
    parser.add_argument('--init', help='Create new plum config file', action='store_true')
    parser.add_argument('--run', help='Run commands defined in config file', action='store', nargs='?')

    if parser.parse_args().init:
        config.create_new_file()

    if parser.parse_args().run:
        for script in config.get_config('scripts'):
            if parser.parse_args().run in script:
                print(f'Running {script[parser.parse_args().run]}...')
                os.system(script[parser.parse_args().run])
            else:
                print(f'Cannot find {parser.parse_args().run} in plum.json')

if __name__ == '__main__':
    main()