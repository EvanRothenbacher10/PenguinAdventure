import os
penguins = [["King penguins breed on the Subantarctic islands at the northern reaches of Antarctica, South Georgia, and other temperate islands of the region. King penguins also live on Macquarie Island in the Southern Ocean.", "King penguins eat various species of small fish, squid, and krill. Fish constitute roughly 80 percent of their diet, except in winter months of July and August, when they make up only around 30%.[19] Lanternfish are the main fish taken", "The king penguin (Aptenodytes patagonicus) is the second largest species of penguin, smaller, but somewhat similar in appearance to the emperor penguin. There are two subspecies: A. p. patagonicus and A. p. halli; patagonicus", "King penguins primarily feed at the Antarctic Convergence, which provides 80 percent of their food biomass. King penguins currently travel 300 to 500 km over a course of over a week to complete the journey. However, ocean warming could easily move these fronts further away from breeding grounds."], [" percent of their food biomass. King penguins currently travel 300 to 500 km over a course of over a week to complete the journey. However, ocean warming could easily move these fronts further away from breeding grounds.", "Emperors feed mostly on Antarctic silverfish as well as other species of fish, krill (like Will & Bill from Happy Feet) and some squid.", "The emperor penguin (Aptenodytes forsteri) is the tallest and heaviest of all living penguin species and is endemic to Antarctica. The male and female are similar in plumage and size, reaching 100 cm (39 in) in length and weighing from 22 to 45 kg (49 to 99 lb).", "The primary causes for an increased risk of species endangerment are declining food availability, due to the effects of climate change and industrial fisheries on the crustacean and fish populations. "], ["Chinstrap fact1", "Chinstrap fact2", "Chinstrap fact3", "Chinstrap fact4"], ["Gentoo fact1", "Gentoo fact2", "Gentoo fact3", "Gentoo fact4"], ["Little fact1", "Little fact2", "Little fact3", "Little fact4"], ["African fact1", "African fact2", "African fact3", "African fact4"], ["Southern RockHopper fact1", "Southern RockHopper fact2", "Southern RockHopper fact3", "Southern RockHopper fact4"], ["Macaronifact1", "Macaronifact2", "Macaronifact3", "Macaronifact4"]]
os.system('cls' if os.name == 'nt' else 'clear')
x = input("Hello! Welcome to Penguin Facts! What Penguin would you like to learn about?\n[ 0. King, 1. Emperor, 2. Chinstrap, 3. Gentoo, 4. Little, 5. African, 6. Southern Rockhopper, 7. Marcaroni ]\n")
os.system('cls' if os.name == 'nt' else 'clear')
x2 = input("What would you like to learn about your penguin?\n[ 0. Habitat, 1. Diet, 2. Appearance, 3. Conservation Status ]\n")
os.system('cls' if os.name == 'nt' else 'clear')
print(penguins[int(x)][int(x2)])