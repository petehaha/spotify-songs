from bs4 import BeautifulSoup
import requests
import re
import base64

trackNames = []

# Playlist ID extracting

spotifyUrl = input("Paste the Spotify Url\n")

playlistID = spotifyUrl.split("/playlist/")[1]

# Authorization to retrieve access token

spotifyClientID = "MyClientID"
spotifySecretID = "MySecretID"

headers = {'Authorization': "Basic " + base64.urlsafe_b64encode((spotifyClientID + ":" + spotifySecretID).encode()).decode()}
payload = {'grant_type': 'client_credentials'}

returnedData = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=payload)
print(headers)
print(returnedData.json())

accessToken = returnedData.json().get("access_token")

print(accessToken)

# HTTP Post request to get (only public) playlist
headers = {'Authorization: Bearer': accessToken}

returnedPlaylistData = requests.post("https://api.spotify.com/v1/playlists/" + playlistID + "/tracks", headers=headers)


for i in returnedPlaylistData:
    trackNames.append
    (returnedPlaylistData.json().get("name"))

print(trackNames)
