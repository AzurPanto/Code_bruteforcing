import random
import tkinter as tk
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
    window.destroy()


# Function to set x to False when "No Enter" button is clicked


def no_enter_clicked():
    global enter_variable
    enter_variable = False
    window.destroy()


# Create the main window
window = tk.Tk()
window.title("Enter or No Enter")
window.geometry("300x100")

# Create the text on top
text = tk.Label(window, text="Press Enter after the code or not")
text.pack()

# Create the "Enter" button
enter_button = tk.Button(window, text="Enter", command=enter_clicked)
enter_button.pack()

# Create the "No Enter" button04664022
no_enter_button = tk.Button(window, text="No Enter", command=no_enter_clicked)
no_enter_button.pack()

# Start the tkinter event loop
window.mainloop()

#Define digits
digits = 4

#Function to set x to 3 if 3 is pressed


def digit_3_pressed():
    global digits
    digits = 3
    secondary.destroy()

#Function to set x to 4 if 4 is pressed


def digit_4_pressed():
    global digits
    digits = 4
    secondary.destroy()

#Function to set x to 4 if 4 is pressed


def digit_5_pressed():
    global digits
    digits = 5
    secondary.destroy()

#Create the secondary window
secondary = tk.Tk()
secondary.title("Digits")
secondary.geometry("300x100")

#Create text on top
text = tk.Label(secondary, text= "How many digits ?")

#create the 3 digits button
button_3 = tk.Button(secondary, text="3 digits", command=digit_3_pressed)
button_3.pack()

#Create the 4 digits button
button_4 = tk.Button(secondary, text="4 digits", command=digit_4_pressed)
button_4.pack()

#Create the 5 digits button
button_5 = tk.Button(secondary, text="5 digits", command=digit_5_pressed)
button_5.pack()

secondary.mainloop()

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