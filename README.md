# DeoldifyBot
A telegram bot to colorize your old b/w photo using Deoldify (https://github.com/jantic/DeOldify.git)

# Requirements
To run this bot, you need the telepot package:

```python
pip install telepot
```

and the requirements of Deoldify. Here the last version:

https://github.com/jantic/DeOldify/blob/master/requirements.txt

# Usage
To set up your own deoldify bot you have to follow these steps:

1.  Clone the repository: 
```python
  git clone --recurse-submodules https://github.com/AlessandroGianfelici/deoldify_bot.git
```
3.  Download the pretrained weights of Deoldify: https://www.dropbox.com/s/zkehq1uwahhbc2o/ColorizeArtistic_gen.pth
4.  Copy file ColorizeArtistic_gen.pth in the folder Deoldify/models
5.  Create a new telegram bot following the instruction of the botfather https://t.me/botfather
6.  Save your telegram token in the file bot_token.py
7.  Run backend.py
8.  Start sending b/w photo to your bot! Enjoy!
