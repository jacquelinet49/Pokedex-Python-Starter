import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
# Add a language choice Feature and print the pokemons name based on the user input
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
# for data in range(len()):
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
                                           #Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

print(data)
language = input("What language do u want to use? type in all lowercase (english french japanese chinese)")
def find_pokemon():
        for pokemon in data:
               print(pokemon["name"][language])
find_pokemon()

x = input("What type of pokemon do u want?").capitalize()
def type():
        for pokemon in data:
                if x in pokemon["type"]:
                        print(pokemon["name"][language])
type()