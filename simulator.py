from tkinter import *
from pokemon_data import *
from PIL import ImageTk, Image

gen1 = {
  "bulbasaur": 1,
  "ivysaur": 2,
  "venusaur": 3,
  "charmander": 4,
  "charmeleon": 5,
  "charizard": 6,
  "squirtle": 7,
  "wartortle": 8,
  "blastoise": 9,
  "caterpie": 10,
  "metapod": 11,
  "butterfree": 12,
  "weedle": 13,
  "kakuna": 14,
  "beedrill": 15,
  "pidgey": 16,
  "pidgeotto": 17,
  "pidgeot": 18,
  "rattata": 19,
  "raticate": 20,
  "spearow": 21,
  "fearow": 22,
  "ekans": 23,
  "arbok": 24,
  "pikachu": 25,
  "raichu": 26,
  "sandshrew": 27,
  "sandslash": 28,
  "nidoran": [29,32],
  "nidorina": 30,
  "nidoqueen": 31,
  "nidorino": 33,
  "nidoking": 34,
  "clefairy": 35,
  "clefable": 36,
  "vulpix": 37,
  "ninetales": 38,
  "jigglypuff": 39,
  "wigglytuff": 40,
  "zubat": 41,
  "golbat": 42,
  "oddish": 43,
  "gloom": 44,
  "vileplume": 45,
  "paras": 46,
  "parasect": 47,
  "venonat": 48,
  "venomoth": 49,
  "diglett": 50,
  "dugtrio": 51,
  "meowth": 52,
  "persian": 53,
  "psyduck": 54,
  "golduck": 55,
  "mankey": 56,
  "primeape": 57,
  "growlithe": 58,
  "arcanine": 59,
  "poliwag": 60,
  "poliwhirl": 61,
  "poliwrath": 62,
  "abra": 63,
  "kadabra": 64,
  "alakazam": 65,
  "machop": 66,
  "machoke": 67,
  "machamp": 68,
  "bellsprout": 69,
  "weepinbell": 70,
  "victreebel": 71,
  "tentacool": 72,
  "tentacruel": 73,
  "geodude": 74,
  "graveler": 75,
  "golem": 76,
  "ponyta": 77,
  "rapidash": 78,
  "slowpoke": 79,
  "slowbro": 80,
  "magnemite": 81,
  "magneton": 82,
  "farfetch'd": 83,
  "doduo": 84,
  "dodrio": 85,
  "seel": 86,
  "dewgong": 87,
  "grimer": 88,
  "muk": 89,
  "shellder": 90,
  "cloyster": 91,
  "gastly": 92,
  "haunter": 93,
  "gengar": 94,
  "onix": 95,
  "drowzee": 96,
  "hypno": 97,
  "krabby": 98,
  "kingler": 99,
  "voltorb": 100,
  "electrode": 101,
  "exeggcute": 102,
  "exeggutor": 103,
  "cubone": 104,
  "marowak": 105,
  "hitmonlee": 106,
  "hitmonchan": 107,
  "lickitung": 108,
  "koffing": 109,
  "weezing": 110,
  "rhyhorn": 111,
  "rhydon": 112,
  "chansey": 113,
  "tangela": 114,
  "kangaskhan": 115,
  "horsea": 116,
  "seadra": 117,
  "goldeen": 118,
  "seaking": 119,
  "staryu": 120,
  "starmie": 121,
  "mr mime": 122,
  "scyther": 123,
  "jynx": 124,
  "electabuzz": 125,
  "magmar": 126,
  "pinsir": 127,
  "tauros": 128,
  "magikarp": 129,
  "gyarados": 130,
  "lapras": 131,
  "ditto": 132,
  "eevee": 133,
  "vaporeon": 134,
  "jolteon": 135,
  "flareon": 136,
  "porygon": 137,
  "omanyte": 138,
  "omastar": 139,
  "kabuto": 140,
  "kabutops": 141,
  "aerodactyl": 142,
  "snorlax": 143,
  "articuno": 144,
  "zapdos": 145,
  "moltres": 146,
  "dratini": 147,
  "dragonair": 148,
  "dragonite": 149,
  "mewtwo": 150,
  "mew": 151
}

dx_opp = 20
dy_opp = 6.4
dx_curr = 20
dy_curr = 6.4

def opp_move1():
    x_opp,y_opp = battle_canvas.coords(opponent_pokemon_image)
    x_curr,y_curr = battle_canvas.coords(curr_pokemon_image)

    if x_opp >=200:
      battle_canvas.move(opponent_pokemon_image,-dx_opp,dy_opp)
    else:
       opp_move2()
       return
    battle_canvas.after(2,opp_move1)

def opp_move2():
    x_opp,y_opp = battle_canvas.coords(opponent_pokemon_image)
    x_curr,y_curr = battle_canvas.coords(curr_pokemon_image)

    if x_opp >=100:
      battle_canvas.move(opponent_pokemon_image,-dx_opp,dy_opp)
      battle_canvas.move(curr_pokemon_image,-dx_curr,dy_curr)
    else:
       opp_move3()
       return
    battle_canvas.after(2,opp_move2)

def opp_move3():
    x_opp,y_opp = battle_canvas.coords(opponent_pokemon_image)
    x_curr,y_curr = battle_canvas.coords(curr_pokemon_image)

    if x_opp < init_opp_x:
      battle_canvas.move(opponent_pokemon_image,dx_opp,-dy_opp)
    if x_curr < init_curr_x:
       battle_canvas.move(curr_pokemon_image,dx_curr,-dy_curr)

    if x_opp >= init_opp_x and x_curr >= init_curr_x:
       return
    
    battle_canvas.after(2,opp_move3)


def curr_move1():
    x_opp,y_opp = battle_canvas.coords(opponent_pokemon_image)
    x_curr,y_curr = battle_canvas.coords(curr_pokemon_image)

    if x_curr <=700:
      battle_canvas.move(curr_pokemon_image,dx_opp,-dy_opp)
    else:
       curr_move2()
       return
    battle_canvas.after(2,curr_move1)

def curr_move2():
    x_opp,y_opp = battle_canvas.coords(opponent_pokemon_image)
    x_curr,y_curr = battle_canvas.coords(curr_pokemon_image)

    if x_curr <=800:
      battle_canvas.move(opponent_pokemon_image,dx_opp,-dy_opp)
      battle_canvas.move(curr_pokemon_image,dx_curr,-dy_curr)
    else:
       curr_move3()
       return
    battle_canvas.after(2,curr_move2)

def curr_move3():
    x_opp,y_opp = battle_canvas.coords(opponent_pokemon_image)
    x_curr,y_curr = battle_canvas.coords(curr_pokemon_image)

    if x_opp > init_opp_x:
      battle_canvas.move(opponent_pokemon_image,-dx_opp,dy_opp)
    if x_curr > init_curr_x:
       battle_canvas.move(curr_pokemon_image,-dx_curr,dy_curr)

    if x_opp <= init_opp_x and x_curr <= init_curr_x:
       return
    
    battle_canvas.after(2,curr_move3)

def get_key(index):
    zeros = 4-len(str(index))
    key = "0"*zeros + str(index)
    return key


opponent_pokemon = 150
curr_pokemon = 142

root = Tk()
root.geometry('1000x700')

battle_canvas = Canvas(root,bg='lightblue',width=1000,height=400)
battle_canvas.grid(row=0,column=0)


opp_img = Image.open(f"sprites/{get_key(opponent_pokemon)}.png")
opp_img = opp_img.resize((120, 120), Image.LANCZOS)
opp_img = ImageTk.PhotoImage(opp_img)

curr_img = Image.open(f"sprites/{get_key(curr_pokemon)}.png")
curr_img = curr_img.resize((120, 120), Image.LANCZOS)
curr_img = ImageTk.PhotoImage(curr_img)

opp_health = 90
curr_health = 20

opp_hp1 = battle_canvas.create_rectangle(800,25,800+opp_health,35,fill='lightgreen',outline='')
opp_hp2 = battle_canvas.create_rectangle(800+opp_health,25,900,35,fill='red',outline='')

curr_hp1 = battle_canvas.create_rectangle(100,225,100+curr_health,235,fill='lightgreen',outline='')
curr_hp2 = battle_canvas.create_rectangle(100+curr_health,225,200,235,fill='red',outline='')

init_opp_x = 850
init_curr_x = 150

opponent_pokemon_image = battle_canvas.create_image((init_opp_x,100),image=opp_img)
curr_pokemon_image = battle_canvas.create_image((init_curr_x,300),image=curr_img)

moves_frame = Frame(root,bg='lightgreen',height=200,width=1000)
moves_frame.pack_propagate(False)
moves_frame.grid(row=1,column=0)

move1 = Button(moves_frame,text='move1',command=opp_move1)
move1.grid(row=0,column=0,padx=10,pady=10)
move2 = Button(moves_frame,text='move2',command=curr_move1)
move2.grid(row=0,column=1,padx=10,pady=10)
move3 = Button(moves_frame,text='move3')
move3.grid(row=0,column=2,padx=10,pady=10)
move4 = Button(moves_frame,text='move4')
move4.grid(row=0,column=3,padx=10,pady=10)


root.mainloop()