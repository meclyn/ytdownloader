import os 
from tkinter import *
from tkinter import messagebox, filedialog
import yt_dlp
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap.constants import *


# Função para baixar o vídeo ou áudio usando yt-dlp
def baixar_video_yt_dlp(link, formato, path):
    ydl_opts = {
        'format': 'bestaudio/best' if formato == "MP3" else 'bestvideo+bestaudio',
        'outtmpl': f'{path}/%(title)s.%(ext)s',
    }

    # Se o formato for MP3, adicionamos a opção de conversão
    if formato == "MP3":
        ydl_opts.update({
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        messagebox.showinfo("Sucesso", f"{formato} baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função chamada ao clicar no botão de download
def baixar():
    link = link_entry.get()  # Pega o link inserido pelo usuário
    formato = formato_var.get()  # Pega o formato escolhido
    path = filedialog.askdirectory()  # Permite que o usuário escolha o diretório de salvamento

    if not link or not formato:
        messagebox.showwarning("Aviso", "Por favor, insira o link do vídeo e escolha o formato.")
        return

    baixar_video_yt_dlp(link, formato, path)

# Criando a interface com Tkinter
janela = ttk.Window(themename="darkly")
janela.title("YouTheus")
janela.geometry("400x250")
janela.resizable(False, False)


# Label e entrada para o link do vídeo
link_label = Label(janela, text="Link do vídeo:")
link_label.pack(pady=10)
link_entry = Entry(janela, width=50)
link_entry.pack(pady=5)

# Opções de formato (MP3 ou MP4)
formato_var = StringVar(value="MP4")
formato_label = ttk.Label(janela, text="Escolha o formato:")
formato_label.pack(pady=10)

mp4_radio = ttk.Radiobutton(janela, text="MP4 (Vídeo)", variable=formato_var, value="MP4")
mp4_radio.pack()

mp3_radio = ttk.Radiobutton(janela, text="MP3 (Áudio)", variable=formato_var, value="MP3")
mp3_radio.pack()

# Botão de download
baixar_button = ttk.Button(janela, text="Baixar", bootstyle="success", command=baixar)
baixar_button.pack(pady=20)

# Executar a janela
janela.mainloop()

