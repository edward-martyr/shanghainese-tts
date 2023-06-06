from pathlib import Path
from re import sub

from phonemisation.romanisation import romanise_sentence

data_folders = Path("data").resolve().glob("*")

for folder in (
    f
    for f in data_folders
    # skip hidden folders
    if not f.stem.startswith(".")
):
    txts = sorted(folder.glob("txts/*"))
    wavs = sorted(folder.glob("wavs/*"))
    assert len(txts) == len(wavs)  # check the number of files

    with open(folder / "metadata.txt", "w") as f:
        for txt, wav in zip(txts, wavs):
            # correct some common transcription errors
            # for example, 特's Mandarin pronunciation is similar to 脱's
            # pronunciation in Shanghainese, so it is often misused. It's
            # a common language practice but we need to correct these for
            # the phonemisation to work correctly
            transcription = sub("\w\.", "", txt.read_text())
            transcription = sub("伊", "佢", transcription)
            transcription = sub("[额呃]", "个", transcription)
            transcription = sub("萨", "啥", transcription)
            transcription = sub("窝里", "屋里", transcription)
            transcription = sub("特", "脱", transcription)
            romanised = romanise_sentence(transcription)
            f.write(f"{wav.name}|{romanised}\n")
