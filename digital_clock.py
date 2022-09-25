#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 08:38:19 2022

@author: milouchev
"""

# Using Tkinter package to create the graphical user interface (GUI)
import tkinter as ui
import time

window = ui.Tk()
window.title("Digital Clock")

def clock_update():
# "%I" for 12-hour clock, "%H" for 24-hour clock
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_pm = time.strftime("%p")
    clock_text = hours + ":" + minutes + ":" + seconds, am_pm
    clock_label.config(text=clock_text)
    clock_label.after(1000, clock_update)
    
clock_label = ui.Label(window, font="Garamond 120 bold")
clock_label.pack()
clock_update()

window.mainloop()