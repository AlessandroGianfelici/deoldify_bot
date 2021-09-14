import sys
import time
import telepot
import os, sys
from bot_token import bot_token
myfolder = os.getcwd()
os.chdir(os.path.join(myfolder, 'DeOldify'))
sys.path.append(os.path.join(myfolder, 'DeOldify'))
from deoldify import device
from deoldify.device_id import DeviceId
#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.CPU)
from deoldify.visualize import *
import warnings


def file_folder_exists(path: str):
    """
    Return True if a file or folder exists.
    :param path: the full path to be checked
    :type path: str
    """
    try:
        os.stat(path)
        return True
    except:
        return False

def select_or_create(path: str):
    """
    Check if a folder exists. If it doesn't, it create the folder.
    :param path: path to be selected
    :type path: str
    """
    if not file_folder_exists(path):
        os.makedirs(path)
    return path


input_path = select_or_create(os.path.join(myfolder, 'input_images'))
render_factor=32

vis = get_image_colorizer(render_factor=render_factor, artistic=True)

def handle(msg):
    chat_id = msg['chat']['id']
    if 'text' in msg.keys():
        bot.sendMessage(chat_id, f"Mandami una foto da colorare!")
    if 'photo' in msg.keys():
        fileid = msg['photo'][-1]['file_id']
        saved_file = os.path.join(input_path, f"{fileid}.png")
        bot.sendMessage(chat_id, f"Grazie! ti manderò la foto colorata appena sarà pronta!")
        bot.download_file(fileid, saved_file)
        result_path = vis.plot_transformed_image(saved_file, render_factor=render_factor, compare=False)
        bot.sendPhoto(chat_id=chat_id, photo=open(os.path.join(myfolder, 'DeOldify', result_path), 'rb'))
    return None

bot = telepot.Bot(bot_token)
bot.message_loop(handle)

while(1):
    time.sleep(1)