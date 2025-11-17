from tkinter import *
from PIL import Image, ImageTk
def copyright():
  tk = Tk()
  tk.title("Copyright")

  canvas_width = 1000
  canvas_height = 500

  canvas = Canvas(tk, width=canvas_width, height=canvas_height)
  canvas.pack()

  # --- Load and resize background image ---
  img = Image.open("/home/arun/Minecraft/Launch/Python/images.jpeg")
  img = img.resize((canvas_width, canvas_height), Image.LANCZOS)
  bg_image = ImageTk.PhotoImage(img)

  canvas.create_image(0, 0, anchor="nw", image=bg_image)

  # --- Text ---
  canvas.create_text(150, 40, text="Copyright 2025", font=("Arial", 10))
  canvas.create_text(168, 60, text="Arun Chandrasekaran", font=("Arial", 10))
  canvas.create_text(210, 80, text="https://www.MArun.com/users/admin", font=("Arial", 10))
  canvas.create_text(195, 100, text="Or Contact admin@MArun.com", font=("Arial", 10))
  canvas.create_text(185, 120, text="This Game Was Made From:", font=("Arial", 10))
  canvas.create_text(285, 140, text="Creating a Voxel Engine (like Minecraft) from Scratch in Python", font=("Arial", 10))

  # --- Blue OK button ---
  def start_and_close():
      start_game()
      tk.destroy()
  def start_game():
    print("output:")
    for x in range(100):
      print(f"Starting Game...%{x}")
    print("Game Ready...")
    print("DONE %100")

  ok_button = Button(tk, text="Start Game", bg="blue", fg="white", command=start_and_close)
  ok_button.pack(pady=20)

  tk.mainloop()
copyright()