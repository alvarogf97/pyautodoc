import yaml
import os
from pyautodoc.generators.sphinx_structure import generate_structure


if __name__ == '__main__':

    with open('pydoc.yaml', 'r') as stream:
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
