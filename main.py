from tkinter import *
from pandas import *
import random
BACKGROUND_COLOR = "#B1DDC6"
card_language = ""
card_front_text = ""
lessons = ""
words_list = []

current_card = {}

#Reading CSV file

# try:
#     words_data_frame = read_csv("./data/words_to_learn.csv")
# except FileNotFoundError:
#     words_data_frame = read_csv("./data/L2.csv")
# finally:
#     words_list = words_data_frame.to_dict(orient="records")

l1_data_frame = read_csv("./data/L1.csv")
l1_list = l1_data_frame.to_dict(orient="records")
l2_data_frame = read_csv("./data/L2.csv")
l2_list = l2_data_frame.to_dict(orient="records")
l3_data_frame = read_csv("./data/L3.csv")
l3_list = l3_data_frame.to_dict(orient="records")
l4_data_frame = read_csv("./data/L4.csv")
l4_list = l4_data_frame.to_dict(orient="records")
l5_data_frame = read_csv("./data/L5.csv")
l5_list = l5_data_frame.to_dict(orient="records")
l6_data_frame = read_csv("./data/L6.csv")
l6_list = l6_data_frame.to_dict(orient="records")
l7_data_frame = read_csv("./data/L7.csv")
l7_list = l7_data_frame.to_dict(orient="records")
l8_data_frame = read_csv("./data/L8.csv")
l8_list = l8_data_frame.to_dict(orient="records")
l9_data_frame = read_csv("./data/L9.csv")
l9_list = l9_data_frame.to_dict(orient="records")
l10_data_frame = read_csv("./data/L10.csv")
l10_list = l10_data_frame.to_dict(orient="records")
l11_data_frame = read_csv("./data/L11.csv")
l11_list = l11_data_frame.to_dict(orient="records")
l12_data_frame = read_csv("./data/L12.csv")
l12_list = l12_data_frame.to_dict(orient="records")
l13_data_frame = read_csv("./data/L13.csv")
l13_list = l13_data_frame.to_dict(orient="records")

#



# New Word Function

def new_word():
    global current_card
    try:
        current_card = random.choice(words_list)
    except:
        canvas.itemconfig(card_language, text="No more characters!", fill="black")
        canvas.itemconfig(card_front_text, text="Restart?", fill="black")
        canvas.itemconfig(card_background, image=card_front)
    else:
        canvas.itemconfig(card_language, text="Pinyin", fill="black")
        canvas.itemconfig(card_front_text, text=current_card["Pinyin"], fill="black")
        canvas.itemconfig(card_background, image=card_front)
        words_list.remove(current_card)




# Flip Card Function
def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_language, text="Character", fill="white")
    canvas.itemconfig(card_front_text, text=current_card["Character"], fill="white")


# Remove Word Function
# def remove_word():
#     global current_card
#     words_list.remove(current_card)
#     print(len(words_list))
#     new_dataframe = DataFrame(words_list)
#     new_dataframe.to_csv("./data/words_to_learn.csv", index=False)
#     new_word()


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card App")


#Main Screen

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front)

checkmark_image = PhotoImage(file="./images/right.png")
right_button = Button(image=checkmark_image, highlightthickness=0, command=new_word)

x_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=x_image, highlightthickness=0, command=flip_card)


# Printing main screen

def main_screen():
    global card_language
    global card_front_text
    global lessons
    next_button.destroy()
    listbox.destroy()
    canvas.grid(column=0, row=0, columnspan=2, sticky="EW")
    card_language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
    card_front_text = canvas.create_text(400, 263, width=780, text="", font=("SimHei", 40, "bold"))
    right_button.grid(column=1, row=1)
    wrong_button.grid(column=0, row=1)
    new_word()


def select_lessons():
    global lessons, words_list
    lessons = listbox.curselection()
    if 0 in lessons:
        words_list = words_list + l1_list
    if 1 in lessons:
        words_list = words_list + l2_list
    if 2 in lessons:
        words_list = words_list + l3_list
    if 3 in lessons:
        words_list = words_list + l4_list
    if 4 in lessons:
        words_list = words_list + l5_list
    if 5 in lessons:
        words_list = words_list + l6_list
    if 6 in lessons:
        words_list = words_list + l7_list
    if 7 in lessons:
        words_list = words_list + l8_list
    if 8 in lessons:
        words_list = words_list + l9_list
    if 9 in lessons:
        words_list = words_list + l10_list
    if 10 in lessons:
        words_list = words_list + l11_list
    if 11 in lessons:
        words_list = words_list + l12_list
    if 12 in lessons:
        words_list = words_list + l13_list


    main_screen()

listbox = Listbox(height=13, selectmode=MULTIPLE)
listbox.insert(0, "L1")
listbox.insert(1, "L2")
listbox.insert(2, "L3")
listbox.insert(3, "L4")
listbox.insert(4, "L5")
listbox.insert(5, "L6")
listbox.insert(6, "L7")
listbox.insert(7, "L8")
listbox.insert(8, "L9")
listbox.insert(9, "L10")
listbox.insert(10, "L11")
listbox.insert(11, "L12")
listbox.insert(12, "L13")

listbox.grid(column=0, row=0, sticky="EW")


next_button = Button(text="Next", command=select_lessons)
next_button.grid(column=1, row=1, sticky="EW")






window.mainloop()

