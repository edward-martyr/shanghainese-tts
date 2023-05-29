from pathlib import Path
from re import sub

from text.romanisation import romanise_sentence

data_folders = Path("data").resolve().glob("*")

for folder in data_folders:
    txts = sorted(folder.glob("txts/*"))
    wavs = sorted(folder.glob("wavs/*"))
    assert len(txts) == len(wavs)

    with open(folder / "metadata.txt", "w") as f:
        for txt, wav in zip(txts, wavs):
            transcription = sub("\w\.", "", txt.read_text())
            transcription = sub("伊", "佢", transcription)
            romanised = romanise_sentence(transcription)
            f.write(f"{wav.name}|{romanised}\n")
