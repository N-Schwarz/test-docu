project = 'Example Program'
author = 'Your Name'

extensions = [
    'sphinx.ext.autodoc',
]

html_theme = 'alabaster'
html_logo = "_static/cat.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}


html_static_path = ["_static"]