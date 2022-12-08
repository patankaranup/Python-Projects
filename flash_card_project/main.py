from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# reading csv data
try:
    df = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_word.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = df.to_dict(orient="records")
# print(data)


def is_known():
    to_learn.remove(current_card)
    learn_df = pd.DataFrame(to_learn)
    learn_df.to_csv('./data/words_to_learn.csv', index=False)
    # print(len(to_learn))
    new_word()


def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    text = current_card['French']
    # print(current_card['French'])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=text, fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    text = current_card["English"]
    canvas.itemconfig(card_word, text=text, fill="white")

    pass


# creating window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# adding image to use it
right_image = PhotoImage(file='./images/right.png')
wrong_image = PhotoImage(file='./images/wrong.png')
back_image = PhotoImage(file='./images/card_back.png')
front_image = PhotoImage(file='./images/card_front.png')

# flash card
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="Title", font=(
    "Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=(
    "Arial", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

unknown_button = Button(
    image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_word)
unknown_button.grid(row=1, column=0)

check_button = Button(
    image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
check_button.grid(row=1, column=1)
canvas.grid(row=0, column=0, columnspan=2)

new_word()
window.mainloop()
