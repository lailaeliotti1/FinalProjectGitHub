
from playsound import playsound
from jukebox import genre, toggle_jukebox, magic_jukebox, playlist_sources


def main():
    playsound('opening.mp3')
    print("Welcome to Laila's Magic Jukebox! Let's find you some new music that you might be interested in.")
    user_name = input("What is your name?")
    user_genre = input("What's your favorite genre? Enter either Hip-Hop, R&B, Pop, or Country.")
    print(genre(user_genre))
    new_playlist = set()
    new_playlist = toggle_jukebox(user_genre)
    magic_jukebox(new_playlist, user_name)
    playlist_sources(new_playlist)

if __name__ == '__main__':
    main()


