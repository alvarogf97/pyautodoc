from templates.structure import generate_structure


if __name__ == '__main__':

    print('======================================')
    print('=    sphinx automatization module    =')
    print('======================================')
    print('\n \n')

    project_name = input('Enter project name: ')
    author = input('Enter author: ')
    version = input('Enter current version: ')
    language_locale = input('Enter language locale (leave blank for en): ')
    if language_locale == '':
        language_locale = 'en'
    root_folder = input('Enter path for root project folder: ')
    readme_file = input('Enter path for README.md (leave blank if you don\'t want to include it): ')
    license_file = input('Enter path for LICENSE.md (leave blank if you don\'t want to include it): ')
    changelog_file = input('Enter path for CHANGELOG.md (leave blank if you don\'t want to include it):')
    generate_structure(root_folder, project_name, author, version, language_locale)