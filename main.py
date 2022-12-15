from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = ("Helvetica", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] + \
                    [random.choice(symbols) for char in range(nr_symbols)] + \
                    [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {user}\nPassword: "
                                                          f"{password}\nIs it ok to save?")
    if is_ok:
        data = open("data.txt", "a")
        data.write(f"{website} | {user} | {password}\n")
        data.close()
        web_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=30)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)
# WEB ROWS
web_label = Label(text="Website:", font=FONT)
web_label.grid(row=1, column=0)
web_entry = Entry(width=52)
web_entry.grid(row=1, column=1, columnspan=2, sticky=W)
# USER/PASS ROWS
username_label = Label(text="Email/Username:", font=FONT)
username_label.grid(row=2, column=0)
user_entry = Entry(width=52)
user_entry.insert(0, "briantowner@gmail.com")
user_entry.grid(row=2, column=1, columnspan=2, sticky=W)
# PASSWORD ROWS
pass_label = Label(text="Password:", font=FONT)
pass_label.grid(row=3, column=0)
pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1, sticky=W)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky=W)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)

window.mainloop()
