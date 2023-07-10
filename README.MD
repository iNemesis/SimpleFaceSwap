# Simple face swap

## prerequisite

1. download `inswapper_128.onnx` and put it in `./lib`
   1. [drive download link](https://drive.google.com/file/d/1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF/view)
   2. [huggingface download link](https://huggingface.co/deepinsight/inswapper/blob/main/inswapper_128.onnx)

## how to use

there is a command-line app and a _ugly_ GUI app

### command-line app

`python ./main.py image_to_swap image_with_face`

### GUI

`python gui/main.py`

---

Project created thanks to [insightface](https://github.com/deepinsight/insightface)