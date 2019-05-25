def generate_index_rst(file_path):

    template = """
Welcome to fake spotify's documentation!
========================================
.. mdinclude :: /home/alvaro/proyectos/fake_spotify/README.md
.. toctree::
   :maxdepth: 2
   :caption: Table of Contents
   :name: mastertoc

   models
   utils
   decorators
   app

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
    """

    with open(file_path, 'w') as f:
        f.write(template)
