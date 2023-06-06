# Shanghainese TTS

- Dartmouth LING 48 Final Project: _Improving TTS for Shanghainese_
- Yuanhao Chen <yuanhao.chen.25@dartmouth.edu> Spring 2023

## Goal

To build a text-to-speech (TTS) system for Shanghainese from scratch, seeking to improve the production of tone sandhi compared to existing models by paying special attention to preprocessing of text.

## Description

See [writeup/main.pdf](writeup/main.pdf).

## Dependencies

```bash
pip install -r phonemisation/requirements.txt
pip install -r speech_synthesis/requirements.txt
pip install -r comparison_questionnaire/requirements.txt  # for analysis of questionnaire results
```

## Usage

See [`speech_synthesis/README.md`](speech_synthesis/README.md).

## Structure

- `phonemisation/`: contains the phonemisation model
  - See explanation of output in [`phonemisation/__init__.py`](phonemisation/__init__.py)
  - Usage: `python -m phonemisation "text to phonemise"`
  - Mechanism: **Chinese sentence** — _word segmentation_ ⟶ **Chinese words** — _romanisation_ ⟶ **Shanghainese pinyin** — _phonemisation_ ⟶ **Shanghainese phonemes**
    - `jieba` is used for word segmentation
    - [A Shanghainese dictionary I previously made](https://github.com/edward-martyr/rime-yahwe_zaonhe/blob/3b61ea98fc2dfa023df6c351aa1bd518d6dc79c8/yahwe_zaonhe.dict.yaml#L25) is used for romanisation
      - Uses `Qieyun` module to add the tone number `1` to syllables of 陰平 _yinping_/_inbin_ tone; other tones are phonologically unmarked
    - The `romanisation_to_ipa` function in `romanisation.py` contains the phonemisation function
- `make_metadata.py`: uses the `phonemisation` module to convert transcription into IPA and generate metadata for training
  - See below in `data/`
- `data/`: contains the dataset used for training
  - The transcriptions and audio files are adapted from [this repo](https://github.com/Cosmos-Break/asr)
    - Downsampled to 16kHz for training
    - Currently, only `shh.dict.cn/` is used for training
  - The `*/metadata.txt` files are generated by `make_metadata.py`
- `training/`
  - Juptyer notebook for training the model
  - Intended to be uploaded and run in Google Colab environment; not for local use
  - Uses the `coqui-ai/TTS` repo, which contains an implementation of VITS
- `writeup/`: the write-up
- `speech_synthesis/`: contains the speech synthesis model
  - See [`speech_synthesis/README.md`](speech_synthesis/README.md) for more details
- `comparison_questionnaire`: contains the questionnaire and audio files used to compare speech produced by this model, the Apple model, and a human speaker
  - `*-1.wav`: produced by this model
  - `*-2.wav`: produced by the Apple model (MacBook Pro 14-inch, 2021; MacOS Ventura 13.0.1)
  - `*-3.wav`: spoken by myself
  - `stats.ipynb`: Jupyter notebook for analysing the questionnaire results
