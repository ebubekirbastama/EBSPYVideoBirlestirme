import os
from tkinter import Tk, Label, Button, filedialog, messagebox
from moviepy.editor import VideoFileClip, concatenate_videoclips

def select_video1():
    global video1_path
    video1_path = filedialog.askopenfilename(title="1. Videoyu Seçin", filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
    video1_label.config(text=f"1. Video: {video1_path.split('/')[-1]}")

def select_video2():
    global video2_path
    video2_path = filedialog.askopenfilename(title="2. Videoyu Seçin", filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
    video2_label.config(text=f"2. Video: {video2_path.split('/')[-1]}")

def merge_videos():
    if video1_path and video2_path:
        # Videoları yükleyin
        clip1 = VideoFileClip(video1_path)
        clip2 = VideoFileClip(video2_path)

        # Videoları ardışık olarak birleştirin
        final_clip = concatenate_videoclips([clip1, clip2])

        # Birleştirilmiş videonun kaydedileceği klasörü oluştur
        output_dir = "Birlesmis_Videolar"
        os.makedirs(output_dir, exist_ok=True)

        # Birleştirilmiş videoyu belirlenen klasöre kaydedin
        output_path = os.path.join(output_dir, "birlesmis_video.mp4")
        final_clip.write_videofile(output_path)

        messagebox.showinfo("Başarılı", f"Birleştirilmiş video başarıyla '{output_path}' olarak kaydedildi.")
    else:
        messagebox.showwarning("Uyarı", "Lütfen iki video dosyası seçin.")

# Tkinter GUI oluşturma
root = Tk()
root.title("Video Birleştirici")

video1_path = ""
video2_path = ""

Label(root, text="Video Birleştirici").grid(row=0, column=0, columnspan=2, pady=10)

video1_label = Label(root, text="1. Videoyu Seçin")
video1_label.grid(row=1, column=0, padx=10, pady=10)

video2_label = Label(root, text="2. Videoyu Seçin")
video2_label.grid(row=2, column=0, padx=10, pady=10)

Button(root, text="1. Videoyu Seç", command=select_video1).grid(row=1, column=1, padx=10, pady=10)
Button(root, text="2. Videoyu Seç", command=select_video2).grid(row=2, column=1, padx=10, pady=10)

Button(root, text="Videoları Birleştir", command=merge_videos).grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
