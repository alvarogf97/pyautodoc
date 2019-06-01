## En pocas palabras:

Pyautodoc permite la creación de documentación de los proyectos python de forma totalmente automática y
configurable. Hace uso del proyecto [Sphinx](http://www.sphinx-doc.org/en/master/) y de extensiones como 
[autodoc](http://www.sphinx-doc.org/es/stable/ext/autodoc.html) para generar la documentación en función
de los **docstring** de las clases y métodos del proyecto. 

## Instalación:

Desde **github** podemos instalarlo ejecutando:
````cmd
pip install git+https://github.com/alvarogf97/pyautodoc.git
````

Desde **PyPi**:

````cmd
Próximamente
````

## Uso

**NOTA**:
para compilar a latex es necesario tener instalado compilador para el mismo. En windows se necesita 
**MiKTeX** y **Perl**

### Desde consola:

Ejecutamos el comando:

````cmd
pyautodoc
````

Indicamos los datos necesarios:

````cmd
Enter project name: <Nombre del proyecto>
Enter author: <Autor>
Enter current version: <Version>
Enter language locale (leave blank for es): <Código del país para las traducciones>
Enter path for root project folder: <carpeta del proyecto a documentar>
Enter path for README.md (leave blank if you don't want to include it): <fichero readme>
Enter path for LICENSE.md (leave blank if you don't want to include it): <fichero license>
Enter path for CHANGELOG.md (leave blank if you don't want to include it): <fichero changelog>
Enter path for Output folder: <Carpeta para generar la documentación>
````

En la carpeta **output/source** se encontrarán los ficheros generados. Para compilar a html o pdf ejecutamos:
````cmd
make html
make latexpdf
````
desde la carpeta **output**

### Desde yaml:

Podemos crear un fichero ```pydoc.yaml``` con la configuración necesaria para la generación automática de la
documentación, esta opción permite una configuración mucho mas amplia que la generación por consola.

La estructura del documento ```pydoc.yaml``` es: 

````yaml
####################################################
#                   GENERAL CONFIG                 #
####################################################
project_name: PyAutoDoc
author: Alvaro
version: 0.5
language_locale: es
root_folder: pyautodoc
output_folder: MyOutputFolder

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

ignores:
  - test.py

mocks_imports:
  - django
  - pyautodoc

####################################################
#                  COMPILING CONFIG                #
####################################################
makes:
  - html
  #- pdf

####################################################
#                    HTML CONFIG                   #
####################################################
html_config:
  template_theme: alabaster
  #template_package: sphinx_theme
  #template_path: sphinx_theme.get_html_theme_path('stanford-theme')
  template_options:
    logo: MyLogo
    github_user: alvarogf97
    github_repo: pyautodoc
    fixed_sidebar: True
    description: Pyautodoc! Automatize your python project documentation

####################################################
#                 LaTeX PDF CONFIG                 #
####################################################
latex_config:
  latex_engine: pdflatex
  latex_logo: MyLogo
````

Para generar la documentación ejecutamos:
````cmd
pyautodoc --yaml
````

Alternativamente, si el fichero ``.yaml`` tiene otro nombre, o esta en otra localización, podemos
ejecutar:

````cmd
pyautodoc --yaml <Ruta del fichero .yaml>
````