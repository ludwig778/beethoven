from beethoven.ui.components.selectors.multiple.base import MultipleSelector
from beethoven.ui.constants import CHORD_LABELS, CHORDS_DATA, SELECTED_CHORD_LABELS


class MultipleChordSelector(MultipleSelector):
    def __init__(self, *args, **kwargs):
        super(MultipleChordSelector, self).__init__(
            *args,
            data=CHORDS_DATA,
            labels=CHORD_LABELS,
            expanded_labels=SELECTED_CHORD_LABELS,
            checked_labels=SELECTED_CHORD_LABELS,
            **kwargs
        )
