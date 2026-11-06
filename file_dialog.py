import tkinter as GUI
from tkinter import filedialog


class FileDialog:
    AUDIO_FILE_TYPES = (("Audio Files", "*.mp3;*.wav;*.m4a;*.mp4"), ("All Files", "*.*"))

    def __init__(self, parent=None):
        self._owns_root = parent is None
        self.root = GUI.Tk() if self._owns_root else parent
        if self._owns_root:
            self.root.withdraw()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def select_file(self, **options):
        return filedialog.askopenfilename(parent=self.root, **options)

    def select_audio_file(self):
        return self.select_file(
            title="Seleziona un file audio",
            filetypes=self.AUDIO_FILE_TYPES
        )

    def close(self):
        if self._owns_root:
            self.root.destroy()
            self._owns_root = False
