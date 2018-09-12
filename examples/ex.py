# shows tracks for the given artist


import pprint
import sys

import spotipy
import spotipy.util as util

sp = spotipy.Spotify()
username = "dublado"
playlist_id = "4oxcScbIPXLC5ZQZK0vLww"


musicas="""cinema mudo Cinema Mudo Paralamas 
o senhor da guerra LEGIÃO URBANA"""
splitmusica=musicas.split("\n")

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)

inter=1

for x in splitmusica:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    artist_name = x
    results = sp.search(q=artist_name, limit=20)
    for i, t in enumerate(results['tracks']['items']):
    	#print(t['name'], ' ', t['album']['name'],' ', t['id'])
    	print(str(inter)+" " + t['artists'][0]['name'] + ' ' +t['name'] + ' ' +  t['album']['name'] +  ' ' +  t['id'])
    	inter+=1
    	sp.user_playlist_add_tracks(username, playlist_id, {t['id']})
    	#exit(1)
    	break
   	
	#print(x)