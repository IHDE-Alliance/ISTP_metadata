# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "ISTP Metadata Guidelines"
copyright = "CC0 1.0 Universal"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

#intersphinx_mapping = {
#    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
#    "python": ("https://docs.python.org/3/", None),
#    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
#}

# templates_path = ["_templates"]


# Set index.rst as the main page
root_doc = 'index'


# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}


# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"


# Show pointer to GitHub repository
html_theme_options = {
    'github_user': 'IHDE-Alliance',
    'github_repo': 'ISTP_metadata',
    'github_banner': True,
    'github_button': False,
    'github_type': 'star',
    'fixed_sidebar': False,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["source/_static"]


# Prevent Intersphinx from hijacking local Markdown/unresolved references
intersphinx_disabled_reftypes = ["*"]


# Handle appendices in PDF correctly
# Register your appendix document names (omit the extension)
latex_appendices = ["source/07_example-variables", "source/08_example-skeletontables", "source/Multi_Mission_Use_of_Attributes", "source/Non-ISTP-Mission-Global-Attributes", "source/Non-ISTP-Mission-Variable-Attributes", "source/best-practices", "source/faq"]

# LaTeX
latex_elements = {
    # Prevent the fncychap package from rendering "Chapter X" headers over appendices
    'fncychap': '', 

    'pointsize': '11pt',
    'classoptions': ',oneside',
    "sphinxsetup": "hmargin={0.5in,0.5in}, vmargin={0.5in,0.5in}",

}


# Configure Sphinx to clone GitHub's exact header-slug behaviour
myst_heading_anchors = 4 # Enable auto-generation for headers up to level 4


# MyST-Parser extensions
myst_enable_extensions = [
    "html_image",  # Enables correct handling of <img> tags
]


# Display release version (for stable release) or show "latest" (for GitHub update without release)
# Check if the build is running on Read the Docs servers
if os.environ.get('READTHEDOCS') == 'True':
    # Read the dynamic version string injected by the build system
    rtd_version = os.environ.get('READTHEDOCS_VERSION')
    
    # Sphinx variable for short version (displayed in headers/footers)
    version = rtd_version
    # Sphinx variable for full version (displayed on PDF covers/titles)
    release = rtd_version
else:
    # Local fallback settings for when you run 'make html' on your machine
    version = 'local-development'
    release = 'local-development-draft'



# --- Dynamic Markdown replacement for PDF Builder ---

def replace_br_for_pdf(app, docname, source):
    """Intercepts source text and replaces <br> with LaTeX breaks ONLY for PDF builds."""
    # Check if the active builder is the PDF/LaTeX compiler
    if app.builder.name in ('latex', 'pdf'):
        # source is passed as a single-element list containing the full file text
        result = source[0]
        
        # Replace common variations of the HTML break tag
        result = result.replace('<br>', r'\hfill \break')
        result = result.replace('<br/>', r'\hfill \break')
        result = result.replace('<br />', r'\hfill \break')
        
        source[0] = result

def setup(app):
    """Registers the source-read event handler into Sphinx."""
    app.connect('source-read', replace_br_for_pdf)

