import os
import json
from ytmusicapi import YTMusic
from datetime import datetime

# Function to authenticate with YouTube Music using the headers_auth.json file
def authenticate():
    # Check if the headers_auth.json file exists
    if not os.path.exists("headers_auth.json"):
        print("Please follow the instructions in the ytmusicapi documentation to authenticate.")
        return None

    # Load the headers_auth.json file
    with open("headers_auth.json", "r") as f:
        headers = json.load(f)

    # Create a YTMusic instance with the loaded headers
    ytmusic = YTMusic(headers)
    return ytmusic

# Function to search for an artist by name
def search_artist(artist_name):
    # Authenticate with YouTube Music
    ytmusic = authenticate()
    if ytmusic is None:
        return

    # Search for the artist
    search_results = ytmusic.search(query=artist_name, filter="artists")
    # Find the artist with a matching name
    for result in search_results:
        if result['name'].lower() == artist_name.lower():
            return result['browseId']

    return None

# Function to get the upload date of a track
def get_upload_date(video_id):
    # Authenticate with YouTube Music
    ytmusic = authenticate()
    if ytmusic is None:
        return None

    # Get the video details
    video_details = ytmusic.get_song(video_id)
    # Parse the upload date
    upload_date = datetime.strptime(video_details['uploadDate'], "%b %d, %Y").date()
    return upload_date

# Function to check if a single is also part of an album
def is_single_on_album(single, albums):
    ytmusic = authenticate()
    if ytmusic is None:
        return False

    single_info = ytmusic.get_album(single['browseId'])
    for album in albums:
        album_info = ytmusic.get_album(album['browseId'])
        for track in album_info['tracks']:
            if single_info['tracks'][0]['videoId'] == track['videoId']:
                return True
    return False

# Function to create a playlist of the specified artist's discography
def create_artist_playlist(artist_name):
    # Get the artist's browseId
    artist_id = search_artist(artist_name)
    if artist_id is None:
        print("Artist not found.")
        return

    # Authenticate with YouTube Music
    ytmusic = authenticate()
    if ytmusic is None:
        return

    # Get the artist's albums, singles, EPs, and features
    artist_albums = ytmusic.get_artist_albums(artist_id)['albums']
    artist_singles = ytmusic.get_artist_singles(artist_id)['singles']
    artist_eps = ytmusic.get_artist_eps(artist_id)['eps']
    artist_features = ytmusic.get_artist_albums(artist_id, params={'include_group':'appears_on'})['albums']

    # Remove singles that are also on an album
    artist_singles = [single for single in artist_singles if not is_single_on_album(single, artist_albums)]

    # Combine all the releases
    releases = artist_albums + artist_singles + artist_eps + artist_features

    # Sort the releases by year and upload date
    releases.sort(key=lambda x: (x['year'], get_upload_date(x['browseId'])))

   # Set the playlist name to include the artist's name and "Discography"
playlist_name = f"{artist_name} + Discography"
# Set the playlist description to describe the chronological discography of the artist
playlist_description = f"Chronological discography of {artist_name}, including albums, singles, EPs, and features."
# Create a private playlist with the given name and description, and store the playlist ID
playlist_id = ytmusic.create_playlist(playlist_name, playlist_description, privacy_status='PRIVATE')

# Iterate over the releases in the sorted list of the artist's discography
for release in releases:
    # Get the information for the current release (album, single, EP, or feature)
    release_info = ytmusic.get_album(release['browseId'])
    # Extract the video IDs for each track in the release
    track_ids = [track['videoId'] for track in release_info['tracks']]
    # Add the tracks to the created playlist using the extracted video IDs
    ytmusic.add_playlist_items(playlist_id, track_ids)

# Print a message to indicate the successful creation of the playlist
print(f"Playlist '{playlist_name}' created successfully.")

# Execute the following code block only when this script is run directly (not when imported as a module)
if __name__ == "__main__":
    # Set the artist's name for which you want to create a playlist (replace with the desired artist name)
    artist_name = 'YOUR_ARTIST_NAME'
    # Call the create_artist_playlist function to create a playlist for the specified artist's discography
    create_artist_playlist(artist_name)

