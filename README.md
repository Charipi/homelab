# homelab
Code for my Raspberry Pi homelab

## .env Required Fields
VOICE_CLIENT_ACTIVATION=*[Key word that voice recognition uses to send following words in sentence to LLM agent]*  
VOICE_CLIENT_GEMINI_API_KEY  
VOICE_CLIENT_VOSK_MODEL=*[Path to Vosk voice recognition model on main computer. eg: vosk-model-small-en-us-0.15]*  
LIGHT_SERVER_REPO_PATH=*[Path to repository on Raspberry Pi]*  
LIGHT_SERVER_USER=*[Username to ssh into Raspberry Pi]*  
LIGHT_SERVER_HOST=*[Host to ssh into Raspberry Pi]*  

## TODO
- Speak AI output
    - Output to speakers
    - Running ssh commands without speaker pop
- Handle too many request errors (i.e. switch to other model)
- Use systemctl to run client on startup
