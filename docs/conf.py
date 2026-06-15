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


# Set index.rst as the main page
root_doc = 'index'


# -- Project information -----------------------------------------------------

project = "ISTP Metadata Guidelines"
copyright = "CC0 1.0 Universal"
author_list = ["Ramona L. Kessel", "Robert E. McGuire", "D. Aaron Roberts", "Robert M. Candey", "Andriy Koval", "Reine Chimiak", "Lan Jian", "Tamara J. Kovalick", "Sarah M. Fooks", "Eric W. Grimes", "Bernard T. Harris", "Alfredo A. Cruz", "Rita C. Johnson", "Fernando Carcaboso Morales"]

# Automatically formats for HTML front page/footer:
author = ", ".join(author_list)

# Automatically injects LaTeX breaking syntax for the PDF version
latex_author = r", \and ".join(author_list)

# Pass the variables seamlessly into their respective configurations
latex_documents = [
    (
        root_doc,
        'istp_metadata.tex',
        project,
        latex_author,     # Standardized list containing \and breaks
        'manual'
    ),
]

# This injects the |author| substitution globally
rst_epilog = f"""
.. |author| replace:: {author}
"""


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
    "sphinx.ext.imgconverter"
]

#intersphinx_mapping = {
#    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
#    "python": ("https://docs.python.org/3/", None),
#    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
#}

# templates_path = ["_templates"]



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
    'sidebar_width': '270px',
    # Injects custom CSS securely on Read the Docs to force the margin
    'extra_nav_links': {
        '<style>img.logo, .sphinxsidebar img { margin-bottom: 40px !important; }</style>': ''
    }
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["source/_static", "logo"]


html_css_files = ['custom.css']

# Logo
html_logo = "logo/ISTP_Metadata_icon.svg"
html_favicon = "logo/ISTP_Metadata_icon.svg"

# Add the logo for PDF/LaTeX generation
latex_logo = 'logo/ISTP_Metadata_icon.png' 


# Prevent Intersphinx from hijacking local Markdown/unresolved references
intersphinx_disabled_reftypes = ["*"]


# Handle appendices in PDF correctly
# Register your appendix document names (omit the extension)
latex_appendices = ["source/07_example-variables", "source/08_example-skeletontables", "source/Multi_Mission_Use_of_Attributes", "source/Non-ISTP-Mission-Global-Attributes", "source/Non-ISTP-Mission-Variable-Attributes", "source/best-practices", "source/faq"]


# Force Sphinx to automatically calculate relative column widths for Markdown tables
# This assigns cell boundaries that text can actually wrap against
myst_table_header_printed = True 


# LaTeX settings
latex_elements = {
    'pointsize': '11pt',
    'classoptions': ',oneside',
    "sphinxsetup": "hmargin={0.5in,0.5in}, vmargin={1.0in,1.0in}, inlineliteralwraps=true",

    # Prevent the fncychap package from rendering "Chapter X" headers over appendices
    'fncychap': '', 

    # This forces the PDF builder to auto-wrap and dynamically size 
    # all standard Markdown tables instead of squishing them
    'colwidths': 'auto',

    # Force Sphinx to wrap literal inline layouts
    'preamble': r'''
        % Completely turn off standard syllable hyphenation dashes globally
        \hyphenpenalty=10000
        \exhyphenpenalty=10000
        
        % Force extreme character wrapping points at technical symbols (underscores, dots, slashes)
        \usepackage{url}
        \makeatletter
        \g@addto@macro\UrlBreaks{\do\_\do\.\do\/\do\-\do\\\do\:\do\&\do\%}
        \makeatother
        
        % Instruct LaTeX to allow splitting text on any arbitrary character if forced
        \emergencystretch=3em
        \tolerance=9999




        \usepackage{ragged2e}
        \usepackage{etoolbox}

        % Tell LaTeX how to break words inside table columns explicitly
        % This enables breaks at underscores, hyphens, and slashes without code adjustments
        \makeatletter
        \newcommand{\forcecellwrap}{%
          \spaceskip=0.33em\relax % Force normal space sizing (no shrinking)
          \RightToLeft % Keeps natural text reading order
          \setlength{\emergencystretch}{3em}% Allows engine to break lines earlier
        }
        
        % Safe interceptor for Markdown backticks (`` `code` ``)
        \protected\def\sphinxupquote#1{%
          \bgroup
          \fontfamily{tt}\selectfont
          % Use a safe parsing token to preserve spaces completely
          \expandafter\RaggedRight\hspace{0pt}#1%
          \egroup
        }
        \makeatother

        % Force multi-line table code blocks to comply with the wrap settings
        \appto\sphinxsetup{\fvset{breaklines=true}}

        % Override the logo command to enforce a specific width, relative to text width

        \renewcommand{\sphinxlogo}{
            \begin{center}
                % Clear any default paragraph indentations
                \noindent
                %Force the image to the right
                \hfill 
                \includegraphics[width=0.35\textwidth]{ISTP_Metadata_icon.png} 
                %Inject 2 centimeters of vertical space below the logo
                \vspace{2cm}                          
            \end{center}
        }
    ''',

}


# Tell the LaTeX compiler to strictly use tabulary to enforce paper boundaries
latex_table_style = ['tabulary']


# Configure Sphinx to clone GitHub's exact header-slug behaviour
myst_heading_anchors = 4 # Enable auto-generation for headers up to level 4


# MyST-Parser extensions
myst_enable_extensions = [
    "html_image",  # Enables correct handling of <img> tags
    "html_admonition",
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




# Handle <br> in PDF table cells

import re

def process_raw_markdown_tables(app, docname, source):
    """
    Processes the raw Markdown text before MyST or LaTeX can alter it.
    Forces uniform column blocks, switches on wrapping, and applies hard line breaks.
    """
    raw_markdown = source[0]

    # --- 1. HANDLE COEXISTING HARD <br> TAGS FOR BOTH HTML & PDF ---
    if app.builder.name in ['latex', 'pdf']:
        # Convert HTML breaks to literal LaTeX newline declarations inside LaTeX cells
        raw_markdown = re.sub(r'<br\s*/?>', r'\\newline ', raw_markdown, flags=re.IGNORECASE)
    else:
        # Keep standard HTML breaks operational for web builds
        raw_markdown = re.sub(r'<br\s*/?>', r'<br>', raw_markdown, flags=re.IGNORECASE)

    # --- 2. ENFORCE COLUMNS & WORD WRAPPING GLOBALLY ---
    if app.builder.name in ['latex', 'pdf']:
        lines = raw_markdown.split('\n')
        processed_lines = []
        in_table = False
        table_lines = []

        for line in lines:
            # Detect a standard Markdown pipe table boundary row
            if re.match(r'^\s*\|.*\|\s*$', line):
                in_table = True
                table_lines.append(line)
            else:
                if in_table and table_lines:
                    # Determine column counts by analyzing the separator row structure
                    col_count = 0
                    for t_line in table_lines:
                        if '---' in t_line:
                            col_count = t_line.count('|') - 1
                            break
                    if col_count <= 0:
                        col_count = table_lines[0].count('|') - 1

                    if col_count > 0:
                        # Construct a custom, bulletproof LaTeX layout format specifier
                        # e.g., 3 columns -> |\X{1}{3}|\X{1}{3}|\X{1}{3}|
                        spec_parts = [rf"\X{{1}}{{{col_count}}}" for _ in range(col_count)]
                        col_spec = f"|{'|'.join(spec_parts)}|"
                        
                        # Wrap the entire table in an explicit directive override block
                        processed_lines.append(f"\n\n.. tabularcolumns:: {col_spec}\n\n")
                    
                    processed_lines.extend(table_lines)
                    table_lines = []
                    in_table = False
                
                processed_lines.append(line)
        
        # Catch any trailing tables sitting at the very end of a file
        if in_table and table_lines:
            col_count = table_lines[0].count('|') - 1
            if col_count > 0:
                spec_parts = [rf"\X{{1}}{{{col_count}}}" for _ in range(col_count)]
                col_spec = f"|{'|'.join(spec_parts)}|"
                processed_lines.append(f"\n\n.. tabularcolumns:: {col_spec}\n\n")
            processed_lines.extend(table_lines)

        raw_markdown = '\n'.join(processed_lines)

    # Overwrite the Sphinx memory source payload safely in place
    source[0] = raw_markdown

def setup(app):
    # Hook directly into the source reading process before any engine execution
    app.connect('source-read', process_raw_markdown_tables)
