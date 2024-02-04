import tkinter as tk
from PIL import ImageTk, Image
import RPi.GPIO as GPIO


class App():

	def __init__(self):
		self.window = tk.Tk()
		self.create_app()

	def check_int(self):
		self.window.after(1000, self.check_int)

	def create_app(self):
		window = self.window
		window.attributes("-fullscreen", True)
		window.title("Mars Freebie Randomiser")
	
		logoFrame = tk.Frame(window)
		logoFrame.pack(side=tk.TOP)
		logoHeight = int(window.winfo_screenheight() / 5)
		loadLogo = Image.open("./mars-logo.png")
		logoWidth = int(logoHeight * loadLogo.width / loadLogo.height)
		logoCanvas = tk.Canvas(logoFrame, bg="#17171F", height=logoHeight*1.2,
				width=window.winfo_screenwidth(), highlightthickness=0)
		logoCanvas.pack()
		self.logo = ImageTk.PhotoImage(loadLogo.resize((logoWidth, logoHeight),
			Image.NEAREST))
		logoCanvas.create_image(window.winfo_screenwidth()/2, logoHeight*0.6,
				image=self.logo)
	
		displayFrame = tk.Frame(window)
		displayFrame.pack(side=tk.BOTTOM)
		displayHeight = int(window.winfo_screenheight() * (1 - 1.2 / 5)) + 1
		self.canvas = tk.Canvas(displayFrame, bg="green", height=displayHeight,
				width=window.winfo_screenwidth(), highlightthickness=0)
		self.canvas.pack()
		self.canvasText = self.canvas.create_text(window.winfo_screenwidth()/2, displayHeight/2,
				text="Press the button to spin!", font=('Roboto', '50', 'bold'))
	
	def run_app(self):
		self.window.mainloop()

	def update_display(self, name: str, background: str):
		self.canvas.itemconfig(self.canvasText, text=name)
		self.canvas.configure(bg=background)
