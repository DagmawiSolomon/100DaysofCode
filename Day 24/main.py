
with open("Input/Letters/starting_letter.docx") as starter_file:
    lines = starter_file.read().split("\n")
    x = lines[0].split(" ")


with open("Input/Names/invited_names.txt") as names_file:
    contents = names_file.read()
    names = contents.split("\n")
    for name in names:
        with open(f"Output/ReadyToSend/letter_for_{name}.docx", mode='w') as final_letter:
            x[1] = name
            message_list = [x[0] + " " + x[1] + ","] + lines[1:]
            new_message = ""
            for m in message_list:
                new_message += m + "\n"
            final_letter.write(new_message)




