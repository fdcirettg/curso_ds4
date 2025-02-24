"""
    Clase Team: Equipo
"""
from Athlete import Athlete
from Sport import Sport
class Team:
    """ Clase para representar un equipo """
    def __init__(self, name:str, sport:Sport, players:list):
        """ Constructor de la clase Team """
        self.name = name
        self.sport = sport
        self.players = players
    
    def __str__(self):
        """ Método para representar la clase como string """
        return f"Team: {self.name}, {self.sport}, {self.players}"
    
    def __repr__(self):
        """ Método para representar la clase como string """
        return f"Team(name='{self.name}', sport={repr(self.sport)}, players={self.players})"
    
    def to_json(self)->dict:
        """ Método para representar la clase como diccionario """
        return {"name":self.name, "sport":self.sport.to_json(), "players":[p.to_json() for p in self.players]}

if __name__ == "__main__":
    a1 = Athlete("Michale Jordan")
    a2 = Athlete("Kobe Bryant")
    a3 = Athlete("Lebron James")
    a4 = Athlete("Stephen Curry")
    a5 = Athlete("Shaquille O'Neal")
    s = Sport("Basketball", 5, "NBA")
    lakers = Team("Los Angeles Lakers", s, [a1, a2, a3, a4, a5])
    print(lakers)
    print(repr(lakers))
    print(lakers.to_json())
    