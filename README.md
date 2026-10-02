# 🎤 Simple Whisper Transcription Tool

A beginner-friendly tool to transcribe audio files using OpenAI Whisper.

## 📋 About This Project

This project is **currently in development** and was created by someone who's just starting to learn serious programming. The goal is simple: make Whisper transcription easy to use, even if you're not tech-savvy.

I'm learning as I go, so the code might not be perfect, but it works! I'm also learning English, so if you notice some strange phrasing, that's normal.

## ✨ What It Does Right Now

- 🖱️ **Easy file selection**: pick your audio file with a file dialog
- 🧠 **Choose your model**: tiny, base, small, medium or large (asked at startup, 3 attempts)
- ⚡ **Uses your GPU**: Whisper automatically uses an NVIDIA GPU if available, otherwise the CPU
- 🌍 **Automatic language detection**: Whisper detects the language by itself
- 🖨️ **Prints the transcription** in the terminal
- ✅ **Startup checks**: verifies that FFmpeg is installed and tells you if a GPU is detected

## 🔧 What You Need

### Software:
- Python 3.7 or newer (I recommend Python 3.10.9)
- **FFmpeg**: required by Whisper to process audio
  - *Windows*: `winget install ffmpeg` or download it online
  - *Mac*: `brew install ffmpeg`
  - *Linux*: `sudo apt install ffmpeg`
- **Tkinter** (for the file dialog): included with Python on Windows/Mac. On Linux: `sudo apt install python3-tk`

### Python packages:
```
pip install torch
pip install openai-whisper
```

### 🖥️ Hardware
- **Graphics card**: NVIDIA GPU is great but not required
- **RAM**: at least 8GB free
- **Internet**: to download the AI model (first time only)

## 🚀 How to Use It

1. **First time? Check your setup**:
```
   python check_cuda.py
```
   It shows if CUDA is available and which GPU you have.

2. **Run the tool**:
```
   python Textwise.py
```

3. **Type the model name** when asked (tiny, base, small, medium, large)
4. **Pick your audio file** when the window opens
5. **Wait** while it transcribes (the first run is slower because it downloads the model)
6. **Read the transcription** in the terminal

## 🧩 Project Structure

| File | What it does |
|------|--------------|
| `Textwise.py` | Main file: asks for the model, opens the file picker, runs the transcription |
| `check.py` | Checks for FFmpeg, GPU and input file |
| `check_cuda.py` | Standalone script to test CUDA/GPU |
| `interface_component.py` | Abstract class `AudioTranscriber` (the "contract" for any transcriber) |
| `Interface_transcriber.py` | Abstract class `TranscriberFactory` |
| `model_factory.py` | `WhisperTranscriberFactory`: validates the model name and creates the transcriber |
| `whisper_transcribe.py` | `WhisperTranscriber`: loads the Whisper model and transcribes the file |

The code uses the **Factory pattern**, so in the future other transcription engines can be added without rewriting the main file.

## 📽️ Audio Files That Work

- MP3
- WAV
- M4A
- MP4 (audio part)

## 🔄 Development Status

### ✅ Working Right Now:
- [x] File picker
- [x] Audio transcription
- [x] GPU support (if available)
- [x] Choose different Whisper models
- [x] Automatic FFmpeg check
- [x] Modular structure (abstract classes + factory)

### WIP:
- [ ] Save the transcription to a .txt file
- [ ] Fix the elapsed time (currently not measured correctly)
- [ ] Error log file
- [ ] Choose the language manually
- [ ] Better interface
- [ ] Automatic install of FFmpeg / torch / whisper
- [ ] WhatsApp audio support

### Maybe for the future:
- [ ] Video files
- [ ] Subtitle files
- [ ] Better text formatting
- [ ] Better error handling
- [ ] Process multiple files at once

## ⚠️ Things to Know

- **First time**: downloads the AI model. Bigger models take more time and space (large is around 3GB), be patient!
- **GPU helps**: much faster with a good graphics card
- **File size**: really long audio files need more RAM
- **Audio quality**: clear audio = better transcription

## 🐛 If Something Goes Wrong

- **FFmpeg error**: install FFmpeg and make sure it's in your system PATH
- **No GPU**: that's fine, it will use your CPU (slower)
- **Out of memory**: try a smaller model or a shorter audio file
- **Invalid model**: choose one of tiny, base, small, medium, large

## 🤝 Help and Contributions

Since I'm still learning, any help is welcome! If you find bugs or have ideas, I'd love to hear them.

## 📝 Learning Notes

- This is my first "real" programming project
- Comments in the code are often in Italian (sorry!)
- I'm trying to make it work first, then make it pretty
- After a new commit the code could be unstable

---

*Made by someone learning to code, trying to make AI transcription simple for everyone.*
*This code was created with the assistance of AI.*