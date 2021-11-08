# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from playsound import playsound
from functions import genre, hip_hop, r_n_b, music_pop, toggle_jukebox, jukebox, playlist_sources
#from gtts import gTTS
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    playsound('opening.mp3')
    print("Welcome to Laila's Magic Jukebox! Let's find you some new music that you might be interested in.")
    user_genre = input("What's your favorite genre? Enter either Hip-Hop, R&B, Pop, or Country.")
    print(genre(user_genre))
    new_playlist = {}
    new_playlist = toggle_jukebox(user_genre)
    playlist_sources(new_playlist)

    # song_file = 'hip-hop/cele.mp3'
    # print(os.path.abspath(song_file))
    # print(os.listdir(PycharmProjects/MyProject))
    # playsound(song_file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
