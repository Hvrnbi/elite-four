import tkinter as tk
from random import shuffle, randint, choice
from PIL import Image, ImageTk
from pygame import mixer
import webbrowser as wb

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
games_list = ["N", "C", "E", "W"]


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
        elif games_list[game_number] == "E":
            mister_e_init()
        elif games_list[game_number] == "W":
            miss_w_init()
    else:
        # The END
        cv.create_rectangle(0, 0, 1280, 720, fill="#b7ddeb", outline="#b7ddeb")
        cv.create_text(640, 100, text="Well played!", font=("Helvetica", 64, "bold"), fill="#194a5c")
        cv.create_text(640, 310, text="Thank you for playing <3", font=("Helvetica", 48, "bold"), fill="#194a5c")
        cv.create_text(640, 520, text="Goodbyyyyye", font=("Helvetica", 64, "bold"), fill="#194a5c")
        github_link = cv.create_text(640, 660, text="PS : You can click here to put a star ⭐️ on GitHub :)", font=("Helvetica", 16, "bold"), fill="#194a5c")
        cv.tag_bind(github_link, "<Button-1>", lambda _ : wb.open("https://github.com/Hvrnbi/elite-four"))

def reset():
    global game_number, miss_n_state, flour_qtt, flour_qtt_inc, sugar_qtt, sugar_qtt_inc, eggs_qtt, eggs_qtt_inc, milk_qtt, milk_qtt_inc, ingredients_height, mister_c_state,\
mister_c_dialog, mister_c_result, skyline_image, ptimage, mister_c_input, mister_c_score, mister_e_state, mister_e_time, mister_e_time_count, mister_e_timer, mask_images,\
masks_list, happy_mask, mister_e_dialog, miss_w_state, miss_w_dialog, notes_id, f_list, g_list, h_list, j_list, k_list, l_list, miss_w_score, miss_w_score_text
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

    # Mister E
    mister_e_state = 0
    mister_e_time = 0
    mister_e_time_count = 0
    mister_e_timer = 0
    mask_images = []
    masks_list = []
    happy_mask = {}
    mister_e_dialog = 0

    # Miss W
    miss_w_state = 0
    miss_w_dialog = 0
    notes_id = []
    f_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 202]
    g_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 384]
    h_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 566]
    j_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 748]
    k_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 930]
    l_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 1112]
    miss_w_score = 0
    miss_w_score_text = 0

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
    eggs_oval =  cv.create_oval(400, 100, 540, 280, fill="#e6c493", outline="#e6c493")
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
mister_c_result: int
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
        mister_c_input.place(x=640, y=632, anchor=tk.CENTER)

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
    global mister_c_score, mister_c_result
    if mister_c_input.get() in mister_c_answers[images_list[mister_c_state - 1]]:
        mister_c_score += 1
        if mister_c_state == 1:
            mister_c_result = cv.create_text(640, 680, text="Correct!", font=("Helvetica", 12), fill="#0b6b0b")
        else:
            cv.itemconfig(mister_c_result, text="Correct!")
        return True
    else:
        if mister_c_state == 1:
            mister_c_result = cv.create_text(640, 680, text="Wrong!", font=("Helvetica", 12), fill="#0b6b0b")
        else:
            cv.itemconfig(mister_c_result, text="Wrong!")
        return False
        

# Mister E game
mister_e_state = 0
mister_e_time = 0
mister_e_time_count = 0
mister_e_timer: int
mask_images = []
masks_list = []
happy_mask = {}
mister_e_dialog: int


def mister_e_init():
    bg_rect = cv.create_rectangle(0, 0, 1280, 720, fill="#fda3ff", outline="#fda3ff")
    draw_dialog_area()
    dialog_name = cv.create_text(640, 500, text="Mister E", font=("Helvetica", 16, "bold"), fill="#730075")
    mister_e_game()

def mister_e_game():
    global mister_e_dialog, mister_e_state, mister_e_time, mister_e_time_count, mister_e_timer
    if mister_e_state == 0:
        mister_e_dialog = cv.create_text(640, 606, text="Hello! I'm Mister E, nice to meet you!\n\
In my game, you'll see some comedy masks, and you'll just have to find the happy one.\n\
Good luck!\n\
Press SPACE to start.", font=("Helvetica", 12), fill="#730075")

    elif mister_e_state == 1:
        spawn_masks()
        mister_e_state = 2
        mister_e_time = 15
        mister_e_timer = cv.create_text(1252, 700, text="15", font=("Helvetica", 16, "bold"), fill="#730075")
        mister_e_game()

    elif mister_e_state == 2:
        move_masks()
        mister_e_countdown()
        root.after(100, mister_e_game)

    elif mister_e_state == 3:
        mister_e_clear()
        cv.itemconfig(mister_e_dialog, text="Well done! But it was the easy level,\nPress SPACE to continue.")

    elif mister_e_state == 4:
        spawn_masks()
        mister_e_time = 20
        cv.itemconfig(mister_e_timer, text="20")
        mister_e_time_count = 0
        mister_e_state = 5
        mister_e_game()

    elif mister_e_state == 5:
        move_masks()
        mister_e_countdown()
        root.after(100, mister_e_game)

    elif mister_e_state == 6:
        mister_e_clear()
        cv.itemconfig(mister_e_dialog, text="Good job! You're ready to the next step,\nPress SPACE to continue.")

    elif mister_e_state == 7:
        spawn_masks()
        mister_e_time = 25
        cv.itemconfig(mister_e_timer, text="25")
        mister_e_time_count = 0
        mister_e_state = 8
        mister_e_game()

    elif mister_e_state == 8:
        move_masks()
        mister_e_countdown()
        root.after(100, mister_e_game)

    elif mister_e_state == 9:
        mister_e_clear()
        cv.itemconfig(mister_e_dialog, text="Well played! The next one is the last one, good luck!\nPress SPACE to continue.")

    elif mister_e_state == 10:
        spawn_masks()
        mister_e_time = 30
        cv.itemconfig(mister_e_timer, text="30")
        mister_e_time_count = 0
        mister_e_state = 11
        mister_e_game()

    elif mister_e_state == 11:
        move_masks()
        mister_e_countdown()
        root.after(100, mister_e_game)

    elif mister_e_state == 12:
        mister_e_clear()
        cv.itemconfig(mister_e_dialog, text="You did it!\nPress SPACE to continue.")
        
    elif mister_e_state == 13:
        mister_e_clear()
        cv.itemconfig(mister_e_dialog, text="Oh nooooo, the time is up!\nyou'll be luckier next time darling.")
        root.after(5000, reset)

def spawn_masks():
    global masks_list, happy_mask, mask_images
    mask_images.append(ImageTk.PhotoImage(file="images/happy.png"))
    happy_mask = {"id": cv.create_image(randint(0, 1280), randint(0, 500), image=mask_images[0], anchor=tk.CENTER), "velx": mask_vel_gen(), "vely": mask_vel_gen()}
    cv.tag_bind(happy_mask["id"], "<Button-1>", button1)
    for i in range(40 * mister_e_state // 3 + 1):
        mask_images.append(ImageTk.PhotoImage(file=choice(["images/sad.png", "images/fastfood.png"])))
        masks_list.append({"id": cv.create_image(randint(0, 1280), randint(0, 500), image=mask_images[i + 1], anchor=tk.CENTER), "velx": mask_vel_gen(), "vely": mask_vel_gen()})

def move_masks():
    global masks_list
    for mask in masks_list:
        cv.move(mask["id"], mask["velx"], mask["vely"])
        if cv.coords(mask["id"])[0] < 0 or 1280 < cv.coords(mask["id"])[0]:
            mask["velx"] = -mask["velx"]
        if cv.coords(mask["id"])[1] < 0 or 500 < cv.coords(mask["id"])[1]:
            mask["vely"] = -mask["vely"]
    cv.move(happy_mask["id"], happy_mask["velx"], happy_mask["vely"])
    if cv.coords(happy_mask["id"])[0] < 0 or 1280 < cv.coords(happy_mask["id"])[0]:
        happy_mask["velx"] = -happy_mask["velx"]
    if cv.coords(happy_mask["id"])[1] < 0 or 500 < cv.coords(happy_mask["id"])[1]:
        happy_mask["vely"] = -happy_mask["vely"]

def mask_vel_gen():
    vel = randint(6, 12)
    sign = randint(0, 1)
    if sign == 1:
        vel = -vel
    return vel

def mister_e_clear():
    global mask_images, masks_list, happy_mask
    for elt in masks_list:
        cv.delete(elt)
    mask_images = []
    masks_list = []
    happy_mask = {}


def mister_e_countdown():
    global mister_e_time, mister_e_time_count, mister_e_timer, mister_e_state
    mister_e_time_count += 1
    if mister_e_time_count % 10 == 0:
        mister_e_time -= 1
        cv.itemconfig(mister_e_timer, text=str(mister_e_time))
        if mister_e_time == 0:
            mister_e_state = 13


# Miss W game
miss_w_state = 0
miss_w_dialog: int
notes_list = [[748, -68], [930, -118], [1112, -168], [566, -314], [384, -364], [202, -414], [748, -524], [566, -624], [384, -724], [930, -724], [384, -774], [930, -774], [384, -824], [930, -824], [566, -968], [748, -1084], [566, -1162], [384, -1212], [202, -1262], [748, -1424], [384, -1524], [1112, -1624], [202, -1758],\
[748, -68 - 1808], [930, -118 - 1808], [1112, -168 - 1808], [566, -314 - 1808], [384, -364 - 1808], [202, -414 - 1808], [748, -524 - 1808], [566, -624 - 1808], [384, -724 - 1860], [930, -724 - 1860], [384, -774 - 1860], [930, -774 - 1860], [384, -824 - 1860], [930, -824 - 1860], [566, -968 - 1860], [748, -1084 - 1860], [566, -1162 - 1880], [384, -1212 - 1860], [202, -1262 - 1860], [748, -1424 - 1860], [384, -1524 - 1860], [1112, -1624 - 1860], [202, -1758 - 1860],\
[748, -68 - 3680], [930, -118 - 3680], [1112, -168 - 3680], [566, -314 - 3680], [384, -364 - 3680], [202, -414 - 3680], [748, -524 - 3700], [566, -624 - 3700], [384, -724 - 3700], [930, -724 - 3700], [384, -774 - 3700], [930, -774 - 3700], [384, -824 - 3700], [930, -824 - 3700], [566, -968 - 3700], [748, -1084 - 3700], [566, -1162 - 3700], [384, -1212 - 3700], [202, -1262 - 3700], [748, -1424 - 3700], [384, -1524 - 3700], [1112, -1624 - 3700], [202, -1758 - 3700],\
[748, -68 - 5500], [930, -118 - 5500], [1112, -168 - 5500], [566, -314 - 5500], [384, -364 - 5500], [202, -414 - 5500], [748, -524 - 5500], [566, -624 - 5500], [384, -724 - 5500], [930, -724 - 5500], [384, -774 - 5500], [930, -774 - 5500], [384, -824 - 5500], [930, -824 - 5500], [566, -968 - 5500], [748, -1084 - 5500], [566, -1162 - 5500], [384, -1212 - 5500], [202, -1262 - 5500], [748, -1424 - 5500], [384, -1524 - 5500], [1112, -1624 - 5500], [202, -1758 - 5500]]
notes_id = []
f_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 202]
g_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 384]
h_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 566]
j_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 748]
k_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 930]
l_list = [[i, 0] for i in range(len(notes_list)) if notes_list[i][0] == 1112]
miss_w_score = 0
miss_w_score_text = 0

def miss_w_init():
    bg_rect = cv.create_rectangle(0, 0, 1280, 720, fill="#c892e0", outline="#c892e0")
    draw_dialog_area()
    dialog_name = cv.create_text(640, 500, text="Miss W", font=("Helvetica", 16, "bold"), fill="#481a5b")
    miss_w_game()

def miss_w_game():
    global miss_w_state, miss_w_dialog, miss_w_score_text
    if miss_w_state == 0:
        miss_w_dialog = cv.create_text(640, 606, text="Helloooo, I'm Miss W!\n\
My game is a rythm game, good luck!\n\
Press SPACE to start.", font=("Helvetica", 12), fill="#481a5b")
    
    elif miss_w_state == 1:
        miss_w_draw_ui()
        spawn_notes()
        mixer.init()
        mixer.music.load("audio/scottish.mp3")
        mixer.music.set_volume(1.0)
        mixer.music.play()
        miss_w_state = 2
        miss_w_game()
        miss_w_score_text = cv.create_text(1252, 700, text="0", font=("Helvetica", 16, "bold"), fill="#481a5b")

    elif miss_w_state == 2:
        if cv.coords(notes_id[-1])[1] < 500:
            move_notes()
            root.after(20, miss_w_game)
        else:
            if miss_w_score < 840:
                miss_w_state = 3
                miss_w_game()
            else:
                miss_w_state = 4
                miss_w_game()

    elif miss_w_state == 3:
        cv.itemconfig(miss_w_dialog, text="You need more training, come back later !")
        root.after(5000, reset)

    elif miss_w_state == 4:
        cv.itemconfig(miss_w_dialog, text="Gg! That was a beautiful scottish! :D\nPress SPACE to continue")


def miss_w_draw_ui():
    cv.create_rectangle(0, 438, 1280, 442, fill="#ffffff", outline="#ffffff")
    cv.create_text(182, 460, text="F", font=("Helvetica", 16, "bold"), fill="#ffffff")
    cv.create_text(364, 460, text="G", font=("Helvetica", 16, "bold"), fill="#ffffff")
    cv.create_text(546, 460, text="H", font=("Helvetica", 16, "bold"), fill="#ffffff")
    cv.create_text(728, 460, text="J", font=("Helvetica", 16, "bold"), fill="#ffffff")
    cv.create_text(910, 460, text="K", font=("Helvetica", 16, "bold"), fill="#ffffff")
    cv.create_text(1092, 460, text="L", font=("Helvetica", 16, "bold"), fill="#ffffff")

def spawn_notes():
    global notes_id
    for note in notes_list:
        notes_id.append(cv.create_text(note[0], note[1], text="♩", font=("Helvetica", 64, "bold"), fill="#ffffff"))

def move_notes():
    global notes_id
    for i in range(len(notes_id)):
        if cv.coords(notes_id[i])[1] < 500:
            cv.move(notes_id[i], 0, 4)
            if cv.coords(notes_id[i])[1] >= 500:
                cv.move(notes_id[i], 0, 500)


# Handle the pressed keys

def space(_):
    global game_number, miss_n_state, ingredients_height, mister_c_state, mister_e_state, miss_w_state
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

        elif games_list[game_number] == "E":
            if mister_e_state in [0, 3, 6, 9]:
                mister_e_state += 1
                mister_e_game()
            elif mister_e_state == 12:
                game_number += 1
                next_game()

        elif games_list[game_number] == "W":
            if miss_w_state == 0:
                miss_w_state = 1
                miss_w_game()
            elif miss_w_state == 4:
                game_number += 1
                next_game()

    elif game_number == 4:
        start()

def enter(_):
    global mister_c_state, mister_c_score
    if game_number < len(games_list):
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

def button1(_):
    global mister_e_state
    if game_number < len(games_list):
        if games_list[game_number] == "E":
            if mister_e_state in [2, 5, 8, 11]:
                mister_e_state += 1

def f(_):
    global miss_w_score, f_list
    if miss_w_state == 2:
        for note in f_list:
            if note[1] == 0 and 408 <= cv.coords(notes_id[note[0]])[1] <= 472:
                note[1] = 1
                miss_w_score += 10
                cv.itemconfig(miss_w_score_text, text=str(miss_w_score))
                cv.itemconfig(notes_id[note[0]], fill="#a9e092")

def g(_):
    global miss_w_score, g_list
    if miss_w_state == 2:
        for note in g_list:
            if note[1] == 0 and 408 <= cv.coords(notes_id[note[0]])[1] <= 472:
                note[1] = 1
                miss_w_score += 10
                cv.itemconfig(miss_w_score_text, text=str(miss_w_score))
                cv.itemconfig(notes_id[note[0]], fill="#a9e092")

def h(_):
    global miss_w_score, h_list
    if miss_w_state == 2:
        for note in h_list:
            if note[1] == 0 and 408 <= cv.coords(notes_id[note[0]])[1] <= 472:
                note[1] = 1
                miss_w_score += 10
                cv.itemconfig(miss_w_score_text, text=str(miss_w_score))
                cv.itemconfig(notes_id[note[0]], fill="#a9e092")

def j(_):
    global miss_w_score, j_list
    if miss_w_state == 2:
        for note in j_list:
            if note[1] == 0 and 408 <= cv.coords(notes_id[note[0]])[1] <= 472:
                note[1] = 1
                miss_w_score += 10
                cv.itemconfig(miss_w_score_text, text=str(miss_w_score))
                cv.itemconfig(notes_id[note[0]], fill="#a9e092")

def k(_):
    global miss_w_score, k_list
    if miss_w_state == 2:
        for note in k_list:
            if note[1] == 0 and 408 <= cv.coords(notes_id[note[0]])[1] <= 472:
                note[1] = 1
                miss_w_score += 10
                cv.itemconfig(miss_w_score_text, text=str(miss_w_score))
                cv.itemconfig(notes_id[note[0]], fill="#a9e092")

def l(_):
    global miss_w_score, l_list
    if miss_w_state == 2:
        for note in l_list:
            if note[1] == 0 and 408 <= cv.coords(notes_id[note[0]])[1] <= 472:
                note[1] = 1
                miss_w_score += 10
                cv.itemconfig(miss_w_score_text, text=str(miss_w_score))
                cv.itemconfig(notes_id[note[0]], fill="#a9e092")

root.bind("<space>", space)
root.bind("f", f)
root.bind("g", g)
root.bind("h", h)
root.bind("j", j)
root.bind("k", k)
root.bind("l", l)
mister_c_input.bind("<Return>", enter)

menu()
root.mainloop()
