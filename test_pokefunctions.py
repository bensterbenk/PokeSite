import requests
import random
from poke_list import PokeList

def test_all():
    poke_json_list = []
    for i in range(1, 20):
        pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(i))
        pokemon_json = pokemon.json()
        poke_json_list.append(pokemon_json)
    pokelist = PokeList("All Pokemon", poke_json_list)
    #test_pokelist
    assert isinstance(pokelist.pokemonList[0].name, str)
    assert isinstance(pokelist.pokemonList[0].id, int)
    assert isinstance(pokelist.pokemonList[0].types, list)
    #test_random
    assert isinstance(pokelist.random_pokemon(), int)
    assert isinstance(pokelist.pokemonList[pokelist.random_pokemon()].name, str)
    #test_pokesort
    testlist = pokelist
    testlist.pokesort()
    assert testlist.pokemonList[0].name == "beedrill"
    #test_pokefind
    pokelist.pokesort()
    assert pokelist.pokemonList[pokelist.pokefind("ivysaur")].name == "ivysaur"
    assert pokelist.pokemonList[pokelist.pokefind("squirtle")].name == "squirtle"
    assert pokelist.pokefind("abcd") == -1
    # test_schooled
    schooled_list = pokelist.schooled()
    intypes = False
    for poketype in schooled_list[1]:
        if schooled_list[2] == poketype:
            intypes = True
    assert intypes
    assert schooled_list[1][0] != schooled_list[1][1] or schooled_list[1][0] != schooled_list[1][2]
    #test_odd
    odd_list = pokelist.odd_one_out()
    assert pokelist.pokemonList[odd_list[0][0]].types == pokelist.pokemonList[odd_list[0][1]].types
    assert pokelist.pokemonList[odd_list[0][0]].types != pokelist.pokemonList[odd_list[1]].types


if __name__ == "__main__":
    test_all()
