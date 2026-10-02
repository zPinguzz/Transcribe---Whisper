from interface_component import AudioTranscriber
from whisper_transcribe import WhisperTranscriber
from Interface_transcriber import TranscriberFactory 

class WhisperTranscriberFactory(TranscriberFactory):
    # factory effettiva che implementa tutto
    available_models = ["tiny", "base", "small", "medium", "large"]

    def create_transcriber(self, model_name: str) -> AudioTranscriber:
        normalizedName = model_name.lower()
        if normalizedName not in self.available_models:
            available = ", ".join(self.available_models)
            raise ValueError(f"Modello non valido. Scegli tra {available}.")
        return WhisperTranscriber(normalizedName)