# python-transformer-chatbots

Huggingface makes it easy to build your own basic chatbot based on pretrained transformer models. In this project you can find a handful of examples to play around with. 

## Installation

Install via pip:

```
pip install git+github.com/butyr/python-transformer-chatbot.git
```

## Usage
To have a quick chat with one of the bots, simply run the following lines of code. The first run might take a while since the models need to be downloaded.

```python
from chatbots import BlenderBot


bot = BlenderBot()
bot.run()
```

```python
from chatbots import DialoGPT


bot = DialoGPT()
bot.run()
```
