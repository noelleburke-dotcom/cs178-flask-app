-- ----------------------
-- TABLES
-- ----------------------

CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Playlist (
    playlist_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE
);

CREATE TABLE Artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE Song (
    song_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    length_seconds INT,
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);

CREATE TABLE PlaylistSong (
    playlist_id INT,
    song_id INT,
    position INT,
    PRIMARY KEY (playlist_id, song_id),
    FOREIGN KEY (playlist_id) REFERENCES Playlist(playlist_id) ON DELETE CASCADE,
    FOREIGN KEY (song_id) REFERENCES Song(song_id)
);

-- ----------------------
-- DATA
-- ----------------------

-- Users
INSERT INTO User (name) VALUES ('Noelle');

-- Playlist for user_id = 1
INSERT INTO Playlist (user_id) VALUES (1);

-- Artists
INSERT INTO Artist (name) VALUES
('IVE'), ('ITZY'), ('ILLIT'), ('aespa'),
('Stray Kids'), ('NMIXX'), ('KiiKii'), ('Twice');

-- Songs
INSERT INTO Song (title, length_seconds, artist_id)
SELECT 'In Your Heart', 123, artist_id FROM Artist WHERE name='IVE'
UNION ALL
SELECT 'Bang Bang', 178, artist_id FROM Artist WHERE name='IVE'
UNION ALL
SELECT 'I Am', 183, artist_id FROM Artist WHERE name='IVE'
UNION ALL
SELECT 'Wannabe', 191, artist_id FROM Artist WHERE name='ITZY'
UNION ALL
SELECT 'Magnetic', 160, artist_id FROM Artist WHERE name='ILLIT'
UNION ALL
SELECT 'Dirty Work', 180, artist_id FROM Artist WHERE name='aespa'
UNION ALL
SELECT 'Maniac', 182, artist_id FROM Artist WHERE name='Stray Kids'
UNION ALL
SELECT 'Tunnel Vision', 185, artist_id FROM Artist WHERE name='ITZY'
UNION ALL
SELECT 'Blue Valentine', 186, artist_id FROM Artist WHERE name='NMIXX'
UNION ALL
SELECT 'I DO ME', 180, artist_id FROM Artist WHERE name='KiiKii'
UNION ALL
SELECT 'MOUNTAINS', 187, artist_id FROM Artist WHERE name='Stray Kids'
UNION ALL
SELECT 'Easy', 183, artist_id FROM Artist WHERE name='Stray Kids'
UNION ALL
SELECT 'My Pace', 190, artist_id FROM Artist WHERE name='Stray Kids'
UNION ALL
SELECT 'I Can''t Stop Me', 205, artist_id FROM Artist WHERE name='Twice';

-- Link songs to playlist (playlist_id = 1)
INSERT INTO PlaylistSong (playlist_id, song_id, position)
SELECT 1, song_id, 1 FROM Song WHERE title='In Your Heart'
UNION ALL
SELECT 1, song_id, 2 FROM Song WHERE title='Bang Bang'
UNION ALL
SELECT 1, song_id, 3 FROM Song WHERE title='I Am'
UNION ALL
SELECT 1, song_id, 4 FROM Song WHERE title='Wannabe'
UNION ALL
SELECT 1, song_id, 5 FROM Song WHERE title='Magnetic'
UNION ALL
SELECT 1, song_id, 6 FROM Song WHERE title='Dirty Work'
UNION ALL
SELECT 1, song_id, 7 FROM Song WHERE title='Maniac'
UNION ALL
SELECT 1, song_id, 8 FROM Song WHERE title='Tunnel Vision'
UNION ALL
SELECT 1, song_id, 9 FROM Song WHERE title='Blue Valentine'
UNION ALL
SELECT 1, song_id, 10 FROM Song WHERE title='I DO ME'
UNION ALL
SELECT 1, song_id, 11 FROM Song WHERE title='MOUNTAINS'
UNION ALL
SELECT 1, song_id, 12 FROM Song WHERE title='Easy'
UNION ALL
SELECT 1, song_id, 13 FROM Song WHERE title='My Pace'
UNION ALL
SELECT 1, song_id, 14 FROM Song WHERE title='I Can''t Stop Me';