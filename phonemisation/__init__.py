"""
This package is the phonemisation module, which is used to convert
Shanghainese text in Chinese characters to Shanghainese IPA transcriptions.
Hyphens ``-`` are used to separate syllables in a small word (typically
corresponding to left-dominant tone sandhi domains); equal signs ``=`` are
used to separate syllables in a major phrase (typically corresponding to
right-dominant tone sandhi domains).
"""

from .romanisation import romanise_sentence as phonemise

__all__ = ["phonemise"]
