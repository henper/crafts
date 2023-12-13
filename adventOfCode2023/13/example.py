from numpy import array, frombuffer
landscape = [array([
 frombuffer(b'#.##..##.', dtype='S1'),
 frombuffer(b'..#.##.#.', dtype='S1'),
 frombuffer(b'##......#', dtype='S1'),
 frombuffer(b'##......#', dtype='S1'),
 frombuffer(b'..#.##.#.', dtype='S1'),
 frombuffer(b'..##..##.', dtype='S1'),
 frombuffer(b'#.#.##.#.', dtype='S1'),
]), array([
 frombuffer(b'#...##..#', dtype='S1'),
 frombuffer(b'#....#..#', dtype='S1'),
 frombuffer(b'..##..###', dtype='S1'),
 frombuffer(b'#####.##.', dtype='S1'),
 frombuffer(b'#####.##.', dtype='S1'),
 frombuffer(b'..##..###', dtype='S1'),
 frombuffer(b'#....#..#', dtype='S1'),
])]
