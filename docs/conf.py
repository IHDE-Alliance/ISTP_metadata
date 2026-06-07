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



# Custom slug function to preserve underscores in markdown header links

import re
from docutils import nodes
from sphinx.transforms import SphinxTransform

class MultiUnderscoreIdRestorer(SphinxTransform):
    """Restores underscores to section IDs, fully supporting multiple consecutive underscores."""

    default_priority = 100

    def apply(self):
        for node in self.document.findall(nodes.section):
            if "ids" in node:
                # Get the raw text of the markdown heading
                raw_title = node.astext().strip().lower()

                # If there are no underscores in the actual heading text, skip it completely
                if "_" not in raw_title:
                    continue

                new_ids = []
                for node_id in node["ids"]:
                    # Create an underscore-substituted version of the ID
                    fixed_id = node_id.replace("-", "_")

                    # Strip special characters from both to create a baseline check
                    clean_title = "".join(
                        c for c in raw_title if c.isalnum() or c in ("_", "-")
                    )
                    clean_fixed_id = "".join(
                        c for c in fixed_id if c.isalnum() or c in ("_", "-")
                    )

                    # Build a flexible regex sequence where hyphens match any boundary separator
                    # This safely links "a-b-c" (from Docutils) directly back to "a_b_c"
                    pattern = re.sub(r"[_\-]+", ".*", clean_fixed_id)

                    if re.search(pattern, clean_title) or clean_fixed_id in clean_title:
                        new_ids.append(fixed_id)
                    else:
                        new_ids.append(
                            node_id
                        )  # Fallback to the original hyphen id if it's a mismatch

                node["ids"] = new_ids

# Register with Sphinx
def setup(app):
    app.add_transform(MultiUnderscoreIdRestorer)
