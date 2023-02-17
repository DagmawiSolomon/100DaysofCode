from tkinter import *
import pandas
FONT = "Roboto"
FONT_SIZE = 25

window = Tk()
window.title("Flash cards app")
window.config(pady=25, padx=25)


data = pandas.read_csv("data/french_words.csv")
data_dict = {row.French: row.English for (index, row) in data.iterrows()}
word_list = [ds for ds in data_dict.keys()]


count = 0
def generate_word():
    global count
    x = word_list[count]
    if count <= len(word_list) + 1:
        count += 1
    return x

print(generate_word())

def remove_from_list():
    print("removed form list")
    generate_word()


def load_more():
    generate_word()

def flip_card():
    generate_word()
    if flash_card["text"] == generate_word():
        flash_card["background"] = "white"
        flash_card["text"] = data_dict[generate_word()]
        flash_card['fg'] = "black"
    elif flash_card["text"] == data_dict[generate_word()]:
        flash_card["background"] = "#e2979c"
        flash_card["text"] = generate_word()
        flash_card['fg'] = "white"





flash_card = Button(text=generate_word(), background="#e2979c", font=(FONT,FONT_SIZE), fg="white", width=30, height=10, command=flip_card)
flash_card.pack()

check_btn = Button(text="Yes", background="#9bdeac", fg="white", width=6, height=2, font=(FONT,12, 'bold'), command=remove_from_list)
check_btn.pack(side="left", pady=30)

wrong_btn = Button(text="No", background="#e7305b", fg="white", width=6, height=2, font=(FONT,12, 'bold'), command=generate_word)
wrong_btn.pack(side="right", pady=30)



window.mainloop()