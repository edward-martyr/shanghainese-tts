# Shanghainese Speech Synthesis

In order to synthesise speech, you need a model and a configuration file.
Please find the sample model and config files here

- <https://drive.google.com/file/d/109VOkplX4hOoPc1_9BbCilIUbeHspbqh/view?usp=sharing>
- <https://drive.google.com/file/d/1-KNdDuuDbeITqLrjfD0NQHs7yiCJQYIn/view?usp=sharing>

## Usage

### Python API

```python
from speech_synthesis import load_model, text_to_wav
model = load_model("path/to/model.pth", "path/to/config.json")
text_to_wav(model, "儂好，世界", "output.wav")
```

### CLI

```bash
python -m speech_synthesis [-h] [-r] -m MODEL_PATH -c CONFIG_PATH -t TEXT -o OUTPUT_PATH

options:
  -h, --help            show this help message and exit
  -r, --romanisation    whether to romanise the input text
  -m MODEL_PATH, --model_path MODEL_PATH
                        path to model.pth
  -c CONFIG_PATH, --config_path CONFIG_PATH
                        path to config.json
  -t TEXT, --text TEXT  text to synthesise
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        path to output WAV file
```
