### Desde consola:

### Desde yaml:

````yaml
####################################################
#                   GENERAL CONFIG                 #
####################################################
project_name: PyAutoDoc
author: Alvaro
version: 0.2
language_locale: es
root_folder: pyautodoc
output_folder: C:\Users\alvaro\Desktop\Nueva carpeta

####################################################
#                     EXTRA FILES                  #
####################################################
readme_file: README.md
license_file: LICENSE.md
changelog_file: CHANGELOG.md

####################################################
#                   PROJECT CONFIG                 #
####################################################
excludes:
  - scripts
  - i18n.exceptions.py

ignores:
  - test.py

mocks_imports:
  - django

####################################################
#                  COMPILING CONFIG                #
####################################################
makes:
  - html
  - pdf

####################################################
#                    HTML CONFIG                   #
####################################################
html_config:
  template_theme: alabaster

####################################################
#                 LaTeX PDF CONFIG                 #
####################################################
latex_config:
  latex_engine: pdflatex
  latex_logo: C:\Users\alvaro\Desktop\alvaro\cosillas\w.jpg



````