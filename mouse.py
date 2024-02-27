import pyautogui
import time
import random
import keyboard

# Define the range of pixels the mouse can move in any direction
pixel_amount =  1
# Time interval between mouse movements
time_amount =  10
# State variable to control the program's activation
active = True

def move_mouse():
    """
    Moves the mouse cursor by a random amount within the defined range.
    This function is called repeatedly to keep the mouse active.
    """
    if not active:  # Skip if the program is not active
        return

    # Get the current mouse position
    current_position = pyautogui.position()
    
    # Generate random offsets for x and y within the range
    x_offset = random.randint(-pixel_amount, pixel_amount)
    y_offset = random.randint(-pixel_amount, pixel_amount)
    
    # Calculate the new position by adding the offsets
    new_position = (current_position[0] + x_offset, current_position[1] + y_offset)
    
    # Move the mouse to the new position
    pyautogui.moveTo(*new_position)

def toggle_program():
    """
    Toggles the program's active state.
    When active, the mouse moves; when inactive, the mouse stays still.
    """
    global active
    active = not active  # Toggle the active state
    print(f"Program {'active' if active else 'inactive'}")

# Set up a hotkey to toggle the program's state
keyboard.add_hotkey('ctrl+alt+p', toggle_program)

# Main loop that moves the mouse every time_amount seconds
while True:
    move_mouse()
    time.sleep(time_amount)
