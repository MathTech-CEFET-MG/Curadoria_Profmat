#------------------------------------------------------------------------------#

import re
from schools_list import schools_list

# Clean unicode string
#------------------------------------------------------------------------------#
def unicode_clean(str):
    '''Remove non utf-8 characters'''

    str = bytes(str, 'utf-8').decode('utf-8', 'ignore')
    str = str.strip()

    return str

# Function to replace unicode by LaTeX commands
#------------------------------------------------------------------------------#
def unicode2latex( str ):

    return str.replace( 'º',     r'\textsuperscript{o}' ) \
              .replace( 'ª',     r'\textsuperscript{a}' ) \
              .replace( '×',     r'\texttimes{}' ) \
              .replace( '®',     r'\textsuperscript{\textregistered}' ) \
              .replace( '–',     r'--' ) \
              .replace( '&',     r'\&' ) \
              .replace( '“',     r'``' ) \
              .replace( '”',     r"''" ) \
              .replace( '‘',     r'`'  ) \
              .replace( '’',     r"'"  ) \
              .replace( '...',   r'\dots'    ) \
              .replace( 'LaTeX', r'\LaTeX{}' )

#-----------------------------------------------------------------------------#
def create_label( author, school, year ):

  label = author.strip() + ':' + school.strip() + ':' + year
  label = label.replace( ' ', '_' )
  label = label.replace( '"', ''  )
  label = label.replace( "'", ''  )

  label = label.upper()

  label = re.sub( '[ÁÀÂÃÂ]', 'A', label )
  label = re.sub( '[Ç]',     'C', label )
  label = re.sub( '[ÉÈÊ]',   'E', label )
  label = re.sub( '[Í]',     'I', label )
  label = re.sub( '[ÓÔÖÕ]',  'O', label )
  label = re.sub( '[ÚÙÜ]',   'U', label )

  label = label.encode( 'ascii', 'replace' )
  label = label.decode()

  label = re.sub( '[^A-Za-z0-9:_]+', '_', label )
  label = re.sub( '_+', '_', label )

  return label

#------------------------------------------------------------------------------#
def school_name( school ):

  try:
    name = schools_list[school][1]

  except KeyError:
    name = "?"

  return name

#-----------------------------------------------------------------------------#
def biblatex( row_dict ) -> str:

    year   = row_dict["Ano Corrigido"]
    date   = row_dict["Data Corrigida"]
    author = row_dict["Nome Corrigido"]
    title  = unicode2latex( row_dict["Título Corrigido"] )
    school = row_dict["Instituição Corrigida"]
    url    = row_dict["URL"]

    label  = create_label( author, school, year )
    school = school_name ( school )

    bib_str  = '    @mastersthesis{' + label  +  ',\n'
    bib_str += '      author = {'    + author + '},\n'
    bib_str += '      title  = {'    + title  + '},\n'
    bib_str += '      school = {'    + school + '},\n'
    bib_str += '      year   = {'    + year   + '},\n'
    bib_str += '      date   = {'    + date   + '},\n'
    bib_str += '      url    = {'    + url    + '},\n'
    bib_str += '    }\n\n'

    return bib_str

#------------------------------------------------------------------------------#
