import sys
import threading
import time
from file_dialog import FileDialog
from check import check_ffmpeg, check_gpu, check_input
from model_factory import WhisperTranscriberFactory


def _update_transcription_timer(start_time, stop_event):
    while not stop_event.wait(1):
        elapsed_seconds = int(time.monotonic() - start_time)
        minutes, seconds = divmod(elapsed_seconds, 60)
        print(f"\rTranscription in progress - Time: {minutes:02d}:{seconds:02d}", end="", flush=True)


def main():
    factory = WhisperTranscriberFactory() #richiamo alla factory per creare il trascriber
    check_ffmpeg()  # Controlla se FFmpeg è installato
    check_gpu()  # Controlla se è disponibile una GPU NVIDIA

    transcriber = None # serve perchè cosi almeno viene inizializzata la variabile anche se non viene selezionato un modello valido
    for attempt in range(3):
        model_name = input(f"Seleziona un modello Whisper tra {factory.available_models}: ").strip().lower()
        try:
            transcriber = factory.create_transcriber(model_name)
            break  # Esce dal ciclo se il modello è valido
        except ValueError as e:
            print(e)
            if attempt < 2:
                print("Riprova.")
            else:
                print("Hai superato il numero massimo di tentativi. Uscita dal programma.")
                sys.exit(1)

    with FileDialog() as dialog:
        percorso_file = dialog.select_audio_file()
    if not percorso_file:
        print("Nessun file selezionato. Uscita dal programma.")
        sys.exit(1)

    stop_event = threading.Event()
    start_time = time.monotonic()
    print("Transcription in progress - Time: 00:00", end="", flush=True)
    timer_thread = threading.Thread(target=_update_transcription_timer, args=(start_time, stop_event))
    timer_thread.start()
    try:
        testo_trascritto = transcriber.transcribe_file(percorso_file)
    finally:
        elapsed_time = time.monotonic() - start_time
        stop_event.set()
        timer_thread.join()
        print(flush=True)
    print(f"Trascrizione completata in {elapsed_time:.2f} secondi.")
    print("il file trascritto è il seguente:")
    print(testo_trascritto)

if __name__ == "__main__":
    main()
