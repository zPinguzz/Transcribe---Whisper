import whisper
from interface_component import  AudioTranscriber

class WhisperTranscriber(AudioTranscriber):
    def __init__(self, model_name: str):
        self.model = whisper.load_model(model_name)

    def transcribe_file(self, path_file: str) -> str:
        result = self.model.transcribe(path_file)
        return result["text"]