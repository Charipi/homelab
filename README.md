# homelab
Code for my Raspberry Pi homelab

## .env Required Fields
ACTIVATION=*[Key word that voice recognition uses to send successive words in sentence to Gemini]*  
GEMINI_API_KEY  
RASPI_PATH=*[Path to repository on Raspberry Pi]*  
RASPI_USER=*[Username to ssh into Raspberry Pi]*  
RASPI_HOST=*[Host to ssh into Raspberry Pi]*  
VOSK_MODEL=*[Path to Vosk voice recognition model on main computer. eg: vosk-model-small-en-us-0.15]*  

## TODO
- Speak AI output
    - Output to speakers
    - Running ssh commands without speaker pop
- Handle too many request errors (i.e. switch to other model)
- Set to run automatically on startup
- Silence the output of pyaudio
