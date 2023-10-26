import random
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
import time
from pynput.keyboard import Key, Controller
from pynput import keyboard

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Create a keyboard controller to press keys
keyboard_controller = Controller()

# Define a flag to control text typing
script_enabled = False

# Ask user for input
# Initialize the variable x
enter_variable = False

# Function to set x to True when "Enter" button is clicked


def enter_clicked():
    global enter_variable
    enter_variable = True

# Function to set x to False when "No Enter" button is clicked


def no_enter_clicked():
    global enter_variable
    enter_variable = False

# Create the main window
window = ttk.Window(themename= "journal")
window.title("Enter or No Enter")
window.geometry("300x300")

# Create the text on top
text = ttk.Label(master = window, text="Press Enter after the code or not", font= "Calibri 16")
text.pack()

# Create the buttons frame
button_frame = ttk.Frame(master= window)
button_frame.pack(pady= 10)

# Create the "Enter" button
enter_button = ttk.Button(master = button_frame, text="Enter", command=enter_clicked)
enter_button.pack(side= "left", padx = 10)

# Create the "No Enter" button
no_enter_button = ttk.Button(master = button_frame, text="No Enter", command=no_enter_clicked)
no_enter_button.pack(side = "left")

#Define digits
digits = 4

#create the digits frame
digits_frame = ttk.Frame(master= window)
digits_frame.pack(pady= 20)

#Create text on top
text = ttk.Label(master = digits_frame, text= "How many digits ?", font= "Calibri 16")
text.pack()

#Function to set x to 3 if 3 is pressed


def digit_3_pressed():
    global digits
    digits = 3

#Function to set x to 4 if 4 is pressed


def digit_4_pressed():
    global digits
    digits = 4

#Function to set x to 4 if 4 is pressed


def digit_5_pressed():
    global digits
    digits = 5

#Function to close window


def close_window():
    window.destroy()

#create the 3 digits button
button_3 = ttk.Button(master= digits_frame, text="3 digits", command=digit_3_pressed)
button_3.pack(side= "left", padx = 10)

#Create the 4 digits button
button_4 = ttk.Button(master = digits_frame, text="4 digits", command=digit_4_pressed)
button_4.pack(side= "left", padx= 10)

#Create the 5 digits button
button_5 = ttk.Button(master = digits_frame, text="5 digits", command=digit_5_pressed)
button_5.pack(side= "left", padx= 10)

#Create the close button
close_button = ttk.Button(master= window, text = "Close", command=close_window)
close_button.pack(pady= 10)

# Start the tkinter event loop
window.mainloop()

# Check the value of enter_variable
print("enter_variable is:", enter_variable)
print(f"digit is {digits}")

# Script run on key press


def on_key_press(key):
    global script_enabled

    if key == Key.f5:
        script_enabled = not script_enabled  # Toggle the script state
        if script_enabled:
            print("Cracking code")
            # You can add your script logic here
        else:
            print("Stopping the cracking")


# Create a keyboard listener
listener = keyboard.Listener(on_press=on_key_press)

# Start listening for keypress events
listener.start()

# Define code and type it
while True:
    if script_enabled:
        if digits == 4:
            if enter_variable == True:
                code = ''.join(str(random.choice(numbers)) for _ in range(4))
                print(code)
                keyboard_controller.type(code)
                keyboard_controller.press(Key.enter)
                keyboard_controller.release(Key.enter)
                time.sleep(1)
            else:
                code = ''.join(str(random.choice(numbers)) for _ in range(4))
                print(code)
                keyboard_controller.type(code)
                time.sleep(1)
        elif digits == 3:
            if enter_variable == True:
                code = ''.join(str(random.choice(numbers)) for _ in range(3))
                print(code)
                keyboard_controller.type(code)
                keyboard_controller.press(Key.enter)
                keyboard_controller.release(Key.enter)
                time.sleep(1)
            else:
                code = ''.join(str(random.choice(numbers)) for _ in range(3))
                print(code)
                keyboard_controller.type(code)
                time.sleep(1)
        elif digits == 5:
            if enter_variable == True:
                code = ''.join(str(random.choice(numbers)) for _ in range(5))
                print(code)
                keyboard_controller.type(code)
                keyboard_controller.press(Key.enter)
                keyboard_controller.release(Key.enter)
                time.sleep(1)
            else:
                code = ''.join(str(random.choice(numbers)) for _ in range(5))
                print(code)
                keyboard_controller.type(code)
                time.sleep(1)
