from PySide6.QtCore import Signal
from PySide6.QtWidgets import QComboBox

from beethoven.ui.constants import DEFAULT_MIDI_OUTPUT
from beethoven.ui.managers import AppManager


class MidiOutputComboBox(QComboBox):
    value_changed = Signal(str)

    def __init__(self, *args, manager: AppManager, value: str | None, **kwargs):
        super(MidiOutputComboBox, self).__init__(*args, **kwargs)

        self.manager = manager
        self.setup_items()

        if value:
            self.setCurrentText(value)

        self.currentIndexChanged.connect(self.value_changed.emit)

    def setup_items(self):
        self.addItem(DEFAULT_MIDI_OUTPUT)

        output_names = list(set(sorted(self.manager.adapters.midi.outputs)))

        self.addItems(output_names)
