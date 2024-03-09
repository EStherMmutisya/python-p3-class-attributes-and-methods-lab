
class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = set()
    artists = set()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        
        Song.count += 1
        self._update_counts()

    def _update_counts(self):
        
        Song.genres.add(self.genre)
        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1


        Song.artists.add(self.artist)
        Song.artist_count[self.artist] = Song.artist_count.get(self.artist, 0) + 1


def create_song(name, artist, genre):
    return Song(name, artist, genre)


song1 = create_song("99 Problems", "Jay Z", "Rap")
song2 = create_song("Halo", "Beyonce", "Pop")
song3 = create_song("Smells Like Teen Spirit", "Nirvana", "Rock")


print("Total Song Count:", Song.count)
print("Genre Count:", Song.genre_count)
print("Artist Count:", Song.artist_count)

