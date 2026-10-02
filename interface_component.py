from abc import ABC, abstractmethod

class AudioTranscriber(ABC): #interfaccia astratta per la trascrizione audio
    # funzione per la trascrizione
    @abstractmethod
    def transcribe_file(self, path_file: str) -> str:
        pass
