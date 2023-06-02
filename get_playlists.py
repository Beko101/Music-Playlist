import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_playlists', methods=['POST'])
def get_playlists():
    music_service = request.form['music_service']
    access_token = request.form['access_token']

    playlists = []
    if music_service == 'spotify':
        playlists = get_spotify_playlists(access_token)
    elif music_service == 'apple_music':
        playlists = get_apple_music_playlists(access_token)
    elif music_service == 'amazon_music':
        playlists = get_amazon_music_playlists(access_token)
    elif music_service == 'deezer':
        playlists = get_deezer_playlists(access_token)

    if playlists:
        return jsonify(playlists=playlists)
    else:
        return jsonify(error='Failed to get playlists.')

def get_spotify_playlists(access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }

    response = requests.get('https://api.spotify.com/v1/me/playlists', headers=headers)
    
    if response.status_code == 200:
        playlists_data = response.json()
        playlists = [playlist['name'] for playlist in playlists_data['items']]
        return playlists
    else:
        return None

def get_apple_music_playlists(access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }

    response = requests.get('https://api.music.apple.com/v1/me/library/playlists', headers=headers)

    if response.status_code == 200:
        playlists_data = response.json()
        playlists = [playlist['attributes']['name'] for playlist in playlists_data['data']]
        return playlists
    else:
        return None

def get_amazon_music_playlists(access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }

    response = requests.get('https://api.amazon.com/user/playlists', headers=headers)

    if response.status_code == 200:
        playlists_data = response.json()
        playlists = [playlist['title'] for playlist in playlists_data['playlists']]
        return playlists
    else:
        return None

def get_deezer_playlists(access_token):
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }

    response = requests.get('https://api.deezer.com/user/me/playlists', headers=headers)

    if response.status_code == 200:
        playlists_data = response.json()
        playlists = [playlist['title'] for playlist in playlists_data['data']]
        return playlists
    else:
        return None

if __name__ == '__main__':
    app.run()
