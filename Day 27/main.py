from tkinter import *

window = Tk()

window.title("Mile to km comvertor")
window.config(padx=15, pady=15)



user_input = Entry(width=20)
user_input.grid(row=0, column=1)

miles_text = Label(text="Miles")
miles_text.grid(row=0, column=2)

is_equal_text = Label(text="is equal to")
is_equal_text.grid(column=0, row=1)

converted_value = Label(text="0")
converted_value.grid(column=1, row=1)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

def mile_to_km():
    miles = user_input.get()
    print(miles)
    km = float(miles) * 1.60934
    converted_value["text"] = km

calc_button = Button(text="Calculate", command= mile_to_km)
calc_button.grid(column=1, row=2)







window.mainloop()

