from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generatePassword():
    password = generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as datafile:
            data = json.load(datafile)

    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message="No data file found")

    else:
        if website in data.keys():
            email = data[website]['email']  # nested dictionary
            password = data[website]['password']
            messagebox.showinfo(
                title=website, message=f"Username :{email}\n Password :{password}")
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        'email': email,

        'password': password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # to write json file
                # json.dump(new_data, data_file, indent=4)
                # to read json data use 'r' mode

                # print(data)
                # to update json data
                # reading old data
                data = json.load(data_file)
                # and updating it

                data.update(new_data)
        except FileNotFoundError:
            # f = open("data.json", "x") # this is to create a file only if it does not exist
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        except ValueError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # and saving it to original data
                json.dump(data, data_file, indent=4)

                # data_file.write(f"{website} | {email} | {password}\n")

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager App")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "anup@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(
    text="Generate Password", command=generatePassword)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# search button
search_button = Button(text="Search", command=find_password, width=12)

search_button.grid(row=1, column=2)

window.mainloop()
