#------------------------------------------------------------------------------#

import csv
import hashlib
from pathlib import Path

from years        import create_years,   add_to_year
from schools      import create_schools, add_to_school
from dissertation import create_dissertation

# Input CVS files
csv_path = Path("csv")
# input_csv = csv_path / "teste.csv"
input_csv = csv_path / "todas_as_dissertacoes.csv"

# Output directories
docs_path          = Path("docs")
dissertations_path = docs_path / "dissertations"
schools_path       = docs_path / "schools"
years_path         = docs_path / "years"


#------------------------------------------------------------------------------#
def hash_row(row_dict):
    """
    Create a hash SHA256 based on line content
    """

    row_string = "|".join(row_dict[col] for col in row_dict)

    return hashlib.sha256(row_string.encode("utf-8")).hexdigest()

#------------------------------------------------------------------------------#
def main():

    create_years  (years_path)
    create_schools(schools_path)

    with open(input_csv, newline="", encoding="utf-8") as csv_file:

        reader = csv.DictReader(csv_file)

        ii = 0

        for row_dict in reader:

            year = row_dict["Ano Corrigido"]

            entry_hash = hash_row(row_dict)
            entry_path = f"{year}-{entry_hash}.md"

            create_dissertation(row_dict, dissertations_path / entry_path)
            add_to_year        (years_path,   row_dict, Path("../dissertations/") / entry_path )
            add_to_school      (schools_path, row_dict, Path("../dissertations/") / entry_path )

            ii += 1

    print(f"{ii} arquivos gerados com sucesso")


#------------------------------------------------------------------------------#
if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------#
