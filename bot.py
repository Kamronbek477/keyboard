import os
import requests

TOKEN = '5943315985:AAGzM6GHlv6wcm38nzy50KB9DKyi7QLqgag'



def sendMessage(chat_id:str, text:str):
    button1 = {'text':'lacetti'}
    button2 = {'text':'cobalt'}
    button3 = {'text':'epica'}

    keyboard = [[button1, button2],[button3]]

    reply_markup = {'keyboard':keyboard}

    payload = {
        'chat_id':chat_id,
        'text':text,
        'reply_markup':reply_markup
    }
   
  
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    
    response = requests.post(url=URL, json=payload)
    return response.json()

    

chat_id = 1993623102
text = 'Hello'
print(sendMessage(chat_id, text))