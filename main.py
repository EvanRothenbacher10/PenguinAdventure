penguins = ["King", "Emperor", "Chinstrap", "Gentoo", "Little", "African", "Southern Rockhopper", "Macaroni"]
factOptions = ["Habitat", "Diet", "Appearance", "Conservation Status"]
import os
def clear():     os.system('cls' if os.name == 'nt' else 'clear')
clear()
def start(x):    pass
start(input("Hello! Welcome to Penguin Facts! What Penguin would you like to learn about?\n[ King, Emperor, Chinstrap, Gentoo, Little, African, Southern Rockhopper, Marcaroni ]\n"))
