note_mappings = [
    (0, 0,  "C", "Do"),
    (1, 2,  "D", "Re"),
    (2, 4,  "E", "Mi"),
    (3, 5,  "F", "Fa"),
    (4, 7,  "G", "Sol"),
    (5, 9,  "A", "La"),
    (6, 11, "B", "Si")
]


interval_mappings = [
    (0,  0,  "1",  "unisson"),
    (1,  2,  "2",  "second"),
    (2,  4,  "3",  "third"),
    (3,  5,  "4",  "fourth"),
    (4,  7,  "5",  "fifth"),
    (5,  9,  "6",  "sixth"),
    (6,  11, "7",  "seventh"),
    (7,  12, "8",  "octave"),
    (8,  14, "9",  "ninth"),
    (9,  16, "10", "tenth"),
    (10, 17, "11", "eleventh"),
    (11, 19, "12", "twelveth"),
    (12, 21, "13", "thirdteenth"),
    (13, 23, "14", "fourteenth"),
    (14, 24, "15", "two octaves")
]


chord_mappings = [
    ('1,5',        'power',      'power chord',                   'add5'),
    ('1,5d',       'dim power',  'diminished power chord',        'add5d'),
    ('1,5a',       'aug power',  'augmented power chord',         'add5a'),
    ('1,3,5',      'maj',        'major triad',                   ''),
    ('1,3,5d',     'majb5',      'major triad (b5)',              'b5'),
    ('1,3m,5',     'min',        'minor triad',                   '-'),
    ('1,3,5a',     'aug',        'augmented triad',               '+'),
    ('1,3m,5d',    'dim',        'diminished triad',              '°'),
    ('1,3d,5d',    'dim dim3',   'diminished triad diminished 3', '°3'),
    ('1,2,5',      'sus2',       'suspended 2',                   'sus2'),
    ('1,4,5',      'sus4',       'suspended 4',                   'sus4'),
    ('1,3,5,7',    'maj7',       'major 7',                       'Δ'),
    ('1,3m,5,7m',  'min7',       'minor 7',                       '-7'),
    ('1,3,5,7m',   '7',          'dominant 7',                    '7'),
    ('1,3m,5d,7m', 'min7b5',     'minor 7 (b5)',                  'ø'),
    ('1,3m,5d,7d', 'dim7',       'diminished 7',                  '°7'),
    ('1,3m,5,7',   'min maj7',   'minor major 7',                 '-Δ'),
    ('1,3,5a,7',   'maj7#5',     'major 7 (#5)',                  'Δ#5'),
    ('1,3,5,6',    '6',          'major 6',                       '6'),
    ('1,3m,5,6',   'min 6',      'minor 6',                       '-6'),
    ('1,2,5,7m',   '7sus2',      '7 suspended 2',                 '7sus2'),
    ('1,4,5,7m',   '7sus4',      '7 suspended 4',                 '7sus4'),
    ('1,3d,5d,7d', 'min dim7',   'minor diminished 7',            '-°7'),
    ('1,3m,5,7d',  'dim7 dim3',  'diminished 7 diminished 3',     '°7°3'),
    ('1,3,5d,7',   'maj7b5',     'major 7 (b5)',                  'Δb5'),
    ('1,3m,5d,7',  'min maj7b5', 'minor major 7 (b5)',            '-Δb5'),
    ('1,3,5d,7m',  '7b5',        'dominant 7 (b5)',               '7b5')
]


scale_mappings = [
    ("1,3m,4,5,7m",                  "",                      "pentatonic minor", "pentatonic"),
    ("1,2,3,5,6",                    "",                      "pentatonic major"),
    ("1,3m,4,5d,5,7m",               "",                      "pentatonic blues minor", "blues minor", "blues"),
    ("1,2,3m,3,5,6",                 "",                      "pentatonic blues major", "blues major"),
    ("1,2,3,4,5,6,7",                "major",                 "ionian", "major"),
    ("1,2,3m,4,5,6,7m",              "major",                 "dorian"),
    ("1,2m,3m,4,5,6m,7m",            "major",                 "phrygian"),
    ("1,2,3,4a,5,6,7",               "major",                 "lydian"),
    ("1,2,3,4,5,6,7m",               "major",                 "mixolydian"),
    ("1,2,3m,4,5,6m,7m",             "major",                 "aeolian", "natural minor", "minor"),
    ("1,2m,3m,4,5d,6m,7m",           "major",                 "locrian"),
    ("1,2,3m,4,5,6,7",               "melodic minor",         "melodic minor", "ascending melodic minor"),
    ("1,2m,3m,4,5,6,7m",             "melodic minor",         "phrygian #6", "dorian b2"),
    ("1,2,3,4a,5a,6,7",              "melodic minor",         "lydian augmented"),
    ("1,2,3,4a,5,6,7m",              "melodic minor",         "lydian dominant"),
    ("1,2,3,4,5,6m,7m",              "melodic minor",         "mixolydian b6"),
    ("1,2,3m,4,5d,6m,7m",            "melodic minor",         "half diminished", "half-diminished"),
    ("1,2m,3m,4d,5d,6m,7m",          "melodic minor",         "altered dominant"),
    ("1,2,3m,4,5,6m,7",              "harmonic minor",        "harmonic minor"),
    ("1,2m,3m,4,5d,6,7m",            "harmonic minor",        "locrian #6"),
    ("1,2,3,4,5a,6,7",               "harmonic minor",        "ionian #5"),
    ("1,2,3m,4a,5,6,7m",             "harmonic minor",        "ukrainian dorian"),
    ("1,2m,3,4,5,6m,7m",             "harmonic minor",        "phrygian dominant"),
    ("1,2a,3,4a,5,6,7",              "harmonic minor",        "lydian #2"),
    ("1,2m,3m,4d,5d,6m,7d",          "harmonic minor",        "altered diminished"),
    ("1,2m,3,4,5,6m,7",              "double harmonic minor", "double harmonic minor"),
    ("1,2a,3,4a,5,6a,7",             "double harmonic minor", "lydian #2 #6"),
    ("1,2m,3m,4d,5,6m,7d",           "double harmonic minor", "phrygian bb7 b4"),
    ("1,2,3m,4a,5,6m,7",             "double harmonic minor", "hungarian minor"),
    ("1,2m,3,4,5d,6,7m",             "double harmonic minor", "locrian #6 #3", "mixolydian b5 b2"),
    ("1,2a,3,4,5a,6,7",              "double harmonic minor", "ionian #5 #2"),
    ("1,2m,3d,4,5d,6m,7d",           "double harmonic minor", "locrian bb3 bb7"),
    ("1,2,3,4,5,6,7m,7",             "",                      "bebop"),
    ("1,3m,4a,6",                    "",                      "diminished"),
    ("1,3,6m",                       "",                      "augmented"),
    ("1,2,3,4a,6m,7m",               "",                      "whole tone"),
    ("1,2m,2,3m,3,4,5d,5,6m,6,7m,7", "",                      "chromatic")
]


degree_mappings = ["i", "ii", "iii", "iv", "v", "vi", "vii"]