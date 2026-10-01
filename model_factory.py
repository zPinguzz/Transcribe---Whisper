import whisper

Model_Name =("tiny", "base", "small", "medium", "large")

def create_model(model_name):
    """crea un modello Whisper basato sul nome specificato.
    """
    normalized_model_name = model_name.lower()
    if normalized_model_name not in Model_Name:
        avalable_models = ", ".join(Model_Name)
        raise ValueError(f"Nome del modello non valido. Scegli tra: {avalable_models}")
    model = whisper.load_model(normalized_model_name)
    return model

