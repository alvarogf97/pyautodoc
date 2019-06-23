import os
import sys
import yaml
import traceback
import shutil
from pyautodoc.generators.sphinx_structure import generate_structure
from pyautodoc.utils.stringify import convert_path
from pyautodoc.utils.path import get_abs_path, path_leaf


make_actions = {
    'html': 'make html',
    'pdf': 'make latexpdf'
}


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
            yaml_folder = os.path.abspath(os.path.dirname(file))
            config = yaml.safe_load(stream)
            output_folder = get_abs_path(convert_path(config['output_folder']), yaml_folder)

            readme_file = get_abs_path(config.get('readme_file', ''), yaml_folder) \
                if config.get('readme_file', '') != '' else ''
            license_file = get_abs_path(config.get('license_file', ''), yaml_folder) \
                if config.get('license_file', '') != '' else ''
            changelog_file = get_abs_path(config.get('changelog_file', ''), yaml_folder) \
                if config.get('changelog_file', '') != '' else ''

            html_logo_file_path = config.get('html_config', {}).get('template_options', {}).get('logo')
            if html_logo_file_path is not None:
                html_logo_file_path = get_abs_path(html_logo_file_path, yaml_folder)
                config['html_config']['template_options']['logo'] = path_leaf(html_logo_file_path)

            if not os.path.isdir(output_folder):
                os.mkdir(output_folder)
            else:
                if os.path.isdir(output_folder + '/source'):
                    shutil.rmtree(output_folder + '/source', ignore_errors=True)
                if os.path.isdir(output_folder + '/build'):
                    shutil.rmtree(output_folder + '/build', ignore_errors=True)
            os.chdir(output_folder)
            generate_structure(convert_path(get_abs_path(config['root_folder'], yaml_folder)), config['project_name'],
                               config['author'], config['version'], config.get('language_locale', 'es'),
                               readme_file, license_file, changelog_file, config.get('excludes'),
                               config.get('ignores'), config.get('html_config'), config.get('latex_config'),
                               config.get('mocks_imports'), config.get('sphinx_extensions'), config.get('indexes'))

            if html_logo_file_path is not None and os.path.isdir('./source/_static'):
                shutil.copy(html_logo_file_path, './source/_static')

            if config.get('html_config', {}).get('custom_css') is not None:
                css_path = convert_path(get_abs_path(config['html_config']['custom_css'], yaml_folder))
                if os.path.isfile(css_path):
                    shutil.copy(css_path, './source/_static')
                    os.rename('./source/_static/' + path_leaf(css_path), './source/_static/custom.css')
                else:
                    print('cannot import custom css, file: ' + css_path + ' does not exists')

            makes = config.get('makes', [])
            for make_action in makes:
                try:
                    os.system(make_actions.get(make_action))
                except Exception:
                    print('Action: ' + make_action + ' not available')

        except yaml.YAMLError as e:
            print('Invalid yaml file structure: ' + str(e))
        except KeyError as e:
            print('Required config param: ' + str(e))
        except Exception as e:
            print(traceback.format_exc())
            print('Invalid path for output or root folder ' + str(e))


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--yaml':
            try:
                yaml_file = sys.argv[2]
            except IndexError:
                yaml_file = 'pydoc.yaml'
            if not os.path.isfile(yaml_file):
                print('yaml document not found!')
            else:
                from_yaml(yaml_file)
        else:
            print('Invalid option: ' + sys.argv[1])
    else:
        from_console()


if __name__ == '__main__':
    main()
