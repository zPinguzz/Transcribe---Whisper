from abc import ABC, abstractmethod
from interface_component import AudioTranscriber

class TranscriberFactory(ABC):
    @abstractmethod
    def create_transcriber(self) -> AudioTranscriber:
        pass

    