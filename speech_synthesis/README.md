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
python -m speech_synthesis --model_path /path/to/model --config_path /path/to/config --text "text to synthesise" --output_path /path/to/output.wav
```
