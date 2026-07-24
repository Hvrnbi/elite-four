import tkinter as tk
from random import shuffle
from PIL import Image, ImageTk

# Window
root = tk.Tk()
root.title("Elite Four")
root.resizable(False, False)
root.geometry("1280x720")


# Canvas
cv = tk.Canvas(root, width=1280, height=720)
cv.place(x=0, y=0)

# Game variables
game_number = 4
games_list = ["N", "C"] # To finish


# Creation of the start menu
start_button: tk.Button

def menu():
    global start_button
    cv.delete("all")

    bg_rect = cv.create_rectangle(0, 0, 1280, 720, fill="#7993a3", outline="#7993a3")
    title = cv.create_text(640, 360, text="Elite Four", font=("Helvetica", 48, "bold"), fill="aliceblue")

    start_button = tk.Button(bg="#7993a3", fg="aliceblue", activebackground="aliceblue", activeforeground="#7993a3", text="START", font=("Helvetica", 24, "bold"), cursor="hand2", borderwidth=0, highlightthickness=0, command=start)
    start_button.place(x=576, y=600)


def start():
    # To finish
    global game_number, games_list
    shuffle(games_list)
    game_number = 0
    start_button.destroy()
    next_game()

def next_game():
    cv.delete("all")
    if game_number < len(games_list):
        if games_list[game_number] == "N":
            miss_n_init()
        elif games_list[game_number] == "C":
            mister_c_init()
    else:
        print("THE END")        # TODO the end

def reset():
    # To finish
    global game_number, miss_n_state, flour_qtt, flour_qtt_inc, sugar_qtt, sugar_qtt_inc, eggs_qtt, eggs_qtt_inc, milk_qtt, milk_qtt_inc, ingredients_height, mister_c_state, mister_c_dialog, skyline_image, ptimage, mister_c_input, mister_c_score
    game_number = 4

    # Miss N
    miss_n_state = 0
    flour_qtt = 0
    flour_qtt_inc = True
    sugar_qtt = 0
    sugar_qtt_inc = True
    eggs_qtt = 0
    eggs_qtt_inc = True
    milk_qtt = 0
    milk_qtt_inc = True
    ingredients_height = 359

    # Mister C
    mister_c_state = 0
    mister_c_dialog = 0
    skyline_image = 0
    ptimage = None
    mister_c_input = tk.Entry(root)
    mister_c_input.bind("<Return>", enter)
    mister_c_score = 0

    menu()


# General GUI functions
def draw_dialog_area():
    dialog_rect = cv.create_rectangle(8, 500, 1272, 712, fill="#ffffff", outline="#ffffff")
    dialog_name_rect = cv.create_rectangle(580, 484, 700, 500, fill="#ffffff", outline="#ffffff")

# Miss N game
miss_n_state = 0
flour_qtt = 0
flour_qtt_inc = True
sugar_qtt = 0
sugar_qtt_inc = True
eggs_qtt = 0
eggs_qtt_inc = True
milk_qtt = 0
milk_qtt_inc = True
miss_n_dialog: int
flour_qtt_text: int
sugar_qtt_text: int
eggs_qtt_text: int
milk_qtt_text: int
ingredients_height = 359

def miss_n_init():
    bg_rect = cv.create_rectangle(0, 0, 1280, 720, fill="#6abd9c", outline="#6abd9c")
    draw_dialog_area()
    dialog_name = cv.create_text(640, 500, text="Miss N", font=("Helvetica", 16, "bold"), fill="#163226")

    container_rect = cv.create_rectangle(1140, 80, 1240, 360, fill="#c9c9c9", outline="#c9c9c9")
    flour_rect = cv.create_rectangle(40, 100, 180, 280, fill="#fff4de", outline="#fff4de")
    flour_text = cv.create_text(110, 88, text="FLOUR", font=("Helvetica", 16), fill="#163226")
    sugar_rect = cv.create_rectangle(220, 160, 360, 280, fill="#ffb34f", outline="#ffb34f")
    sugar_top = cv.create_polygon(220, 160, 360, 160, 290, 100, fill="#ffb34f", outline="#ffb34f")
    sugar_text = cv.create_text(290, 88, text="SUGAR", font=("Helvetica", 16), fill="#163226")
    eggs_oval = cv.create_oval(400, 100, 540, 280, fill="#e6c493", outline="#e6c493")
    eggs_text = cv.create_text(470, 88, text="EGGS", font=("Helvetica", 16), fill="#163226")
    milk_rect = cv.create_rectangle(580, 160, 720, 280, fill="#ffffff", outline="#ffffff")
    milk_top = cv.create_rectangle(580, 100, 720, 160, fill="#0000cc", outline="#0000cc")
    milk_text = cv.create_text(650, 88, text="MILK", font=("Helvetica", 16), fill="#163226")

    miss_n_game()

def miss_n_game():
    global miss_n_dialog, flour_qtt, flour_qtt_inc, flour_qtt_text, sugar_qtt, sugar_qtt_inc, sugar_qtt_text, eggs_qtt, eggs_qtt_inc, eggs_qtt_text, milk_qtt, milk_qtt_inc, milk_qtt_text
    if miss_n_state == 0:
        miss_n_dialog = cv.create_text(640, 606, text="Hiiiiii! I'm Miss N and in my game, you'll have to make a crêpe!\n\
The rules are easy, just press SPACE when you think that a quantity is good.\n\
If you follow the recipe, you win. If you don't, you lose.\n\
Here is the recipe:\n\
- 170g of flour\n\
- 40g of sugar\n\
- 3 eggs\n\
- 600mL of milk\n\n\
Press SPACE to start, good luck <3", font=("Helvetica", 12), fill="#163226")
        flour_qtt_text = cv.create_text(110, 308, text="", font=("Helvetica", 16), fill="#163226")
        sugar_qtt_text = cv.create_text(290, 308, text="", font=("Helvetica", 16), fill="#163226")
        eggs_qtt_text = cv.create_text(470, 308, text="", font=("Helvetica", 16), fill="#163226")
        milk_qtt_text = cv.create_text(650, 308, text="", font=("Helvetica", 16), fill="#163226")

    elif miss_n_state == 1:
        if flour_qtt_inc:
            flour_qtt += 1
            if flour_qtt == 400:
                flour_qtt_inc = False
        else:
            flour_qtt -= 1
            if flour_qtt == 0:
                flour_qtt_inc = True

        cv.itemconfig(flour_qtt_text, text=str(flour_qtt))
        root.after(8, miss_n_game)

    elif miss_n_state == 2:
        if sugar_qtt_inc:
            sugar_qtt += 1
            if sugar_qtt == 100:
                sugar_qtt_inc = False
        else:
            sugar_qtt -= 1
            if sugar_qtt == 0:
                sugar_qtt_inc = True

        cv.itemconfig(sugar_qtt_text, text=str(sugar_qtt))
        root.after(10, miss_n_game)

    elif miss_n_state == 3:
        if eggs_qtt_inc:
            eggs_qtt += 1
            if eggs_qtt == 5:
                eggs_qtt_inc = False
        else:
            eggs_qtt -= 1
            if eggs_qtt == 0:
                eggs_qtt_inc = True

        cv.itemconfig(eggs_qtt_text, text=str(eggs_qtt))
        root.after(140, miss_n_game)

    elif miss_n_state == 4:
        if milk_qtt_inc:
            milk_qtt += 1
            if milk_qtt == 1000:
                milk_qtt_inc = False
        else:
            milk_qtt -= 1
            if milk_qtt == 0:
                milk_qtt_inc = True

        cv.itemconfig(milk_qtt_text, text=str(milk_qtt))
        root.after(4, miss_n_game)

def miss_n_end():
    global miss_n_state
    score = abs(flour_qtt - 170) * 3 + abs(sugar_qtt - 40) * 15 + abs(eggs_qtt - 3) * 200 + abs(milk_qtt - 600)
    if score < 300:
        cv.itemconfig(miss_n_dialog, text="Those crepes look delicious, great job!\nPress SPACE to continue <3")
        miss_n_state = 6
    else:
        cv.itemconfig(miss_n_dialog, text="It seems absolutely uneatable, I hope you'll do better next time.")
        root.after(5000, reset)


# Mister C game
mister_c_state = 0
images_list = ["images/bucharest.png", "images/dallas.png", "images/dublin.png", "images/kualalumpur.png", "images/lagos.png", "images/lyon.png", "images/warsaw.png"]
mister_c_answers = {"images/bucharest.png": ["bucharest", "Bucharest", "BUCHAREST"], "images/dallas.png": ["dallas", "Dallas", "DALLAS"], "images/dublin.png": ["dublin", "Dublin", "DUBLIN"], "images/kualalumpur.png": ["kuala lumpur", "Kuala lumpur", "Kuala Lumpur", "KUALA LUMPUR"], "images/lagos.png": ["lagos", "Lagos", "LAGOS"], "images/lyon.png": ["lyon", "Lyon", "LYON"], "images/warsaw.png": ["warsaw", "Warsaw", "WARSAW"]}
mister_c_dialog: int
skyline_image: int
ptimage = None
mister_c_input = tk.Entry(root)
mister_c_score = 0

def mister_c_init():
    shuffle(images_list)

    bg_rect = cv.create_rectangle(0, 0, 1280, 720, fill="#7cf27c", outline="#7cf27c")
    draw_dialog_area()
    dialog_name = cv.create_text(640, 500, text="Mister C", font=("Helvetica", 16, "bold"), fill="#0b6b0b")
    mister_c_game()

def mister_c_game():
    global mister_c_dialog, skyline_image, ptimage
    if mister_c_state == 0:
        mister_c_dialog = cv.create_text(640, 606, text="Halloooo, my name is Mister C !\n\
In my game, you'll have to recognize a city from his skyline, and the colors on the flag of its country.\n\
You will see 3 images, and you'll have to make 2 correct guesses if you want to continue.\n\
You only have one chance per image, good luck !\n\
Press SPACE to start", font=("Helvetica", 12), fill="#0b6b0b")
    if mister_c_state == 1:
        cv.itemconfig(mister_c_dialog, text="Which city do you think it is ?")
        ptimage = ImageTk.PhotoImage(file=images_list[0])
        skyline_image = cv.create_image(640, 242, image=ptimage, anchor=tk.CENTER)
        mister_c_input.place(x=640, y=680, anchor=tk.CENTER)

    elif mister_c_state == 2:
        cv.itemconfig(mister_c_dialog, text="Which city do you think it is ?")
        ptimage = ImageTk.PhotoImage(file=images_list[1])
        cv.itemconfigure(skyline_image, image=ptimage)

    elif mister_c_state == 3:
        cv.itemconfig(mister_c_dialog, text="Which city do you think it is ?")
        ptimage = ImageTk.PhotoImage(file=images_list[2])
        cv.itemconfigure(skyline_image, image=ptimage)

    elif mister_c_state == 4:
        cv.itemconfig(mister_c_dialog, text="Well played!\nPress SPACE to continue.")

    elif mister_c_state == 5:
        cv.itemconfig(mister_c_dialog, text="You have to work a little more, see you later !")
        root.after(5000, reset)

def mister_c_verif():
    global mister_c_score
    if mister_c_input.get() in mister_c_answers[images_list[mister_c_state - 1]]:
        mister_c_score += 1
        return True
    else:
        return False
        
        


# Handle the pressed keys

def space(_):
    global game_number, miss_n_state, ingredients_height, mister_c_state
    if game_number < len(games_list):
        if games_list[game_number] == "N":
            if miss_n_state == 0:
                miss_n_state = 1
                miss_n_game()
            elif miss_n_state == 1:
                miss_n_state = 2
                ingredients_height -= round(flour_qtt / 3)
                cv.create_rectangle(1141, 359, 1239, ingredients_height, fill="#fff4de", outline="#fff4de")
            elif miss_n_state == 2:
                miss_n_state = 3
                cv.create_rectangle(1141, ingredients_height, 1239, ingredients_height - round(sugar_qtt / 3), fill="#ffb34f", outline="#ffb34f")
                ingredients_height -= round(sugar_qtt / 3)
            elif miss_n_state == 3:
                miss_n_state = 4
                cv.create_line(1141, ingredients_height, 1239, ingredients_height, fill="#ffffff")
                cv.create_line(1180, ingredients_height, 1200, ingredients_height, fill="#ffcc00")
                ingredients_height -= 1
            elif miss_n_state == 4:
                miss_n_state = 5
                cv.create_rectangle(1141, ingredients_height, 1239, ingredients_height - round(milk_qtt / 3), fill="#ffffff", outline="#ffffff")
                miss_n_end()
            elif miss_n_state == 6:
                game_number += 1
                next_game()

        elif games_list[game_number] == "C":
            if mister_c_state == 0:
                mister_c_state = 1
                mister_c_game()
            elif mister_c_state == 4:
                game_number += 1
                next_game()
        
def enter(_):
    global mister_c_state, mister_c_score
    if game_number < 4:
        if games_list[game_number] == "C":
            if mister_c_state == 1:
                mister_c_verif()
                mister_c_input.delete(0, tk.END)
                mister_c_state = 2
                mister_c_game()
            elif mister_c_state == 2:
                mister_c_verif()
                mister_c_input.delete(0, tk.END)
                if mister_c_score == 2:
                    mister_c_state = 4
                    mister_c_input.destroy()
                else:
                    mister_c_state = 3
                mister_c_game()
            elif mister_c_state == 3:
                if mister_c_verif():
                    mister_c_state = 4
                    mister_c_game()
                else:
                    mister_c_state = 5
                    mister_c_game()
                mister_c_input.destroy()

root.bind("<space>", space)
mister_c_input.bind("<Return>", enter)


menu()
root.mainloop()
