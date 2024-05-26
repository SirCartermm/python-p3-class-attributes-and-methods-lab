import pytest
from song import Song

@pytest.fixture
def song_obj():
    return Song("Test Song", "Test Artist", "Test Genre")

@pytest.fixture
def multiple_songs():
    songs = []
    for i in range(5):
        songs.append(Song(f"Song {i}", f"Artist {i}", f"Genre {i % 2}"))
    return songs

@pytest.fixture
def song_class():
    return Song