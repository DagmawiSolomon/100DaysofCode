from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20, bg="white")

canvas = Canvas(width=200, height=200, background="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

input_label1 = Label(text="Website: ", background="white")
input_label1.grid(row=1, column=0)

input_entry1 = Entry(width=35, background="white")
input_entry1.grid(row=1, column=1,columnspan=2)

input_label2 = Label(text="Email/Username: ", background="white")
input_label2.grid(row=2, column=0)

input_entry2 = Entry(width=35)
input_entry2.grid(row=2, column=1, columnspan=2)

input_label3 = Label(text="Password: ", background="white")
input_label3.grid(row=3, column=0)

input_entry3 = Entry(width=21)
input_entry3.grid(row=3, column=1)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = Button(text="Add",width=55)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()