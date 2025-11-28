# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'syw.accountonline.login'
copyright = '2025, SYW'
author = 'SYW Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional)
# html_theme = 'sphinx_rtd_theme'

# ✅ SEO-Optimized Titles with Your Keyword
html_title = "syw.accountonline.login – Easy Login Guide for SYW Account Access"
html_short_title = "SYW Account Login Guide"

# ✅ SEO Meta Tags
html_meta = {
    "description": "Visit syw.accountonline.login to securely access your SYW account. Step-by-step login guide, troubleshooting, and account recovery tips.",
    "keywords": "syw.accountonline.login, SYW login, SYW account access, SYW online account, SYW login help"
}

# Favicon
html_favicon = 'favicon.ico'

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files (for buttons)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets
# html_static_path = ['_static']
