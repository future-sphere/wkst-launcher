import tkinter as tk
import tkinter.messagebox
from ctypes import windll
from util import get_current_pc_id
import os
import requests
windll.shcore.SetProcessDpiAwareness(1)

CODE_VERIFY_API = 'https://app.thefuturesphere.com/rooms/workstation-code/verify'
CURRENT_PC_ID = get_current_pc_id()

PC_LOOKUP = {
    1: '192.168.100.110',
    2: '192.168.100.111',
    3: '192.168.100.112',
    4: '192.168.100.113',
    5: '192.168.100.114',
    6: '192.168.100.115',
}

# Create a window
window = tk.Tk()
window.geometry("480x320")
# Title the window "Launch GPU Workstation"
window.title("Launch GPU Workstation")

# Create a text label "Please enter Workstation Code"
label = tk.Label(text="Please enter Workstation Code")
label.pack()

# Create a text entry box labeled "Workstation Code"
entry = tk.Entry()
entry.pack()

# Create a button labeled "Submit"
button = tk.Button(text="Launch")
button.pack()

helper_label = tk.Label(
    text="If you do not have a code, \n please contact your instructor. \n This is PC {}".format(
        CURRENT_PC_ID))
helper_label.pack()

# make all components centered
for component in (label, entry, button, helper_label):
    component.pack(expand=True)


def launch_rd(evt):
    # Get the text from the entry box
    code = entry.get()
    if len(code) != 6:
        # alert the user that the code is invalid using a popup
        tk.messagebox.showerror("Error", "Invalid Workstation Code")
        window.update()
        return

    # send the code to the API
    try:
        response = requests.get(CODE_VERIFY_API, params={'code': code})
        res_data = response.json()
        if res_data['success']:
            # launch the workstation
            os.system(
                'start "C:\\Users\\Student\\Moonlight\\Moonlight.exe stream" GPU-PC{} Desktop'.format(CURRENT_PC_ID))
        else:
            tk.messagebox.showerror("Error", 'Workstation code is incorrect.')
            return
    except Exception:
        tk.messagebox.showerror("Error", "Could not connect to server")
        return


# Bind the button to the function
button.bind("<Button-1>", launch_rd)

if __name__ == "__main__":
    window.mainloop()
