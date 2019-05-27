import os
from pyautodoc.generators.sphinx_structure import generate_structure
from pyautodoc.i18n.dictionary import Locale
from pyautodoc.utils.stringify import convert_path


if __name__ == '__main__':

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

    Locale(locale=language_locale)

    root_folder = ""
    while not os.path.isdir(root_folder):
        root_folder = input('Enter path for root project folder: ')

    root_folder = convert_path(root_folder)
    readme_file = input('Enter path for README.md (leave blank if you don\'t want to include it): ')
    license_file = input('Enter path for LICENSE.md (leave blank if you don\'t want to include it): ')
    changelog_file = input('Enter path for CHANGELOG.md (leave blank if you don\'t want to include it):')
    generate_structure(root_folder, project_name, author, version, language_locale, readme_file, license_file,
                       changelog_file)
