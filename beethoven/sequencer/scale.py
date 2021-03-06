from beethoven.sequencer.chord import Chord
from beethoven.sequencer.interval import AUGMENTED, DIMINISHED
from beethoven.sequencer.note import Note
from beethoven.theory.scale import Scale as BaseScale


class Scale(BaseScale):
    def __init__(self, tonic, name):
        self._load_attributes(tonic, name)

    def __repr__(self):
        return f"<Scale {str(self)}>"

    def __str__(self):
        return f"{self.tonic.name} {self.name}"

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.tonic == other.tonic and
            self.notes == other.notes
        )

    def __hash__(self):
        return id(self.name)

    def _load_attributes(self, tonic, scale_name):
        if not isinstance(tonic, Note):
            tonic = Note(tonic)

        self.tonic = tonic

        if not (data := self._DIRECTORY.get(scale_name)):
            raise ValueError("Scale name does not exists")

        self.name, self.mode, self.intervals = data

        self.notes = [self.tonic] + [
            self.tonic + interval
            for interval in self.intervals[1:]
        ]

        self.mode_index = None
        if self.mode:
            self.mode_index = self._MODES_DIRECTORY[self.mode].index(str(self.name))

    def get_chord(self, start_degree, degrees, alteration=0, inversion=None, base_note=None, extensions=None):
        degrees = degrees.split(",")
        notes = []

        for degree in degrees:
            note = self.notes[(start_degree + int(degree) - 1) % 7]
            for _ in range(abs(alteration)):
                if alteration < 0:
                    note += DIMINISHED
                elif alteration > 0:
                    note += AUGMENTED
            notes.append(note)

        first_note = notes[0]
        intervals = []
        for note in notes:
            intervals.append(first_note // note)

        chord_name = Chord.get_chord_name_from_intervals(intervals)

        return Chord(
            first_note,
            chord_name.short,
            inversion=inversion,
            base_note=base_note,
            extensions=extensions
        )
