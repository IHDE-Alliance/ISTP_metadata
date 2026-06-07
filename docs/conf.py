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


# Set README as your main page
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


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["source/_static"]


# Prevent Intersphinx from hijacking local Markdown/unresolved references
intersphinx_disabled_reftypes = ["*"]


# Handle appedices in PDF correctly
# 1. Register your appendix document names (omit the extension)
latex_appendices = ["source/07_example-variables", "source/08_example-skeletontables", "source/Multi_Mission_Use_of_Attributes", "source/Non-ISTP-Mission-Global-Attributes", "source/Non-ISTP-Mission-Variable-Attributes", "source/best-practices", "source/faq"]

# 2. Prevent the fncychap package from rendering "Chapter X" headers over appendices
latex_elements = {
    'fncychap': '',  # Disables the default fancy chapter heading behavior
}


# Custom slug function to preserve underscores in markdown header links
from docutils import nodes
from sphinx.transforms import SphinxTransform

class DynamicIdRestorer(SphinxTransform):
    """Restores underscores to section IDs ONLY if they were present in the source heading."""

    # Run early in translation
    default_priority = 100

    def apply(self):
        # Scan every section in the document
        for node in self.document.findall(nodes.section):
            if "ids" in node:
                # Extract the actual raw heading string (e.g., "unit_ptr" or "some-hyphen")
                raw_title_text = node.astext().strip().lower()

                # If the raw title specifically contains an underscore, we fix the ID
                if "_" in raw_title_text:
                    new_ids = []
                    for node_id in node["ids"]:
                        # If Docutils made it "unit-ptr", but title has "unit_ptr", swap it
                        fixed_id = node_id.replace("-", "_")

                        # Double check against the source text to ensure validity
                        if fixed_id in raw_title_text or fixed_id.replace(
                            "_", ""
                        ) in raw_title_text.replace("_", ""):
                            new_ids.append(fixed_id)
                        else:
                            new_ids.append(
                                node_id
                            )  # Keep original if it doesn't match match layout

                    node["ids"] = new_ids

# Register the smart transform with Sphinx
def setup(app):
    app.add_transform(DynamicIdRestorer)
