# -*- coding: utf-8 -*-

import requests
import telegram
import auxiliar # Crear un auxiliar.py con las constantes de tkn=TOKEN_DEL_BOT

# tkn = 'Token'
bot = telegram.Bot(auxiliar.tkn)

def get_users():
    """
    Devuelvo una lista con todos los usuarios registrados
    
    *No implementado
    """
    users=[auxiliar.chat_id]
    return users

def send_vid():
    """
    Envío el video a todos los usuarios registrados
    """
    
    # chat_id = 'chat_id'
    
    video = 'https://r3---sn-5go7ynez.googlevideo.com/videoplayback?expire=1599903660&ei=TENcX46GI4iogAes8JaAAw&ip=37.99.251.44&id=o-AGPVf5uZmiDFJR1k9XxCXxPnCxXRuboC8ikVFlr3yZJW&itag=18&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&gir=yes&clen=219222&ratebypass=yes&dur=7.082&lmt=1591490265672021&fvip=3&c=WEB&txp=6201222&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAI5lHQqdWAawrFyqNVERZI_DTiKSpIFpRcmnGLnMB9YgAiEAqEeaIKy4Jh_G0MrRn_RAU0QkEbKvA0UhvfvC7oy_nIg%3D&video_id=WqN1wnf9zdo&title=Feliz+Jueves+%28Kun+Ag%C3%BCero%29&redirect_counter=1&rm=sn-hpa6s7s&req_id=8b7794bb3affa3ee&cms_redirect=yes&ipbypass=yes&mh=1Z&mip=190.191.113.234&mm=31&mn=sn-5go7ynez&ms=au&mt=1599883536&mv=u&mvi=3&pl=19&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgH5sEOz2cUF-Y8TdXq0CF9jGUpp9W_7hw-fcXW1END58CIQD2u_Ie88tnAxCgEpV4PI7U7r8dOsnEBdCT1Q_Tmit68Q%3D%3D'
    
    for chat_id in get_users():
        bot.send_video(chat_id,video)
    
if __name__ == '__main__':
    send_vid()