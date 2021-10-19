from yandex_music import Client
import os

yandexClient = Client.from_credentials('m4xim28@yandex.ru', 'zmalqp10')

def get_track_url(url: str):
   print(url) 
   album_track = url.split("https://music.yandex.ru/album/")[1].split("/track/")
   album_track_path = album_track[1] + "_" + album_track[0]
   album_track = album_track[1] + ":" + album_track[0]
   
   print(album_track)

   track = yandexClient.tracks([album_track])[0]
   track.download(f"./temp/{album_track_path}.mp3")
   url = track.download_info[0].direct_link
   os.remove(f"./temp/{album_track_path}.mp3")
   return url

