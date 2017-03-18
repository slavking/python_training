'''
You are creating a song playlist for your next party.
You have a collection of songs that can be represented as a list of tuples.
Each tuple has the following elements:

    name: the first element, representing the song name (non-empty string)
    song_length: the second, element representing the song duration (float >= 0)
    song_size: the third, element representing the size on disk (float >= 0)

You want to try to optimize your playlist to play songs for as long as possible
while making sure that the songs you pick do not take up more than a
given amount of space on disk (the sizes should be less than or equal to
                               the max_disk_size).

You decide the best way to achieve your goal is to start with the first song
in the given song list. If the first song doesn't fit on disk,
return an empty list.

If there is enough space for this song, add it to the playlist.

For subsequent songs, you choose the next song such that its size on disk
is smallest and that the song hasn't already been chosen.
You do this until you cannot fit any more songs on the disk.

Write a function implementing this algorithm,
that returns a list of the song names in the order in which they were chosen,
with the first element in the list being the song chosen first.
Assume song names are unique and all the songs have different sizes on disk
and different durations.

You may not mutate any of the arguments.

For example,

    If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 12.2, the function will return ['Roar','Wannabe','Timber']
    If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 11, the function will return ['Roar','Wannabe']

    pohlepan algoritam za hvatanje imena pesama
    po kriterijumu najmanje pesme sve dok nije
    ispunjen max_size, tj. max_disk_size
    prima listu tuplova gore navedenog oblika
'''
def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """

    import operator
    #alternativa key=lambda x:x[2]
    sortedvals = sorted(songs,key=operator.itemgetter(2))
    vals=songs.copy()

    #for x in vals:
    #   print(x)
    totalCost=0
    
    i=0
    L=[]
    if len(vals) == 1:
        if vals[0][2] < max_size:
            return vals 
    elif len(vals)>=2:
        if vals[0][2]<max_size:
            L.append(vals[0])
            totalCost+=vals[0][2]
            I=vals.pop(0)
            sortedvals.remove(I)
        else:
            return [] #ako prva nije korektna, vrati praznu listu
        #print('vals '+str(vals))
        #print('sortedvals '+str(sortedvals))
        #print('L' +str(L))
        while len(sortedvals)>0 and totalCost<max_size and \
        sortedvals[0][2]<max_size and sortedvals[0][2]+totalCost < max_size:
            totalCost+=sortedvals[0][2]
            #print('sortedvals u petlji '+str(sortedvals))
            L.append(sortedvals[0])
            #print('L u petlji '+str(L))
            sortedvals.pop(0)
            #print('totalCost u petlji '+str(totalCost))
    #print(totalCost)
    D=[]            
    if L==[]:
        return L
    else:
        for x in L:
            D.append(x[0])
    return D

song1=[('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]

print(song_playlist(song1,12.2))
print(song_playlist(song1,11))
print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 20))  #ok
print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 12.2)) #ok        
print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 11))#ok
print(song_playlist([('a', 4.0, 4.4), ('b', 7.7, 3.5), ('c', 6.9, 5.1), ('d', 1.2, 2.7)], 20))#ok        
print(song_playlist([('aa', 4, 4), ('bb', 5, 7), ('cc', 5, 6), ('dd', 2, 1)], 1)) #not ok!
print(song_playlist([('aa', 4, 4), ('bb', 5, 7), ('cc', 5, 6), ('dd', 2, 1)], 3))
