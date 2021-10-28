class Song:
    def __init__(self, songs):
        self.songs = [
            {
                "title": [],
                "artist": []
            }
        ]
    
    def create_song(self, title, artist):
        self.songs["title"].append(title)
        self.songs["artist"].append(artist)
        return self.songs
