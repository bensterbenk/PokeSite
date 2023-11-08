import random

from pokemon import Pokemon


class PokeList:
    def __init__(self, list_name, poke_json_list):
        self.name = list_name
        self.pokemonList = []
        self.guessthat = ""
        self.guessthatscore = 0
        self.oddlist = ""
        self.schoollist = ""
        for poke_json in poke_json_list:
            new_pokemon = Pokemon(poke_json)
            self.pokemonList.append(new_pokemon)

    def __str__(self):
        if len(self.pokemonList) >= 1:
            the_string = self.name + "contains" + str(len(self.pokemonList)) + "Pokemon, their names are:"
            for pokemon in self.pokemonList:
                the_string += "\n" + pokemon.name
        else:
            the_string = self.name + "Contains no pokemon."
        return the_string

    def random_pokemon(self):
        # returns a random Pokemon index from the list.
        return random.randint(0, len(self.pokemonList)-1)

    def pokesort(self):
        def get_name(pokemon):
            return pokemon.name
        poke_list = sorted(self.pokemonList, key=get_name)
        self.pokemonList = poke_list
        pass

    def pokefind(self, pokemon_to_find):
        found = 1
        low_value = self.pokemonList[0].name
        low_index = 0
        high_value = self.pokemonList[len(self.pokemonList) - 1].name
        high_index = len(self.pokemonList) - 1
        the_index = -1
        while found == 1 and low_index < high_index:
            mid_value = self.pokemonList[int((high_index + low_index) / 2)].name
            mid_index = int((high_index + low_index) / 2)
            if pokemon_to_find == mid_value:
                the_index = mid_index
                found = 2
            if pokemon_to_find == low_value:
                the_index = low_index
                found = 2
            if pokemon_to_find == high_value:
                the_index = high_index
                found = 2
            else:
                if pokemon_to_find > mid_value:
                    low_index = mid_index + 1
                    low_value = self.pokemonList[low_index].name
                else:
                    high_index = mid_index - 1
                    high_value = self.pokemonList[high_index].name
        return the_index

    def odd_one_out(self):
        poke_random1 = self.random_pokemon()
        stop = False
        while not stop:
            poke_random2 = self.random_pokemon()
            if self.pokemonList[poke_random2].types == self.pokemonList[poke_random1].types:
                stop = True
        stop = False
        while not stop:
            poke_random3 = self.random_pokemon()
            if self.pokemonList[poke_random3].types != self.pokemonList[poke_random1].types:
                stop = True

        odd_list = [[poke_random1, poke_random2, poke_random3], poke_random3]
        return odd_list
        # return a list of indexes of 2 random pokemon with the same types and 1 random pokemon of different types

    def schooled(self):
        stop = False
        poke_index = self.random_pokemon()
        move1 = self.pokemonList[poke_index].knownmoves[random.randint(0, len(self.pokemonList[poke_index].knownmoves) - 1)]
        while not stop:
            ind = self.random_pokemon()
            move2 = self.pokemonList[ind].knownmoves[random.randint(0, len(self.pokemonList[ind].knownmoves) - 1)]
            if move2 not in self.pokemonList[poke_index].knownmoves:
                stop = True
        stop = False
        while not stop:
            ind = self.random_pokemon()
            move3 = self.pokemonList[ind].knownmoves[random.randint(0, len(self.pokemonList[ind].knownmoves) - 1)]
            if move3 not in self.pokemonList[poke_index].knownmoves:
                stop = True

        schooled_list = [poke_index, [move1, move2, move3], move1]
        return schooled_list

        # return a 2 item list containing a one random pokemon index
        # and a list of 3 moves, one of which the pokemon can learn
        # and the two which cannot be learned

