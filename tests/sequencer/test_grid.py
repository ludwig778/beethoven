from beethoven.sequencer.grid import Grid, GridPart
from beethoven.sequencer.note_duration import Half, Whole
from beethoven.sequencer.tempo import Tempo
from beethoven.sequencer.time_signature import TimeSignature
from beethoven.theory.chord import Chord
from beethoven.theory.scale import Scale


def test_create_empty_grid():
    grid = Grid()

    assert grid.parts == []


def test_create_grid_with_parts():
    time_signature = TimeSignature(4, 4)
    tempo = Tempo(90)

    grid = Grid([
        GridPart(
            scale=Scale("A", "major"),
            chord=Chord("A", "maj"),
            tempo=Tempo(90),
            duration=Whole,
            time_signature=TimeSignature(4, 4)
        ),
        GridPart(
            scale=Scale("A", "major"),
            chord=Chord("A", "min"),
            tempo=Tempo(120),
            duration=Whole,
            time_signature=TimeSignature(4, 4)
        ),
        GridPart(
            scale=Scale("A", "major"),
            chord=Chord("A", "maj"),
            tempo=Tempo(120),
            duration=Half,
            time_signature=TimeSignature(4, 4)
        ),
        GridPart(
            scale=Scale("A", "major"),
            chord=Chord("G#", "dim"),
            tempo=Tempo(120),
            duration=Half,
            time_signature=TimeSignature(3, 2)
        )
    ])

    assert len(grid.parts) == 4

    assert grid.parts[0].tempo == tempo
    assert grid.parts[0].time_signature == time_signature


def test_grid_part_repr():
    grid_part = GridPart(
        Scale("C", "ionian"),
        Chord("C", "maj7"),
        Whole,
        TimeSignature(4, 4),
        Tempo(60)
    )

    assert repr(grid_part) == (
        "GridPart("
        "scale=<Scale C ionian>, "
        "chord=<Chord Cmaj7>, "
        "time_signature=NoteDuration(name='Whole', base_units=4, divisor=1), "
        "tempo=TimeSignature(beat_unit=4, beats_per_bar=4), "
        "duration=Tempo(bpm=60), "
        "repeat=1, "
        "bypass=False)"
    )
