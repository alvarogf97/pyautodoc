import os
import sys
import yaml
from pyautodoc.generators.sphinx_structure import generate_structure
from pyautodoc.utils.stringify import convert_path


def from_console():
    print('======================================')
    print('=    sphinx automatization module    =')
    print('======================================')
    print('\n')

    project_name = input('Enter project name: ')
    author = input('Enter author: ')
    version = input('Enter current version: ')
    language_locale = input('Enter language locale (leave blank for es): ')
    if language_locale == '':
        language_locale = 'es'

    root_folder = ""
    while not os.path.isdir(root_folder):
        root_folder = convert_path(input('Enter path for root project folder: '))

    readme_file = input('Enter path for README.md (leave blank if you don\'t want to include it): ')
    license_file = input('Enter path for LICENSE.md (leave blank if you don\'t want to include it): ')
    changelog_file = input('Enter path for CHANGELOG.md (leave blank if you don\'t want to include it): ')

    output_folder = convert_path(input('Enter path for Output folder: '))
    while not os.path.isdir(output_folder):
        try:
            os.mkdir(output_folder)
        except FileNotFoundError:
            print('Output folder doesn\'t exists')
            output_folder = convert_path(input('Enter path for Output folder: '))

    os.chdir(output_folder)

    generate_structure(root_folder, project_name, author, version, language_locale, readme_file, license_file,
                       changelog_file)


def from_yaml(file):

    with open(file, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            output_folder = config['output_folder']
            os.chdir(output_folder)
            generate_structure(config['root_folder'], config['project_name'], config['author'],
                               config['version'], config.get('language_locale', 'es'), config.get('readme_file', ''),
                               config.get('license_file', ''), config.get('changelog_file', ''))
        except yaml.YAMLError as e:
            print('Invalid yaml file structure: ' + str(e))
        except KeyError as e:
            print('Required config param: ' + str(e))
        except Exception as e:
            print('Invalid path for output or root folder ' + str(e))


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--yaml':
            yaml_file = ''
            try:
                yaml_file = sys.argv[2]
            except IndexError:
                yaml_file = 'pydoc.yaml'
            if not os.path.isfile(yaml_file):
                print('yml document not found!')
            else:
                from_yaml(yaml_file)
        else:
            print('Invalid option: ' + sys.argv[1])
    else:
        from_console()
