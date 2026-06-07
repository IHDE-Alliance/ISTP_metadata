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

class PreciseIdRestorer(SphinxTransform):
    """Reconstructs section IDs directly from source text to respect mixed underscores and hyphens."""

    default_priority = 100

    def apply(self):
        for node in self.document.findall(nodes.section):
            if "ids" in node:
                # 1. Get raw heading text (e.g., "delta_plus-delta_minus")
                raw_title = node.astext().strip().lower()

                # If there are no underscores anywhere in the text, let Docutils handle it safely
                if "_" not in raw_title:
                    continue

                # 2. Reconstruct the ideal slug directly from the source text
                # Replace spaces/whitespace sequences with hyphens (standard web practice)
                ideal_slug = re.sub(r"\s+", "-", raw_title)

                # Strip out everything except alphanumerics, underscores, and hyphens
                # (This removes punctuation like ?, !, commas, etc.)
                ideal_slug = "".join(
                    c for c in ideal_slug if c.isalnum() or c in ("_", "-")
                )

                # Clean up any accidental double hyphens/underscores caused by punctuation removal
                ideal_slug = re.sub(r"-+", "-", ideal_slug)
                ideal_slug = re.sub(r"_+", "_", ideal_slug)
                ideal_slug = ideal_slug.strip("-_")

                if not ideal_slug:
                    continue

                # 3. Update the node IDs matching this pattern
                new_ids = []
                for node_id in node["ids"]:
                    # If this is the main auto-generated ID or a numerical variant (e.g. -1, -2)
                    # We match it to our ideal layout
                    if node_id.startswith(
                        ideal_slug.replace("_", "-").replace("-", "-")
                    ):
                        # Preserve suffix numbers if Docutils added uniqueness markers (like delta-plus-1)
                        suffix = node_id[
                            len(ideal_slug.replace("_", "-")) :
                        ]  # Capture any trailing numbers
                        new_ids.append(f"{ideal_slug}{suffix}")
                    else:
                        new_ids.append(node_id)

                node["ids"] = new_ids

# Register the updated transform with Sphinx
def setup(app):
    app.add_transform(PrecerveIdRestorer if "PrecerveIdRestorer" in locals() else PreciseIdRestorer)
