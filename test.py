import tkinter as tk
import uuid
import logging
from tkinter import IntVar
from tkinter import StringVar
from tkinter import messagebox
from functools import partial
from tkinter import *



def main() :
    system = tk.Tk()
    system.configure(background = "#addbd9")
    system.geometry("1000x700")
    system.title("Auction System")
    label = tk.Label(system,
                   text = "Welcome to the auction system",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 36 bold italic").place(anchor = 'center', relx = 0.5, rely = 0.1)


    logInButton = tk.Button(system, text = "Manage id", 
        width = 18,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        command = manageId ,
        font = "Times 30 bold").place(anchor = 'center', relx = 0.5, rely = 0.3)
               
    toBidButton = tk.Button(system, text = "Place a bid", 
        width = 18,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        command =  placeABid,
        font = "Times 30 bold").place(anchor = 'center', relx = 0.5, rely = 0.5)
    
    viewbidsbutton = tk.Button(system, text = "View Bids", 
        width = 18,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        font = "Times 30 bold").place(anchor = 'center', relx = 0.5, rely = 0.7)
    
    exit = tk.Button(system, text = "Exit", command = system.destroy,
        width = 18,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        font = "Times 30 bold").place(anchor = 'center', relx = 0.5, rely = 0.9)
    tk.mainloop()
def placeABid():
    placeABidWin = tk.Tk()
    placeABidWin.configure(background = "#addbd9")
    placeABidWin.geometry("1000x700")
    placeABidWin.title("Place A Bid")
    labelCat = tk.Label(placeABidWin, text = 'Category',width = 10,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        font = "Times 30 bold").place(anchor = 'n', relx = 0.2, rely = 0.1)
    
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    

    CategoryCheckButton1 = tk.Checkbutton(placeABidWin,
                                             text = 'Technology',
                                             variable = CheckVar1,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.215)
    CategoryCheckButton2 = tk.Checkbutton(placeABidWin,
                                             text = 'Travel',
                                             variable = CheckVar2,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.25)
    CategoryCheckButton3 = tk.Checkbutton(placeABidWin,
                                             text = 'Sports Tickets',
                                             variable = CheckVar3,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.28)
    CategoryCheckButton4 = tk.Checkbutton(placeABidWin,
                                             text = 'Food',
                                             variable = CheckVar4,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.31)
    CategoryCheckButton5 = tk.Checkbutton(placeABidWin,
                                             text = 'Music',
                                             variable = CheckVar5,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.34)
    CategoryCheckButton6 = tk.Checkbutton(placeABidWin,
                                             text = 'Education',
                                             variable = CheckVar6,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             selectcolor="white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.37)
    CategoryCheckButton7 = tk.Checkbutton(placeABidWin,
                                             text = 'Sports',
                                             variable = CheckVar7,
                                             onvalue = 1,
                                             offvalue = 0,
                                             height = 1,
                                             width = 10,
                                             selectcolor = "white").place(anchor = 'center',
                                                               relx = 0.1,
                                                               rely = 0.41)

 
    placeABidWin.mainloop()
def manageId():
    idWin = tk.Tk()
    idWin.configure(background = "#addbd9")
    idWin.geometry("1000x700")
    idWin.title("Manage Id")
    label1 = tk.Label(idWin,
                   text = "Do you have a registration number?",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 32 bold italic").place(anchor = 'center', relx = 0.5, rely = 0.1)
    label2 = tk.Label(idWin,
                   text = "Enter here(xxxxxxx): ",
                   fg = "white",
                   bg = "#addbd9",
                   font = "Helvita 26 bold italic").place(anchor = 'center', relx = 0.5, rely = 0.3)
    v = StringVar()
    e = tk.Entry(idWin, textvariable=v)
    e.place(anchor = 'center', relx = 0.5, rely = 0.4)
    button = tk.Button(idWin, text="Enter", width = 10,
        activebackground = "#adb7db",
        activeforeground = "white",
        anchor = "center",
        cursor = "heart",
        height = 1,
        relief = "sunken",
        fg = "white",
        bg = "#898787",
        command = lambda: chkEntry,
        font = "Times 12 bold").place(anchor = 'center', relx = 0.5, rely = 0.5)
    
    

    
def chkEntry(e):
    regis = e.get()
    for t in resgis:
            if t.isalpha():
                messagebox.showerror("error", "try again")
                    
    else:
        tk.messagebox.showinfo('Your number is valid, welcome!')
        regis.set()
        
    




main()
