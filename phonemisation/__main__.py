from argparse import ArgumentParser

from .romanisation import romanise_sentence

arg_parser = ArgumentParser()
arg_parser.add_argument("text", type=str, help="text to phonemise")
args = arg_parser.parse_args()

print(romanise_sentence(args.text, use_ipa=True))
