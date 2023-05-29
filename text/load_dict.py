from collections import defaultdict
from csv import DictReader
from pathlib import Path

dict_file = (Path(__file__).parent / "yahwe_zaonhe.dict.tsv").open()
"""word,romanisation,freq"""

dict_reader = DictReader(dict_file, delimiter="\t")
raw_dict: defaultdict[str, dict[str | None, float]] = defaultdict(dict)
for row in dict_reader:
    word = row["word"]
    romanisation = row["romanisation"]
    freq = float(row["freq"].strip("%") if row["freq"] else 100)
    raw_dict[word][romanisation] = freq
dict_file.close()

romanisations: dict[str, str | None] = {}
for word, romanisation_dict in raw_dict.items():
    romanisations[word] = max(romanisation_dict, key=romanisation_dict.get)

romanisations = romanisations | {
    "，": ",",
    "。": ".",
    "？": "?",
    "！": "!",
    "、": ",",
    "；": ";",
    "：": ":",
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
    "（": "(",
    "）": ")",
    "《": "<",
    "》": ">",
}

__all__ = ["romanisations"]
