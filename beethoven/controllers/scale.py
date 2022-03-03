from beethoven.controllers.interval import IntervalController
from beethoven.controllers.note import NoteController
from beethoven.helpers.note import add_interval_to_note
from beethoven.indexes import scale_index
from beethoven.models import Scale
from beethoven.utils.parser import parse_model_string


class ScaleController:
    @classmethod
    def parse(cls, string: str) -> Scale:
        parsed = parse_model_string("scale", string)

        return cls.construct(parsed)

    @classmethod
    def construct(cls, parsed: dict) -> Scale:
        tonic = NoteController.construct(parsed["tonic"])

        intervals_string = scale_index.get_intervals(parsed["name"])
        intervals = IntervalController.parse_list(intervals_string)

        notes = [add_interval_to_note(tonic, interval) for interval in intervals]

        return Scale(tonic=tonic, name=parsed["name"], notes=notes, intervals=intervals)
