# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from github import Github
from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
Font=("Verdena",12)

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for letter in range(4)]
    password_numbers=[choice(numbers) for number in range(3)]
    password_symbols=[choice(symbols) for symbol in range(3)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

window=Tk()
window.title("Password generator")
window.config(pady=50, padx=50)
canvas=Canvas(width=300, height=310,highlightthickness=0)
logo=PhotoImage(file="logo.png")
canvas.create_image(150,150,image=logo)
canvas.grid(column=1, row=1, columnspan=2)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    if len(password)==0 or len(website)==0:
        messagebox.showwarning(title="Something went wrong", message="type in first!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You entered {email}, and password: {password} is it ok?")
        if is_ok and password!="":
            with open("password.txt", mode="a") as password_data:
                password_data.write(f"website: {website} | login: {email} | password: {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
website_label=Label(text="Website:", font=Font)
email_label=Label(text="Email/login:", font=Font)
password_label=Label(text="Password", font=Font)
website_label.grid(column=0, row=2)
email_label.grid(column=0, row=3)
password_label.grid(column=0, row=4)

#Enteies

website_entry=Entry(width=45)
website_entry.grid(column=1, row=2, columnspan=2)
website_entry.focus()
email_entry=Entry(width=45)
email_entry.grid(column=1,row=3, columnspan=2)
email_entry.insert(0,'patryk.ciwinski@gmail.com')
password_entry=Entry(width=32)
password_entry.grid(column=1,row=4)

#Buttons
generate_password_button=Button(text="Generate", width=10, command=generate_password)
generate_password_button.grid(column=2,row=4,columnspan=2)
add_button=Button(text="Add", width=38, command=save)
add_button.grid(column=1,row=5,columnspan=2)




window.mainloop()