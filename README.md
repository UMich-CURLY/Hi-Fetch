# Hi-Fetch
A NLP-based communication module for fetch bot :D.
## Setup:
### Installations:

```git clone https://github.com/erikziyunchi/Hi-Fetch.git```

```cd Hi-Fetch```

```python -m venv venv```

```source /venv/bin/activate```

If you are a Mac user:
1. ```brew install portaudio```

2. ```pip install --global-option='build_ext' --global-option="-I$(brew --prefix)/include" --global-option="-L$(brew --prefix)/lib" pyaudio```

Otherwise:
```pip install -r requirements.txt```

#### Access keys: (Has filled in in this repo)
1. AudioManager.py: line 23: pvporcupine.create(access_key=“YOUR_ACCESS_KEY”, keywords=["hi fetch"]) <- obtain from https://console.picovoice.ai/
2. Put your GPT-3 OpenAI access Key into “OpenAIKey.txt”

```python run.py```