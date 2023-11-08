
class Pokemon:
    def __init__(self, poke_json):
        self.name = poke_json["name"]
        self.id = poke_json["id"]
        self.height = poke_json["height"]
        self.weight = poke_json["weight"]
        self.sprite = poke_json['sprites']['front_default']
        self.types = []
        for type in poke_json["types"]:
            self.types.append(type["type"]["name"])
        self.knownmoves = []
        for move in poke_json["moves"]:
            self.knownmoves.append(move['move']['name'])

    def __str__(self):
        the_string = self.name + ", ID" + self.id
        return the_string





