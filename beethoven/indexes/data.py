from beethoven.indexes.models import (ChordData, IntervalData, NoteData,
                                      ScaleData)

notes_index_data = [
    NoteData(index=0, semitones=0, alphabetic_name="C", syllabic_name="Do"),
    NoteData(index=1, semitones=2, alphabetic_name="D", syllabic_name="Re"),
    NoteData(index=2, semitones=4, alphabetic_name="E", syllabic_name="Mi"),
    NoteData(index=3, semitones=5, alphabetic_name="F", syllabic_name="Fa"),
    NoteData(index=4, semitones=7, alphabetic_name="G", syllabic_name="Sol"),
    NoteData(index=5, semitones=9, alphabetic_name="A", syllabic_name="La"),
    NoteData(index=6, semitones=11, alphabetic_name="B", syllabic_name="Si"),
]


intervals_index_data = [
    IntervalData(index=0, semitones=0, short_name="1", long_name="unisson"),
    IntervalData(index=1, semitones=2, short_name="2", long_name="second"),
    IntervalData(index=2, semitones=4, short_name="3", long_name="third"),
    IntervalData(index=3, semitones=5, short_name="4", long_name="fourth"),
    IntervalData(index=4, semitones=7, short_name="5", long_name="fifth"),
    IntervalData(index=5, semitones=9, short_name="6", long_name="sixth"),
    IntervalData(index=6, semitones=11, short_name="7", long_name="seventh"),
    IntervalData(index=7, semitones=12, short_name="8", long_name="octave"),
    IntervalData(index=8, semitones=14, short_name="9", long_name="ninth"),
    IntervalData(index=9, semitones=16, short_name="10", long_name="tenth"),
    IntervalData(index=10, semitones=17, short_name="11", long_name="eleventh"),
    IntervalData(index=11, semitones=19, short_name="12", long_name="twelveth"),
    IntervalData(index=12, semitones=21, short_name="13", long_name="thirdteenth"),
    IntervalData(index=13, semitones=23, short_name="14", long_name="fourteenth"),
    IntervalData(index=14, semitones=24, short_name="15", long_name="two octaves"),
]


chords_index_data = [
    ChordData(
        intervals_string="1,5",
        labels=["power"],
        short_name="power",
        full_name="power chord",
        symbol="add5",
    ),
    ChordData(
        intervals_string="1,5d",
        labels=["power"],
        short_name="dim power",
        full_name="diminished power chord",
        symbol="add5d",
    ),
    ChordData(
        intervals_string="1,5a",
        labels=["power"],
        short_name="aug power",
        full_name="augmented power chord",
        symbol="add5a",
    ),
    ChordData(
        intervals_string="1,3,5",
        labels=["triad"],
        short_name="maj",
        full_name="major triad",
        symbol="",
    ),
    ChordData(
        intervals_string="1,3,5d",
        labels=["alt triad"],
        short_name="majb5",
        full_name="major triad (b5)",
        symbol="b5",
    ),
    ChordData(
        intervals_string="1,3m,5",
        labels=["triad"],
        short_name="min",
        full_name="minor triad",
        symbol="-",
    ),
    ChordData(
        intervals_string="1,3,5a",
        labels=["triad"],
        short_name="aug",
        full_name="augmented triad",
        symbol="+",
    ),
    ChordData(
        intervals_string="1,3m,5d",
        labels=["triad"],
        short_name="dim",
        full_name="diminished triad",
        symbol="°",
    ),
    ChordData(
        intervals_string="1,3d,5d",
        labels=["alt triad"],
        short_name="dim dim3",
        full_name="diminished triad diminished 3",
        symbol="°3",
    ),
    ChordData(
        intervals_string="1,2,5",
        labels=["suspended"],
        short_name="sus2",
        full_name="suspended 2",
        symbol="sus2",
    ),
    ChordData(
        intervals_string="1,4,5",
        labels=["suspended"],
        short_name="sus4",
        full_name="suspended 4",
        symbol="sus4",
    ),
    ChordData(
        intervals_string="1,3,5,7",
        labels=["seventh"],
        short_name="maj7",
        full_name="major 7",
        symbol="Δ",
    ),
    ChordData(
        intervals_string="1,3m,5,7m",
        labels=["seventh"],
        short_name="min7",
        full_name="minor 7",
        symbol="-7",
    ),
    ChordData(
        intervals_string="1,3,5,7m",
        labels=["seventh"],
        short_name="7",
        full_name="dominant 7",
        symbol="7",
    ),
    ChordData(
        intervals_string="1,3m,5d,7m",
        labels=["seventh"],
        short_name="min7b5",
        full_name="minor 7 (b5)",
        symbol="ø",
    ),
    ChordData(
        intervals_string="1,3m,5d,7d",
        labels=["seventh"],
        short_name="dim7",
        full_name="diminished 7",
        symbol="°7",
    ),
    ChordData(
        intervals_string="1,3m,5,7",
        labels=["alt seventh"],
        short_name="min maj7",
        full_name="minor major 7",
        symbol="-Δ",
    ),
    ChordData(
        intervals_string="1,3,5a,7",
        labels=["alt seventh"],
        short_name="maj7#5",
        full_name="major 7 (#5)",
        symbol="Δ#5",
    ),
    ChordData(
        intervals_string="1,3,5,6",
        labels=["sixth"],
        short_name="6",
        full_name="major 6",
        symbol="6",
    ),
    ChordData(
        intervals_string="1,3m,5,6",
        labels=["sixth"],
        short_name="min6",
        full_name="minor 6",
        symbol="-6",
    ),
    ChordData(
        intervals_string="1,2,5,7m",
        labels=["suspended"],
        short_name="7sus2",
        full_name="7 suspended 2",
        symbol="7sus2",
    ),
    ChordData(
        intervals_string="1,4,5,7m",
        labels=["suspended"],
        short_name="7sus4",
        full_name="7 suspended 4",
        symbol="7sus4",
    ),
    ChordData(
        intervals_string="1,3d,5d,7d",
        labels=["alt seventh"],
        short_name="min dim7",
        full_name="minor diminished 7",
        symbol="-°7",
    ),
    ChordData(
        intervals_string="1,3m,5,7d",
        labels=["alt seventh"],
        short_name="dim7 dim3",
        full_name="diminished 7 diminished 3",
        symbol="°7°3",
    ),
    ChordData(
        intervals_string="1,3,5d,7",
        labels=["alt seventh"],
        short_name="maj7b5",
        full_name="major 7 (b5)",
        symbol="Δb5",
    ),
    ChordData(
        intervals_string="1,3m,5d,7",
        labels=["alt seventh"],
        short_name="min maj7b5",
        full_name="minor major 7 (b5)",
        symbol="-Δb5",
    ),
    ChordData(
        intervals_string="1,3,5d,7m",
        labels=["alt seventh"],
        short_name="7b5",
        full_name="dominant 7 (b5)",
        symbol="7b5",
    ),
]


scales_index_data = [
    ScaleData(
        intervals_string="1,3m,4,5,7m",
        labels=["pentatonic", "main", "main_non_diatonic"],
        names=["pentatonic minor", "pentatonic"],
    ),
    ScaleData(intervals_string="1,2,3,5,6", labels=["pentatonic"], names=["pentatonic major"]),
    ScaleData(
        intervals_string="1,3m,4,5d,5,7m",
        labels=["pentatonic", "main", "main_non_diatonic"],
        names=["pentatonic blues minor", "blues minor", "blues"],
    ),
    ScaleData(
        intervals_string="1,2,3m,3,5,6",
        labels=["pentatonic"],
        names=["pentatonic blues major", "blues major"],
    ),
    ScaleData(
        intervals_string="1,2,3,4,5,6,7",
        labels=["main", "main_diatonic"],
        names=["major"],
    ),
    ScaleData(
        intervals_string="1,2,3m,4,5,6m,7m",
        labels=["main", "main_diatonic"],
        names=["minor"],
    ),
    ScaleData(intervals_string="1,2,3,4,5,6,7", labels=["major"], names=["ionian"]),
    ScaleData(intervals_string="1,2,3m,4,5,6,7m", labels=["major"], names=["dorian"]),
    ScaleData(intervals_string="1,2m,3m,4,5,6m,7m", labels=["major"], names=["phrygian"]),
    ScaleData(intervals_string="1,2,3,4a,5,6,7", labels=["major"], names=["lydian"]),
    ScaleData(intervals_string="1,2,3,4,5,6,7m", labels=["major"], names=["mixolydian"]),
    ScaleData(
        intervals_string="1,2,3m,4,5,6m,7m",
        labels=["major"],
        names=["aeolian", "natural minor"],
    ),
    ScaleData(intervals_string="1,2m,3m,4,5d,6m,7m", labels=["major"], names=["locrian"]),
    ScaleData(
        intervals_string="1,2,3m,4,5,6,7",
        labels=["melodic minor", "main"],
        names=["melodic minor", "ascending melodic minor"],
    ),
    ScaleData(
        intervals_string="1,2m,3m,4,5,6,7m",
        labels=["melodic minor"],
        names=["phrygian #6", "dorian b2"],
    ),
    ScaleData(
        intervals_string="1,2,3,4a,5a,6,7",
        labels=["melodic minor"],
        names=["lydian augmented"],
    ),
    ScaleData(
        intervals_string="1,2,3,4a,5,6,7m",
        labels=["melodic minor"],
        names=["lydian dominant"],
    ),
    ScaleData(
        intervals_string="1,2,3,4,5,6m,7m",
        labels=["melodic minor"],
        names=["mixolydian b6"],
    ),
    ScaleData(
        intervals_string="1,2,3m,4,5d,6m,7m",
        labels=["melodic minor"],
        names=["half diminished", "half-diminished"],
    ),
    ScaleData(
        intervals_string="1,2m,3m,4d,5d,6m,7m",
        labels=["melodic minor"],
        names=["altered dominant"],
    ),
    ScaleData(
        intervals_string="1,2,3m,4,5,6m,7",
        labels=["harmonic minor", "main"],
        names=["harmonic minor"],
    ),
    ScaleData(
        intervals_string="1,2m,3m,4,5d,6,7m",
        labels=["harmonic minor"],
        names=["locrian #6"],
    ),
    ScaleData(
        intervals_string="1,2,3,4,5a,6,7",
        labels=["harmonic minor"],
        names=["ionian #5"],
    ),
    ScaleData(
        intervals_string="1,2,3m,4a,5,6,7m",
        labels=["harmonic minor"],
        names=["ukrainian dorian"],
    ),
    ScaleData(
        intervals_string="1,2m,3,4,5,6m,7m",
        labels=["harmonic minor"],
        names=["phrygian dominant"],
    ),
    ScaleData(
        intervals_string="1,2a,3,4a,5,6,7",
        labels=["harmonic minor"],
        names=["lydian #2"],
    ),
    ScaleData(
        intervals_string="1,2m,3m,4d,5d,6m,7d",
        labels=["harmonic minor"],
        names=["altered diminished"],
    ),
    ScaleData(
        intervals_string="1,2m,3,4,5,6m,7",
        labels=["double harmonic minor"],
        names=["double harmonic minor"],
    ),
    ScaleData(
        intervals_string="1,2a,3,4a,5,6a,7",
        labels=["double harmonic minor"],
        names=["lydian #2 #6"],
    ),
    ScaleData(
        intervals_string="1,2m,3m,4d,5,6m,7d",
        labels=["double harmonic minor"],
        names=["phrygian bb7 b4"],
    ),
    ScaleData(
        intervals_string="1,2,3m,4a,5,6m,7",
        labels=["double harmonic minor"],
        names=["hungarian minor"],
    ),
    ScaleData(
        intervals_string="1,2m,3,4,5d,6,7m",
        labels=["double harmonic minor"],
        names=["locrian #6 #3", "mixolydian b5 b2"],
    ),
    ScaleData(
        intervals_string="1,2a,3,4,5a,6,7",
        labels=["double harmonic minor"],
        names=["ionian #5 #2"],
    ),
    ScaleData(
        intervals_string="1,2m,3d,4,5d,6m,7d",
        labels=["double harmonic minor"],
        names=["locrian bb3 bb7"],
    ),
    ScaleData(intervals_string="1,2,3,4,5,6,7m,7", labels=["alternative"], names=["bebop"]),
    ScaleData(intervals_string="1,3m,4a,6", labels=["alternative"], names=["diminished"]),
    ScaleData(intervals_string="1,3,6m", labels=["alternative"], names=["augmented"]),
    ScaleData(intervals_string="1,2,3,4a,6m,7m", labels=["alternative"], names=["whole tone"]),
    ScaleData(
        intervals_string="1,2m,2,3m,3,4,5d,5,6m,6,7m,7",
        labels=["alternative"],
        names=["chromatic"],
    ),
]


degrees_index_data = ["i", "ii", "iii", "iv", "v", "vi", "vii"]
