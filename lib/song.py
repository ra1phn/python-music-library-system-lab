class Song:
    """
    Represents a single song and maintains class-level (shared) data
    about every Song instance ever created.
    """

    # ---------- Class Attributes ----------
    count = 0            # total number of Song objects created
    genres = []          # list of unique genres across all songs
    artists = []         # list of unique artists across all songs
    genre_count = {}     # e.g. {"Rap": 5, "Rock": 1, "Country": 3}
    artist_count = {}    # e.g. {"Beyonce": 17, "Jay-Z": 40}

    def __init__(self, name, artist, genre):
        # ---------- Instance Attributes ----------
        self.name = name
        self.artist = artist
        self.genre = genre

        # Every time a new Song is created, update all class-level stats.
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    # ---------- Class Methods ----------

    @classmethod
    def add_song_to_count(cls):
        """Increment the total song count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a new genre to the shared genres list, no duplicates."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add a new artist to the shared artists list, no duplicates."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment this genre's tally; start at 1 if not tracked yet."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Increment this artist's tally; start at 1 if not tracked yet."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    def __repr__(self):
        return f"<Song name={self.name!r} artist={self.artist!r} genre={self.genre!r}>"
    