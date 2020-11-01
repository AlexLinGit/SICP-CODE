def make_album(artist, album, tracks=''):
	"""Creates a dictionary of album info."""
	album = {
			'artist': artist, 
			'album': album,
			}
	
	if tracks:
			album['tracks'] = tracks
			
	return album	
	
	
while True:
		
	artist = input("Enter an artist (Press 'q' to quit):  " ) 
	if artist == 'q':
		break
		
	album = input("Enter an album by the artist:  ")
	if album == 'q':
		break
		
	tracks = input("Optional- Enter the # of tracks in the album:  ")
	if tracks == 'q':
		break
	elif tracks == '':
		tracks = ''
			
	final = make_album(artist=artist, album=album, tracks=tracks)
	print(final)
	print("\n")
		
		
		

	

