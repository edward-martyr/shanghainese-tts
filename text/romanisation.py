from re import sub

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


def romanisation_to_ipa(text: str) -> str:
    text = sub("syu", "sy", text)

    text = sub("gh", "ɦ", text)
    text = sub("sh", "ɕ", text)

    text = sub("h$", "ʔ", text)
    text = sub("eʔ$", "əʔ", text)
    text = sub("iʔ$", "ɪʔ", text)
    text = sub("aʔ$", "ɐʔ", text)
    text = sub(r"(.)h", r"\1ʰ", text)

    text = sub("eu$", "ɤ", text)
    text = sub("au$", "ɔ", text)

    text = sub("^ny", "ɲi", text)
    text = sub("yu", "y", text)
    text = sub("y$", "z", text)
    text = sub("^y", "ɦi", text)
    text = sub("ii", "i", text)
    text = sub("iu", "y", text)
    # text = sub(r"ɲi([^nʔ])", r"ɲ\1", text)

    text = sub("ao", "ɑ", text)
    text = sub("on$", "oŋ", text)
    text = sub("in$", "ɪɲ", text)
    text = sub("en$", "əŋ", text)
    text = sub("a$", "ɑ", text)
    text = sub("n$", "̃", text)

    text = sub("j", "ɟ", text)
    text = sub("ts", "ʦ", text)
    text = sub("ng", "ŋ", text)
    text = sub("oe", "ø", text)
    text = sub(r"(.)u(.)", r"\1ʷ\2", text)
    return text


def romanise_sentence(text: str, use_ipa=True) -> str:
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
    split_raw_romanisation.append(b)

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
        if use_ipa:
            romanised_char = romanisation_to_ipa(romanised_char)
        if char and is_清母_and_平聲(char):
            romanisation += f"{romanised_char}1"
        else:
            romanisation += romanised_char

    return romanisation
