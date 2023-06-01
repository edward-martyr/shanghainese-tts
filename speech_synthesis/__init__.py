from TTS.api import TTS

from ..phonemisation import phonemise


def load_model(model_path: str, config_path: str):
    return TTS(model_path=model_path, config_path=config_path)


def tts_to_wav(model: TTS, text: str, file_path: str):
    """
    Here, ``text`` is a phonemised string.
    """
    model.tts_to_file(text=text, file_path=file_path)


def text_to_wav(model: TTS, text: str, file_path: str):
    """
    Here, ``text`` is Shanghainese text in Chinese characters.
    """
    tts_to_wav(model, phonemise(text), file_path)
