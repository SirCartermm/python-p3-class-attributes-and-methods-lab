import song

def test_song():
    # Create some song objects
    song1 = song.Song("99 Problems", "Jay-Z", "Rap")
    song2 = song.Song("Sweet Child O' Mine", "Guns N' Roses", "Rock")
    song3 = song.Song("Country Roads", "John Denver", "Country")
    song4 = song.Song("Lose Yourself", "Eminem", "Rap")
    song5 = song.Song("Hotel California", "Eagles", "Rock")

    # Verify genre count
    print("Genre Count:")
    print(song.Song.genre_count)
    assert song.Song.genre_count == {"Rap": 2, "Rock": 2, "Country": 1}

    # Verify artist count
    print("Artist Count:")
    print(song.Song.artist_count)
    assert song.Song.artist_count == {"Jay-Z": 1, "Guns N' Roses": 1, "John Denver": 1, "Eminem": 1, "Eagles": 1}

    # Verify unique genres and artists
    print("Genres:")
    print(song.Song.genres)
    assert song.Song.genres == ["Rap", "Rock", "Country"]

    print("Artists:")
    print(song.Song.artists)
    assert song.Song.artists == ["Jay-Z", "Guns N' Roses", "John Denver", "Eminem", "Eagles"]

    print("All tests passed!")

if __name__ == "__main__":
    test_song()