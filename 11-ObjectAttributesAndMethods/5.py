class Songs():
    
    def __init__(self, artist, title, album, year):
        self.artist = artist 
        self.title = title
        self.album = album
        self.year = year
    
    def __str__(self):
        return 'Performer: ' + self.artist + "\n" + 'Song: ' + self.title + '\nAlbum: ' + self.album + '\nYear: ' + self.year +'\n'

    
song1 = Songs('Imagine Dragons', 'Natural','Smoke and Mirrors', '2018')
song2 = Songs('Ed Sheeran', "Hearts Don't Break Around here","divide", '2017')
song3 = Songs('Imagine Dragons', 'Radioactive','Smoke and Mirrors', '2014')
print(song1)
print(song2)  
print(song3)      