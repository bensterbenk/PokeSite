import requests
import random
import time
from poke_list import PokeList
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return HOME_HTML


HOME_HTML = """
 <html><body>
     <h2>Home</h2>
     <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png" alt="Italian Trulli">
     <form action="/pokesearch">
         <input type='submit' value='PokeSearch!'>
     </form>
     <form action="/pokegame">
         <input type='submit' value='PokeGame!'>
     </form>
 </body></html>"""


@app.route('/pokesearch')
def pokesearch():
    search = request.args.get('search', '')
    message = ""
    if search != "":
        pokeindex = pokelist.pokefind(search.lower())
        if pokeindex != -1:
            message = "Pokemon Found!"
            pokemon = pokelist.pokemonList[pokeindex]
            sprite = pokemon.sprite
            name = pokemon.name
            id = pokemon.id
            height = pokemon.height
            weight = pokemon.weight
            types = pokemon.types
            moves = pokemon.knownmoves
        else:
            sprite = "https://articles.pokebattler.com/wp-content/uploads/2018/08/pokedex-kanto-1.jpg"
            message = "Pokemon Not Found"
            name = "unknown"
            id = "unknown"
            height = "unknown"
            weight = "unknown"
            types = "unknown"
            moves = "unknown"
    else:
        sprite = "https://articles.pokebattler.com/wp-content/uploads/2018/08/pokedex-kanto-1.jpg"
        message = "Enter in a pokemon name to bring up it's data!"
        name = "unknown"
        id = "unknown"
        height = "unknown"
        weight = "unknown"
        types = "unknown"
        moves = "unknown"

    return POKESEARCH_HTML.format(message, sprite, name, id, height, weight, types, moves)


POKESEARCH_HTML = """
 <html><body>
     <h2>PokeSearch</h2>
     <form action="/pokesearch">
         Search for a pokemon: <input type='text' name='search'><br>
         <input type='submit' value='Search'>
     </form>
     <b>{0}<br>
     <img src="{1}" alt="Randompokemon" width="500" height="500"><br>
     Name: {2}<br>
     ID: {3}<br>
     Height: {4}<br>
     Weight: {5}<br>
     Types: {6}<br>
     Moves: {7}<br>
     <form action="/">
         <input type='submit' value='Home'>
     </form>
     
 </body></html>"""


@app.route('/pokegame')
def pokegame():
    return POKEGAME_HTML


POKEGAME_HTML = """
 <html><body>
     <h2>Pokegame</h2>
     <form action="/pokeimage">
         <input type='submit' value='Guess That Pokemon!'>
     </form>
     <form action="/pokeodd">
         <input type='submit' value='Odd One Out!!'>
     </form>
     <form action="/pokeschooled">
         <input type='submit' value='Schooled!'>
     </form>
     <form action="/">
         <input type='submit' value='Home'>
     </form>
 </body></html>"""


@app.route('/pokeimage')
def pokeimage():
    guess_ind = pokelist.random_pokemon()
    if pokelist.guessthat == "":
        pokelist.guessthat = pokelist.pokemonList[guess_ind]
    name = pokelist.guessthat.name
    sprite = pokelist.guessthat.sprite
    guess = request.args.get('guess', '')
    button = "Submit Guess"
    if guess == "":
        message = "Guess this Pokemon!"
    else:
        if guess.lower() == name:
            message = "Correct! the Pokemon's name was " + name + "\n"
            pokelist.guessthat = ""
            button = "Guess Again"
            pokelist.guessthatscore += 1
        else:
            message = "Incorrect"

    return POKEIMAGE_HTML.format(sprite, message, button, pokelist.guessthatscore)


POKEIMAGE_HTML = """
 <html><body>
     <h2>Guess That Pokemon!</h2>
     <img src="{0}" alt="Randompokemon" width="500" height="500">
     <form action="/pokeimage">
         Guess the pokemon! <input type='text' name='guess'><br>
         <input type='submit' value='{2}'>
     </form>
     <b>{1}<b><br>
     <b>The Score Is: {3} <b><br>
     <form action="/">
         <input type='submit' value='Home'>
     </form>
 </body></html>"""


@app.route('/pokeodd')
def pokeodd():
    #Show 3 random Pokemon and try to guess which one is the one with a different type
    guess = request.args.get('guess', '')
    message = "Choose an answer..."
    button = "Guess!"
    if pokelist.oddlist == "":
        pokelist.oddlist = pokelist.odd_one_out()
        random.shuffle(pokelist.oddlist[0])
    answers = pokelist.oddlist[0]
    sprite1 = pokelist.pokemonList[answers[0]].sprite
    sprite2 = pokelist.pokemonList[answers[1]].sprite
    sprite3 = pokelist.pokemonList[answers[2]].sprite
    if guess != "":
        if pokelist.oddlist[0][int(guess)-1] == pokelist.oddlist[1]:
            message = "Correct Answer!"
            pokelist.oddlist = ""
            button = "Play Again!"
        else:
            message = "Incorrect Answer!"
    return POKEODD_HTML.format(sprite1, sprite2, sprite3, message, button)


POKEODD_HTML = """
 <html><body>
     <h2>Odd One Out!</h2>
     Which One Of These Pokemon has a different type than the other two?<br>
     <img src="{0}" alt="Randompokemon" width="250" height="250">
     <img src="{1}" alt="Randompokemon" width="250" height="250">
     <img src="{2}" alt="Randompokemon" width="250" height="250"><br>
     {3}
     <form action="/pokeodd">
         Choose 1, 2, or 3 <input type='text' name='guess'>
         <input type='submit' value='{4}'>
     </form>
     <form action="/">
         <input type='submit' value='Home'>
     </form>
 </body></html>"""


@app.route('/pokeschooled')
def pokeschooled():
    #Show a pokemon and 3 moves, and the player guess which one the pokemon can learn
    guess = request.args.get('guess', '')
    message = "Guess which move this pokemon can learn!"
    button = "Guess!"
    if pokelist.schoollist == "":
        pokelist.schoollist = pokelist.schooled()
        random.shuffle(pokelist.schoollist[1])
    answers = pokelist.schoollist[1]
    answer1 = answers[0]
    answer2 = answers[1]
    answer3 = answers[2]
    sprite = pokelist.pokemonList[pokelist.schoollist[0]].sprite
    if guess != "":
        if pokelist.schoollist[1][int(guess)-1] == pokelist.schoollist[2]:
            message = "Correct Answer!"
            button = "Play Again!!"
            pokelist.schoollist = ""
        else:
            message = "Incorrect Answer!"

    return POKESCHOOLED_HTML.format(answer1, answer2, answer3, sprite, message, button)


POKESCHOOLED_HTML = """
 <html><body>
     <h2>Schooled</h2>
     <img src="{3}" alt="Randompokemon" width="250" height="250"><br>
     1: {0}<br>
     2: {1}<br>
     3: {2}<br>
     {4}
     <form action="/pokeschooled">
         Choose 1, 2, or 3 <input type='text' name='guess'>
         <input type='submit' value='{5}'>
     </form>
     <form action="/">
         <input type='submit' value='Home'>
     </form>
 </body></html>"""

if __name__ == "__main__":
    amount_of_pokemon = 151
    poke_json_list = []
    start = time.process_time_ns()
    for i in range(1, amount_of_pokemon+1):
        pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(i))
        pokemon_json = pokemon.json()
        poke_json_list.append(pokemon_json)
        print(i)
    stop = time.process_time_ns()
    print(stop - start)
    print(poke_json_list[1]['name'])
    pokelist = PokeList("All Pokemon", poke_json_list)
    for i in range(10):
        print(pokelist.pokemonList[i].name)
    print("\n")
    pokelist.pokesort()
    for i in range(10):
        print(pokelist.pokemonList[i].name)
    print("\n")
    print(pokelist.pokemonList[pokelist.pokefind("ivysaur")].name)
    print(pokelist.pokemonList[4].types)
    odd_list = pokelist.odd_one_out()
    print(odd_list)
    for i in odd_list[0]:
        print(pokelist.pokemonList[i].name)
        print(pokelist.pokemonList[i].types)
    schooled_list = pokelist.schooled()
    print(schooled_list)
    print(pokelist.pokemonList[schooled_list[0]].knownmoves)

    # Launch the Flask dev server
    app.run(host="localhost", port=5001, debug=True)


