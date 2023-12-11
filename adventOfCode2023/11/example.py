from numpy import array, frombuffer
image = array([
 frombuffer(b'...#......', dtype='S1'),
 frombuffer(b'.......#..', dtype='S1'),
 frombuffer(b'#.........', dtype='S1'),
 frombuffer(b'..........', dtype='S1'),
 frombuffer(b'......#...', dtype='S1'),
 frombuffer(b'.#........', dtype='S1'),
 frombuffer(b'.........#', dtype='S1'),
 frombuffer(b'..........', dtype='S1'),
 frombuffer(b'.......#..', dtype='S1'),
 frombuffer(b'#...#.....', dtype='S1'),
])
