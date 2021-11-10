from playsound import playsound
import os

def genre(name):
    '''
    Returns a statement with what genre the user has picked. This will check to make sure the user chose one of
    the four genres.

        Args:
            A string with the user choice of genre.

        Returns:
            A string clarifying the user's choice.

        Examples:
            genre("Hip Hop") --> "You chose Hip-Hop as your favorite genre!"
            genre("Pop") --> "You chose Pop as your favorite genre!"
            genre("K-Pop") --> "Sorry, you must enter Hip-Hop, R & B, Pop, or Country. Try Again!"
    '''

    if name not in "Hip-HopR&BPopCountry":
        return "Sorry, you must enter Hip-Hop, R & B, Pop, or Country. Try Again!"
    else:
        return "You chose {} as your favorite genre!".format(name)


def hip_hop():
    '''Returns a set of Hip Hop music instrumentals.
        Args:
            No arguments

        Returns:
            A set containing hip hop instrumentals

        Examples:
            hip_hop() --> {'hiphop/baby.mp3', 'hiphop/bounce.mp3', 'hiphop/cele.mp3', 'hiphop/epic.mp3',
                    'hiphop/fallout.mp3', 'hiphop/mepa.mp3', 'hiphop/mystuff.mp3', 'hiphop/nasty.mp3',
                    'hiphop/persian.mp3', 'hiphop/workout.mp3'}
    '''
    files = os.listdir("hiphop")
    files = [file for file in files if file[-4:] == '.mp3']
    for i in range(len(files)):
        files[i] = os.path.join("hiphop", files[i])
    hip_playlist = set(files)
    return hip_playlist


def r_n_b():
    '''Returns a set of R & B music instrumentals.
        Args:
            No arguments

        Returns:
            A set containing R & B instrumentals

        Examples:
            r_n_b() --> {'r&b/city.mp3', 'r&b/coffee.mp3', 'r&b/glitch.mp3', 'r&b/love.mp3', 'r&b/milan.mp3', 'r&b/need.mp3',
                'r&b/proud.mp3', 'r&b/pyrosion.mp3', 'r&b/smooth.mp3', 'r&b/surface.mp3'}
    '''
    files = os.listdir("r&b")
    files = [file for file in files if file[-4:] == '.mp3']
    for i in range(len(files)):
        files[i] = os.path.join("r&b", files[i])
    rnb_playlist = set(files)
    return rnb_playlist


def music_pop():
    '''Returns a set of Pop music instrumentals.
            Args:
                No arguments

            Returns:
                A set containing Pop instrumentals

            Examples:
                music_pop() --> {{'pop/aura.mp3', 'pop/ecto.mp3', 'pop/funky.mp3', 'pop/chill.mp3', 'pop/future.mp3',
                'pop/lounge.mp3' , 'pop/popsicl.mp3', 'pop/pos.mp3', 'pop/design.mp3', 'pop/upbeat.mp3'}
    '''
    files = os.listdir("pop")
    files = [file for file in files if file[-4:] == '.mp3']
    for i in range(len(files)):
        files[i] = os.path.join("pop", files[i])
    pop_playlist = set(files)
    return pop_playlist


def country():
    '''Returns a set of Country music instruentals.
            Args:
                No arguments

            Returns:
                A set containing R & B instrumentals

            Examples:
                r_n_b() --> {'r&b/city.mp3', 'r&b/coffee.mp3', 'r&b/glitch.mp3', 'r&b/love.mp3', 'r&b/milan.mp3', 'r&b/need.mp3',
                    'r&b/proud.mp3', 'r&b/pyrosion.mp3', 'r&b/smooth.mp3', 'r&b/surface.mp3'}
    '''
    files = os.listdir("country")
    files = [file for file in files if file[-4:] == '.mp3']
    for i in range(len(files)):
        files[i] = os.path.join("country", files[i])
    country_playlist = set(files)
    return country_playlist

def length(playlist):
    '''Returns a playlist set with the user's given length
            Args:
                A set containing instrumentals.

            Returns:
                A playlist that is the user's requested length.

            Examples:
                num_of_songs = 5 -->len(playlist) = 5
    '''
    answer = "no"
    while answer == "no":
        num_of_songs = int(input("How many songs would you like in the playlist?"))
        if num_of_songs == 0:
            print("The length cannot be zero songs.")
        else:
            print("The maximum length for your playlist is {} songs.".format(len(playlist)))
            answer = input("So you want a playlist of {} songs? Press enter to continue or type no. ".format(num_of_songs))
    print("You have chosen a playlist of {} songs.".format(num_of_songs))
    num_of_songs = len(playlist) - num_of_songs
    while num_of_songs > 0:
        playlist.pop()
        num_of_songs -= 1
    return playlist

def waiting():
    '''Returns nothing. Acts as a countdown for the playlist.
            Args:
                No arguments

            Returns:
                No returns

            Examples:
                waiting() --> "In\n3...\n2...\n1...\nPlay!"

    '''
    print("In\n3...\n2...\n1...\nPlay!")


def toggle_jukebox(user_genre):
    '''Returns nothing. Acts as a countdown for the playlist.
            Args:
                No arguments

            Returns:
                No returns

            Examples:
                waiting() --> "In\n3...\n2...\n1...\nPlay!"

    '''
    global new_playlist
    if user_genre == "Hip-Hop":
        new_playlist = hip_hop()
        new_playlist = length(new_playlist)
        waiting()
    elif user_genre == "R&B":
        new_playlist = r_n_b()
        new_playlist = length(new_playlist)
        waiting()
    elif user_genre == "Pop":
        new_playlist = music_pop()
        new_playlist = length(new_playlist)
        waiting()
    elif user_genre == "Country":
        new_playlist = country()
        new_playlist = length(new_playlist)
        waiting()
    return new_playlist

def playlist_sources(playlist):
    '''Returns nothing. Prints the sources of the playlist if the playlist is not empty.
            Args:
                A set of song (playlist)

            Returns:
                No returns

            Examples:
                len(playlist) == 0 --> ""
                len(playlist) > 0 --> "Royalty free music credited to: Music by Joystock - https://www.joystock.org, https://www.pixabay.com/music/, "
            "https://www.free-stock-music.com"

    '''
    if len(new_playlist) == 0:
        pass
    else:
        print("Enjoy your new shuffled playlist!")
        print("Royalty free music credited to: Music by Joystock - https://www.joystock.org, "
              "https://www.pixabay.com/music/, ""https://www.free-stock-music.com")

def magic_jukebox(music, name):
    '''Returns nothing. Plays the playlist.
            Args:
                A set of songs

            Returns:
                No returns

            Examples:
                playsound(song)
    '''
    print("{}'s NEW PLAYLIST".format(name.upper()))
    print("*******************")
    for track_number, song in enumerate(music):
        print(track_number + 1, song)
        playsound(song)
    print("*******************")
