from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'

window = Tk()
window.title("Flashy")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# reading csv
words = pandas.read_csv("./data/french_words.csv")
words_dict = words.to_dict()


# images
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
wrong_img = PhotoImage(file='./images/wrong.png')
right_img = PhotoImage(file='./images/right.png')

front_img = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=1, column=1, columnspan=2)

# text
language_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, 'italic'))
word_text = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, 'bold'))


# button commands
def flip_card():
    canvas.itemconfig(front_img, image=card_back)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=eng_trans, fill='white')


def wrong_pressed():
    canvas.itemconfig(front_img, image=card_front)
    canvas.itemconfig(language_text, text='French', fill='black')
    rand_int = random.randint(0, 100)
    random_word = words_dict['French'][rand_int]
    global eng_trans
    eng_trans = words_dict['English'][rand_int]
    canvas.itemconfig(word_text, text=random_word, fill='black')
    window.after(3000, func=flip_card)


wrong_btn = Button(image=wrong_img, highlightthickness=0, command=wrong_pressed)
wrong_btn.grid(row=2, column=1)
right_btn = Button(image=right_img, highlightthickness=0, command=wrong_pressed)
right_btn.grid(row=2, column=2)


window.mainloop()