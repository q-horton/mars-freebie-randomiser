from app import *
from goodies import *
import tkinter as tk
import RPi.GPIO as GPIO
import signal
import sys
import time


BUTTON_PIN = 14


def main():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING,
			callback=button_callback, bouncetime=2500)
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


def randomiser_flash():
	global goodies, app
	app.update_display("Roll!", "white")
	time.sleep(0.5)
	for i in range(1, 6):
		app.update_display("." * i, "white")
		time.sleep(0.2)
	reward, colour = goodies.draw_goodie()
	app.update_display(reward, colour)


def button_callback(channel):
	global button_protect
	if not button_protect:
		button_protect = True
		randomiser_flash()
		button_protect = False


if __name__ == "__main__":
    main()
