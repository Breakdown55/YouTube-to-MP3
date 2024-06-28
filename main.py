import tkinter as tk
from pytube import YouTube
import os
import platform
from pydub import AudioSegment
import threading



def get_downloads_folder():
    home = os.path.expanduser("~")
    return os.path.join(home, "Downloads")

def download_audio(save_path=get_downloads_folder()):
    downloadButton.configure(text="Downloading...")
    root.update_idletasks()
    try:
        yt = YouTube(linkEntry.get())
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file_path = audio_stream.download(save_path)
        audio = AudioSegment.from_file(audio_file_path)
        mp3_file_path = os.path.splitext(audio_file_path)[0] + '.mp3'
        audio.export(mp3_file_path, format="mp3")
        os.remove(audio_file_path)
        label.configure(text=f"Saved to {mp3_file_path}")
        downloadButton.configure(text="Download MP3")

    except Exception as e:
        label.configure(text=f"An error occurred: {e}")
        downloadButton.configure(text="Download MP3")

def start_download_thread():
    threading.Thread(target=download_audio).start()



root = tk.Tk()
root.title("YouTube to MP3")

linkEntry = tk.Entry(root, width=50)
linkEntry.pack(pady=10)

downloadButton = tk.Button(root, text="Download MP3", command=start_download_thread)
downloadButton.pack(pady=10)

label = tk.Label(root, text="Click to download!")
label.pack(pady=10)




root.mainloop()
