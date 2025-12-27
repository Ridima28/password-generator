from tkinter import *
import secrets
import string


window = Tk()
window.title("password generator")
window.geometry("400x400")
window.config(background = "white")

label = Label(window, text = "GENERATE PASSWORD", bg = "white", fg = "black", font = ("Arial", 20, "bold"))
label.pack()



def generate_password(length =12):
    

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    symbols = string.punctuation
    digits = string.digits


    password = [secrets.choice(lowercase),secrets.choice(uppercase),secrets.choice(symbols),secrets.choice(digits) ]

    rest_char = lowercase+uppercase+symbols+digits
    for i in range(length-4):
        password.append(secrets.choice(rest_char))
    
    secrets.SystemRandom().shuffle(password)
    return "".join(password)



password_var = StringVar()
password_var.set(generate_password())

label = Label(window, textvariable= password_var,
            bg = "lightgrey", fg = "black",
            font = ("Arial", 15),
            height = 3, width = 30)
label.pack()

def update_password():
    password_var.set(generate_password())




frame = Frame(window)
frame.pack()
button = Button(frame, text = "generate password",  bg = "grey", fg = "black", command = update_password)
button.pack(pady = 10)
























window.mainloop()