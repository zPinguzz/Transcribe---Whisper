from itertools import count
import os
import sys
import time
import shutil
import traceback
import tkinter as GUI
from tkinter import filedialog, messagebox
import torch
import whisper
from check import check_ffmpeg, check_gpu, check_input
from model_factory import WhisperTranscriberFactory


def file_dialog():
    """Apre una finestra di dialogo per permettere all'utente di selezionare un file audio."""
    root = GUI.Tk()    
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Seleziona un file audio",
        filetypes=(("Audio Files", "*.mp3;*.wav;*.m4a;*.mp4"), ("All Files", "*.*"))
    )
    root.destroy()  # Chiude la finestra dopo aver selezionato il file
    return file_path


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

    percorso_file = file_dialog()
    if not percorso_file:
        print("Nessun file selezionato. Uscita dal programma.")
        sys.exit(1)

    start_time = time.time()
    end_time = time.time()
    elapsed_time = end_time - start_time
    testo_trascritto = transcriber.transcribe_file(percorso_file)
    print(f"Trascrizione completata in {elapsed_time:.2f} secondi.")
    print("il file trascritto è il seguente:")
    print(testo_trascritto)

if __name__ == "__main__":
    main()