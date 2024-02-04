from app import *
from goodies import *
import tkinter as tk
import RPi.GPIO as GPIO
import signal
import sys


BUTTON_PIN = 14


def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING,
			callback=button_callback, bouncetime=250)
	signal.signal(signal.SIGINT, exit_handler)
	
	global goodies
	goodies = Goodies("./freebies.json")

	global app
	app = App()
	app.window.after(1000, app.check_int)
	app.window.bind_all('<Control-c>', exit_handler)

	global button_protect
	button_protect = False

	app.run_app()


def exit_handler(sig, frame):
	GPIO.cleanup()
	app.window.destroy()
	sys.exit(0)


def button_callback(channel):
	global button_protect, goodies, app
	if not button_protect:
		button_protect = True
		reward, colour = goodies.draw_goodie()
		app.update_display(reward, colour)
		button_protect = False


if __name__ == "__main__":
    main()
