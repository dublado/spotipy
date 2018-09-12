# shows tracks for the given artist


import spotipy
import sys
import spotipy.util as util

sp = spotipy.Spotify()
username = "dublado"

token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    artist_name = ' '.join(sys.argv[1:])
    results = sp.search(q=artist_name, limit=20)
    for i, t in enumerate(results['tracks']['items']):
    	print(t['name'], ' ', t['album']['name'],' ', t['id'])
    	exit(1)
    #print(results)
else:
    print("Can't get token for", username)


