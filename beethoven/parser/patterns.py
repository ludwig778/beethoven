from pyparsing import (Combine, Empty, Group, Literal, Optional, Suppress,
                       Word, ZeroOrMore, alphas, delimitedList, nums, oneOf)

ENGLISH_NOTE_NOTATION = ("A", "B", "C", "D", "E", "F", "G")
SOLFEGE_NOTE_NOTATION = ("La", "Si", "Do", "Re", "Mi", "Fa", "Sol")

CHORD_EXTRA_CHARS = "_()-Δ°#ø+"
SCALE_EXTRA_CHARS = "_-#b"


Integer = Word(nums).setParseAction(lambda t: int(t[0]))

octave_pattern = Word(nums)("octave")
alteration_pattern = Word("#b")("alteration")

degree_pattern = (
    Optional(alteration_pattern) +
    oneOf("I II III IV V VI VII i ii iii iv v vi vi vii")("name")
)

note_pattern = (
    oneOf(ENGLISH_NOTE_NOTATION + SOLFEGE_NOTE_NOTATION)("name") +
    Optional(alteration_pattern) +
    Optional(octave_pattern)
)

interval_alteration_pattern = Combine(
    Literal("M") | Literal("m") | Word("a") | Word("d") | Empty()
)("alteration")

interval_pattern = Word(nums)("name") + interval_alteration_pattern

bpm_pattern = Integer("value")

time_signature_pattern = (
    Integer("beats_per_bar") +
    Suppress("/") +
    Integer("beat_unit")
)

duration_pattern = (
    Optional(
        Integer("numerator") +
        Optional(
            Suppress("/") +
            Integer("denominator")
        )
    ) +
    Optional(oneOf("W H Q E S")("base_duration"))
)

chord_pattern = (
    (
        Group(note_pattern)("root") |
        Group(degree_pattern)("degree")
    ) +
    Optional(Suppress("_")) +
    Optional(Word(alphas + nums + CHORD_EXTRA_CHARS)("name")) +

    ZeroOrMore(
        (Suppress(":i=") + Integer("inversion")) |
        (Suppress(":e=") + Word(nums + alphas + ",")("extensions")) |
        (Suppress(":b=") + Group(note_pattern)("base_note")) |
        (Suppress(":s=") + Group(degree_pattern)("base_degree")) |
        (Suppress(":d=") + Group(duration_pattern)("duration"))
    )
)

scale_pattern = (
    Group(note_pattern)("tonic") +
    Optional(Suppress("_") + Word(alphas + nums + SCALE_EXTRA_CHARS)("name"))
)

grid_pattern = delimitedList(Group(ZeroOrMore(
    Suppress("bpm=") + Group(bpm_pattern)("bpm") |
    Suppress("sc=") + Group(scale_pattern)("scale") |
    Suppress("ts=") + Group(time_signature_pattern)("time_signature") |
    Suppress("du=") + Group(duration_pattern)("duration") |
    Suppress("p=") + delimitedList(Group(chord_pattern), delim=",")("chords") |
    Suppress("r=") + Integer("repeat")
)), delim=";")("grid_parts")