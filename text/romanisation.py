from re import split

from Qieyun.韻書和韻圖 import 字頭2音韻地位_出處們

from .load_dict import romanisations
from .word_segmentation import word_segmentation


def romanise_word(word: str) -> str:
    """
    Romanise a word.
    Use greedy algorithm to match as much as possible.
    Skip None romanisations.
    """
    r = []
    i = len(word)
    while i > 0:
        if word[:i] in romanisations and romanisations[word[:i]]:
            r.append(romanisations[word[:i]].replace(" ", "-"))
            word = word[i:]
            i = len(word)
        else:
            i -= 1
    return "=".join(r)


def is_清母_and_平聲(char: str) -> bool:
    # this is the only marked tone in Shanghainese
    音韻地位_出處們 = 字頭2音韻地位_出處們(char)
    if not 音韻地位_出處們:
        return False
    音韻地位 = 字頭2音韻地位_出處們(char)[0].音韻地位
    return 音韻地位.聲 == "平" and "清" in 音韻地位.清濁


def raw_romanise_sentence(text: str) -> str:
    """Romanise a sentence."""
    words = word_segmentation(text)
    return " ".join(romanise_word(word) for word in words)


def romanise_sentence(text: str) -> str:
    """Romanise a sentence with tone."""
    raw_romanisation = raw_romanise_sentence(text)
    # split_raw_romanisation = split(r"([ -=])", raw_romanisation)
    split_raw_romanisation = []
    i = 0
    b = ""
    for r in raw_romanisation:
        if r in [" ", "-", "="]:
            split_raw_romanisation.append(b)
            split_raw_romanisation.append(r)
            b = ""
        else:
            b += r

    # raw_romanisation is of format: r1-r2 r3=r4 (chars might be separated by space, hyphen or equal sign); need to align these with chars in original text
    corresponding_chars: list[tuple[str, str]] = []
    i = 0
    for r in split_raw_romanisation:
        if r in [" ", "-", "="]:
            corresponding_chars.append(("", r))
        else:
            corresponding_chars.append((text[i], r))
            i += 1

    # add tone number
    romanisation = ""
    for char, romanised_char in corresponding_chars:
        if char and is_清母_and_平聲(char):
            romanisation += f"{romanised_char}1"
        else:
            romanisation += romanised_char

    return romanisation
