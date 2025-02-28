''' Lógica de la puntuación del juego '''
import json
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game

def add_team_to_score(team:str, score:dict):
    ''' Agrega un equipo al diccionario de puntuación '''
    if team not in score:
        score[team] = {
            'G':0,
            'E':0,
            'P':0
        }

def scoring(torneo:list)->dict:
    ''' Puntuación de juegos'''
    tablero = {}
    for juego in torneo:
        equipo_local = juego["A"]["name"]
        equipo_visitante = juego["B"]["name"]
        if equipo_local not in tablero:
            add_team_to_score(equipo_local, tablero)
        if equipo_visitante not in tablero:
            add_team_to_score(equipo_visitante, tablero)
    for juego in torneo:
        equipo_local = juego["A"]["name"]
        equipo_visitante = juego["B"]["name"]
        goles_local = juego["score"][equipo_local]
        goles_visitante = juego["score"][equipo_visitante]
        if goles_local > goles_visitante:
            tablero[equipo_local]['G'] += 1
            tablero[equipo_visitante]['P'] += 1
        elif goles_local < goles_visitante:
            tablero[equipo_local]['P'] += 1
            tablero[equipo_visitante]['G'] += 1
        else:
            tablero[equipo_local]['E'] += 1
            tablero[equipo_visitante]['E'] += 1
    return tablero

def display_tablero(tablero:dict):
    ''' Muestra el tablero de puntuación '''
    print("----------------")
    for equipo, puntaje in tablero.items():
        print(f"{equipo}: {puntaje['G']}G {puntaje['E']}E {puntaje['P']}P")
    print("----------------")
    print("Tabla de posiciones")
    tabla = sorted(tablero.items(), key=lambda x: x[1]['G'], reverse=True)
    for i, (equipo, puntaje) in enumerate(tabla, 1):
        print(f"{i}. {equipo}: {puntaje['G']}G {puntaje['E']}E {puntaje['P']}P")

def json_to_game(json_game:dict)->Game:
    ''' Convierte un diccionario en un objeto Game '''
    A = Team(json_game['A']['name'], 
             Sport(json_game['A']['sport']['name'], 
                   json_game['A']['sport']['players'],
                   json_game['A']['sport']['league']), 
            [Athlete(x['name']) for x in json_game['A']['players']])
    B = Team(json_game['B']['name'],
             Sport(json_game['B']['sport']['name'],
                   json_game['B']['sport']['players'],
                   json_game['B']['sport']['league']),
            [Athlete(x['name']) for x in json_game['B']['players']])
    game = Game(A, B)
    game.score = json_game['score']
    return game

def json_to_tournament(torneo:dict)->list:
    ''' Convierte un torneo en una lista de juegos '''
    return [json_to_game(juego) for juego in torneo]

if __name__ == "__main__":
    archivo = "torneo.json"
    with open(archivo, "r") as f:
        torneo = json.load(f)
    #print(torneo)
    tournament = json_to_tournament(torneo)
    for game in tournament:
        game.play()
    torneo = [game.to_json() for game in tournament]
    tablero = scoring(torneo)
    #print(tablero)
    display_tablero(tablero)
