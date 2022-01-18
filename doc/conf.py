from sys import path as sys_path
from os.path import abspath
from pathlib import Path
from json import loads

ROOT = Path(__file__).resolve().parent

sys_path.insert(0, abspath('.'))
sys_path.insert(0, abspath('..'))
sys_path.insert(0, abspath(str(ROOT.parent / 'openFPGALoader/doc')))


from constraints_data import generateBoardPages


generateBoardPages()


# -- Project information --------------------------------------------------

project =   "FPGA Board Constraints"
copyright = "2021-2021 The HDL Authors"
author =    "The HDL Authors"

version = "latest" # The short X.Y version.
release = "latest" # The full version, including alpha/beta/rc tags.


# -- Miscellaneous settings -----------------------------------------------

extensions = [
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
]

master_doc = 'index'

templates_path = ['_templates']

exclude_patterns = [
	"_build",
	"_theme",
	"Thumbs.db",
	".DS_Store"
]

pygments_style = 'stata-dark'


# -- Options for HTML output ----------------------------------------------

html_context = {}
ctx = ROOT / 'context.json'
if ctx.is_file():
	html_context.update(loads(ctx.open('r').read()))

if (ROOT / "_theme").is_dir():
	html_theme_path = ["."]
	html_theme = "_theme"
	html_theme_options = {
		'logo_only': True,
		'home_breadcrumbs': False,
		'vcs_pageview_mode': 'blob',
	}
else:
	html_theme = "alabaster"

html_static_path = ['_static']

html_logo = str(Path(html_static_path[0]) / "logo.svg")
html_favicon = str(Path(html_static_path[0]) / "icon.png")

htmlhelp_basename = 'HDLConstraintsDoc'

html_last_updated_fmt = "%Y.%m.%d"


# -- Options for LaTeX output ---------------------------------------------

from textwrap import dedent

latex_elements = {
	# The paper size ('letterpaper' or 'a4paper').
	'papersize': 'a4paper',

	# The font size ('10pt', '11pt' or '12pt').
	#'pointsize': '10pt',

	# Additional stuff for the LaTeX preamble.
	'preamble': dedent(r"""
		% ================================================================================
		% User defined additional preamble code
		% ================================================================================
		% Add more Unicode characters for pdfLaTeX.
		% - Alternatively, compile with XeLaTeX or LuaLaTeX.
		% - https://GitHub.com/sphinx-doc/sphinx/issues/3511
		%
		\ifdefined\DeclareUnicodeCharacter
			\DeclareUnicodeCharacter{2265}{$\geq$}
			\DeclareUnicodeCharacter{21D2}{$\Rightarrow$}
		\fi


		% ================================================================================
		"""),

	# Latex figure (float) alignment
	#'figure_align': 'htbp',
}

latex_documents = [
	( master_doc,
		'HDLConstraints.tex',
		'The FPGA Board Constraints Documentation',
		'The HDL Authors',
		'manual'
	),
]


# -- Sphinx.Ext.InterSphinx -----------------------------------------------

intersphinx_mapping = {
	'python':         ('https://docs.python.org/3', None),
	'openfpgaloader': ('https://trabucayre.github.io/openFPGALoader/', None)
}


# -- Sphinx.Ext.ExtLinks --------------------------------------------------

extlinks = {
	'ghrepo':  ('https://github.com/%s', ''),
	'ghissue': ('https://github.com/hdl/constraints/issues/%s', 'issue #'),
	'ghpull':  ('https://github.com/hdl/constraints/pull/%s', 'pull request #'),
	'ghsrc':   ('https://github.com/hdl/constraints/blob/main/%s', ''),
}
