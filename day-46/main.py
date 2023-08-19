import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from bs4 import BeautifulSoup

input_p = input("input date YYYY-MM-DD: ")


URL = f"https://www.billboard.com/charts/hot-100/{input_p}/"

response = requests.get(url=URL)
page = response.text
soup = BeautifulSoup(page, "html.parser")
songs = [n.get_text().strip() for n in soup.select('li ul li h3')]
# names = [n.get_text().strip() for n in soup.select('li ul li span')]
# print(names)

# user ID - https://open.spotify.com/user/31mdypxrldrsdelisz3veang72ju?si=004111a5363b4d25

SPOTIPY_CLIENT_ID = '7c6e030bf59b4157b6336e77059de802'
SPOTIPY_CLIENT_SECRET = 'd3050560eef144578fd1c6448c1d3833'
SPOTIPY_REDIRECT_URI = 'https://www.billboard.com/charts/hot-100'


import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username='Redeks', 
    )
)
song_ids = []

for sng in songs:

    res = sp.search(q=f'track:{sng}', type='track', limit=1)

    try:
        track_id = res['tracks']['items'][0]['id']
        song_ids.append(f'spotify:track:{track_id}')
    except IndexError:
       continue

playlist_name = f'{input_p} Billboard 100'
playlist_description = 'This is my new private playlist created with Python.'

user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description=playlist_description)
playlist_id = playlist['id']
created = sp.user_playlist_add_tracks(sp.current_user()['id'], playlist_id, song_ids)
       
       
print(created)
# uri = 'spotify:track:6rqhFgbbKwnb9MLmUQDhG6'


# artist = sp.track(uri)
# print(artist)

# user = sp.user('plamere')
# print(user)

