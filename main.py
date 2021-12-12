from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def generate(i=None):
    n = no_of_digits.get()
    if n.isdigit() and 6<=int(n)<=64:
        a,b,c,d = password_checkvar1.get(),password_checkvar2.get(),password_checkvar3.get(),password_checkvar4.get()
        s = ""
        if a == 0 and b == 0 and c == 0 and d == 0:
            s+="abcdefghijklmnopqrstuvwxyz"
            s+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            s+="0123456789"
            s+="!@#$%^&*?"
        else:
            if a == 1:
                s+="abcdefghijklmnopqrstuvwxyz"
            if b == 1:
                s+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if c == 1:
                s+="0123456789"
            if d == 1:
                s+="!@#$%^&*?"
        password = "".join(random.choices(s,k=int(n)))
        status = messagebox.askquestion("Password Generated Successfully","Password: "+password+"\nClick on Yes to copy password to clipboard")
        if status == "yes":
            pyperclip.copy(password)
    else:
        messagebox.showerror("Enter a valid Number","Please enter No. of digits between range (6-64)")

main = Tk()
main.title("Password Generator")
main.geometry("300x170")
main.maxsize(300,170)
main.minsize(300,170)

password_checkvar1 = IntVar()
password_checkvar2 = IntVar()
password_checkvar3 = IntVar()
password_checkvar4 = IntVar()

label1 = Label(main,text="If none of checkboxes are checked,\nall four character sets are included in the password.")
label1.pack()

check_buttons_frame = Frame(main)
check_buttons_frame.pack()

lc_alphabets_check = Checkbutton(check_buttons_frame,text="a-z",variable=password_checkvar1,onvalue=1,offvalue=0)
lc_alphabets_check.grid(row=0,column=0)

uc_alphabets_check = Checkbutton(check_buttons_frame,text="A-Z",variable=password_checkvar2,onvalue=1,offvalue=0)
uc_alphabets_check.grid(row=0,column=1)

numbers_check = Checkbutton(check_buttons_frame,text="0-9",variable=password_checkvar3,onvalue=1,offvalue=0)
numbers_check.grid(row=0,column=2)

special_check = Checkbutton(check_buttons_frame,text="special characters",variable=password_checkvar4,onvalue=1,offvalue=0)
special_check.grid(row=1,column=1)

digit_frame = Frame(main)
digit_frame.pack()

digit_label = Label(digit_frame,text="No. of digits")
digit_label.grid(row=0,column=0)

no_of_digits = StringVar(value=6)
digit_box = Spinbox(digit_frame, from_=6, to=64, textvariable=no_of_digits, wrap=False)
digit_box.grid(row=0,column=1)

generate_button = Button(main,text="Generate",command=generate)
generate_button.pack(pady=15)

main.bind("<Return>",generate)
main.mainloop()
