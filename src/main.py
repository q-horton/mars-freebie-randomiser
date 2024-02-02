import json
import tkinter as tk
from PIL import ImageTk, Image


def main():
    global data
    data = pullJSON("freebies.json")
    app()


def pullJSON(file: str) -> list:
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def app():
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("Mars Freebie Randomiser")

    logoFrame = tk.Frame(window)
    logoFrame.pack(side=tk.TOP)
    loadLogo = Image.open("./mars-logo.png")
    logoHeight = int(window.winfo_screenheight() / 5)
    logoWidth = int(logoHeight * loadLogo.width / loadLogo.height)
    logoCanvas = tk.Canvas(logoFrame, bg="#17171F", height=logoHeight*1.2,
                           width=window.winfo_screenwidth(),
                           highlightthickness=0)
    logoCanvas.pack()
    logo = ImageTk.PhotoImage(loadLogo.resize((logoWidth, logoHeight),
                                              Image.NEAREST))
    logoCanvas.create_image(window.winfo_screenwidth()/2, logoHeight*0.6,
                            image=logo)

    displayFrame = tk.Frame(window)
    displayFrame.pack(side=tk.BOTTOM)
    displayHeight = int(window.winfo_screenheight() * (1 - 1.2 / 5)) + 1
    displayCanvas = tk.Canvas(displayFrame, bg="green", height=displayHeight,
                              width=window.winfo_screenwidth(),
                              highlightthickness=0)
    displayCanvas.pack()
    displayCanvas.create_text(window.winfo_screenwidth()/2, displayHeight/2,
                              text="Press the button to spin!")

    window.mainloop()


if __name__ == "__main__":
    main()
