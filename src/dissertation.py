#------------------------------------------------------------------------------#

from biblatex import biblatex

#------------------------------------------------------------------------------#
def create_dissertation(row_dict, file_path):
    """
    Create a markdown file to a dissertation
    """

    date   = row_dict["Data Corrigida"]
    author = row_dict["Nome Corrigido"]
    title  = row_dict["Título Corrigido"]
    school = row_dict["Instituição Corrigida"]
    note   = row_dict["Note"]

    with open(file_path, "w", encoding="utf-8") as f:

        f.write(f"# {title}\n\n")
        f.write(f"Autor: __{author}__\n\n")
        f.write(f"Defendida na __{school}__ em {date}\n\n")

        if note:
            f.write(f"Observação: {note}\n\n")

        f.write('??? abstract "BibLaTeX"\n')
        f.write('    ```latex\n')
        f.write(biblatex(row_dict))
        f.write('    ```\n')

#------------------------------------------------------------------------------#