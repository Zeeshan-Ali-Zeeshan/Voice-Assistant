import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class AIAssistantUI(tk.Tk):
    def __init__(self, gif_path, png_path, gif_size=(200, 200), png_size=(200, 200)):
        super().__init__()

        # Transparent fullscreen window
        self.attributes('-fullscreen', True)
        self.configure(bg='black')
        self.overrideredirect(True)
        self.wm_attributes('-topmost', True)
        self.wm_attributes('-transparentcolor', 'black')

        # Load and resize PNG
        png_image = Image.open(png_path).convert("RGBA").resize(png_size, Image.Resampling.LANCZOS)
        self.png_photo = ImageTk.PhotoImage(png_image)

        # PNG Label (centered directly on the window)
        self.png_label = tk.Label(self, image=self.png_photo, bg='black', borderwidth=0, highlightthickness=0)
        self.png_label.place(relx=0.5, rely=0.5, anchor='center')

        # Load and resize GIF frames
        self.original_gif = Image.open(gif_path)
        self.frames = [
            ImageTk.PhotoImage(frame.convert("RGBA").resize(gif_size, Image.Resampling.LANCZOS))
            for frame in ImageSequence.Iterator(self.original_gif)
        ]

        self.frame_index = 0

        # GIF Label (also centered directly on the window)
        self.gif_label = tk.Label(self, bg='black', borderwidth=0, highlightthickness=0)
        self.gif_label.place(relx=0.5, rely=0.5, anchor='center')

        self.update_frame()

        # ESC to exit
        self.bind("<Escape>", lambda e: self.destroy())

    def update_frame(self):
        frame = self.frames[self.frame_index]
        self.gif_label.config(image=frame)
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        delay = self.original_gif.info.get('duration', 50)
        self.after(delay, self.update_frame)

if __name__ == "__main__":
    app = AIAssistantUI(
        gif_path=r"E:\Shadow\ui\XDZT.gif",
        png_path=r"E:\Shadow\ui\1.png",
        gif_size=(200, 200),
        png_size=(200, 200)
    )
    app.mainloop()
