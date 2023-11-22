# localpilot
_Use GitHub Copilot locally on your Macbook with one-click!_

![image](https://github.com/danielgross/localpilot/assets/279531/521d0613-7423-4839-a5e8-42098cd65a5e)

## Demo Video


https://github.com/danielgross/localpilot/assets/279531/3259981b-39f7-4bfa-8a45-84bde6d4ba4c



_This video is not sped up or slowed down._

## Installation 
1. First, open VS Code Settings and add the following to your settings.json file: 
```json
"github.copilot.advanced": {
    "debug.testOverrideProxyUrl": "http://localhost:5001",
    "debug.overrideProxyUrl": "http://localhost:5001"
}
```

2. Create a virtualenv to run this Python process, install the requirements, and download the models. 
```python
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
# First setup run. This will download several models to your ~/models folder.
python app.py --setup 
``` 

3. Run it! 
```python
python app.py
```

Enjoy your on-device Copilot! 

## Caveat FAQ

**Is the code as good as GitHub Copilot?** 

For simple line completions yes. For simple function completions, mostly. For complex functions... maybe. 

**Is it as fast as GitHub Copilot?**

On my Macbook Pro with an Apple M2 Max, the 7b models are roughly as fast. The 34b models are not. Please consider this repo a demonstration of a very inefficient implementation. I'm sure we can make it faster; please do submit a pull request if you'd like to help. For example, I think we need debouncer because sometimes llama.cpp/GGML isn't fast at interrupting itself when a newer request comes in.

**Can this be packaged as a simple Mac app?**

Yes!, I'm sure it can be, I just haven't had the time. Please do submit a pull request if you're into that sort of thing!

**Should there be a meta-model that routes to a 1b for autocomplete, 7b for more complex autocomplete, and a 34b for program completion?**

Hmm, that seems like an interesting idea.

**OK, but in summary, is it good?** 

Only if your network is bad. I don't think it's competitive if you have fast Internet. But it sure is awesome on airplanes and while tethering!


