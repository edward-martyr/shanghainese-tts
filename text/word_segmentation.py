from jieba import add_word, lcut
from opencc import OpenCC

from .load_dict import romanisations

s2t = OpenCC("s2t.json").convert  # convert to traditional Chinese

for word in romanisations:
    add_word(word)


def word_segmentation(text: str) -> list[str]:
    return lcut(s2t(text))


__all__ = ["word_segmentation"]
