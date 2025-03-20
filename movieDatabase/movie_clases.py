''' Clases del sistema de películas, actores y actrices'''
import csv
from hashlib import sha256
from datetime import datetime

class Actor:
    ''' Clase Actor'''
    def __init__(self,id_estrella,nombre,fecha_nacimiento,ciudad_nacimiento,url_imagen,username):
        self.id_estrella       = int(id_estrella)
        self.nombre            = nombre
        self.fecha_nacimiento  = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        self.ciudad_nacimiento = ciudad_nacimiento
        self.url_imagen        = url_imagen
        self.username          = username
    
    def to_dict(self):
        ''' Retorna un diccionario con los atributos del objeto'''
        return {
            'id_estrella': self.id_estrella,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento.strftime('%Y-%m-%d'),
            'ciudad_nacimiento': self.ciudad_nacimiento,
            'url_imagen': self.url_imagen,
            'username': self.username
        }
    def __str__(self):
        ''' Método para imprimir el objeto Actor'''
        return self.nombre
    
class Pelicula:
    ''' Clase Película'''
    def __init__(self, id_pelicula,titulo_pelicula,fecha_lanzamiento,url_poster):
        ''' Constructor de la clase Película'''
        self.id_pelicula       = int(id_pelicula)
        self.titulo_pelicula   = titulo_pelicula
        self.fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, '%Y-%m-%d')
        self.url_poster        = url_poster
    
    def to_dict(self):
        ''' Retorna un diccionario con los atributos del objeto Película'''
        return {
            'id_pelicula': self.id_pelicula,
            'titulo_pelicula': self.titulo_pelicula,
            'fecha_lanzamiento': self.fecha_lanzamiento.strftime('%Y-%m-%d'),
            'url_poster': self.url_poster
        }
    def __str__(self):
        ''' Método para imprimir el objeto Película'''
        return f'{self.titulo_pelicula} ({self.fecha_lanzamiento.year})'
    
class Relacion:
    ''' Clase Relación: Relación entre actores y películas'''
    def __init__(self,id_relacion,id_pelicula,id_estrella):
        ''' Constructor de la clase Relación'''
        self.id_relacion = int(id_relacion)
        self.id_pelicula = int(id_pelicula)  
        self.id_estrella = int(id_estrella)
    
    def to_dict(self):
        ''' Retorna un diccionario con los atributos del objeto Relación'''
        return {
            'id_relacion': self.id_relacion,
            'id_pelicula': self.id_pelicula,
            'id_estrella': self.id_estrella
        }

class User:
    ''' Clase User: Usuario del sistema'''
    def __init__(self,username,nombre_completo,email,password):
        ''' Constructor de la clase User'''
        self.username = username
        self.nombre_completo = nombre_completo
        self.email = email
        self.password = self.hash_password(password)
    
    def hash_password(self,password):
        ''' Método para encriptar la contraseña'''
        return sha256(password.encode()).hexdigest()
    
    def to_dict(self):
        ''' Retorna un diccionario con los atributos del objeto User'''
        return {
            'username': self.username,
            'nombre_completo': self.nombre_completo,
            'email': self.email,
            'password': self.password
        }
    
class SistemaCine:
    ''' Clase SistemaCine: Sistema de películas'''
    def __init__(self):
        ''' Constructor de la clase SistemaCine'''
        self.actores = {}
        self.peliculas = {}
        self.relaciones = {}
        self.usuarios = {}
        self.usuario_actual = None
        self.idx_actor = 0
        self.idx_pelicula = 0
        self.idx_relacion = 0
    
    def cargar_csv(self, archivo, clase):
        ''' Método para cargar datos desde un archivo CSV'''
        with open(archivo, mode='r', encoding='utf8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if clase == Actor:
                    actor = Actor(**row)
                    self.actores[actor.id_estrella] = actor
                elif clase == Pelicula:
                    pelicula = Pelicula(**row)
                    self.peliculas[pelicula.id_pelicula] = pelicula
                elif clase == Relacion:
                    relacion = Relacion(**row)
                    self.relaciones[relacion.id_relacion] = relacion
                elif clase == User:
                    user = User(**row)
                    self.usuarios[user.username] = user
        if clase == Actor:
            self.idx_actor = max(self.actores.keys()) if self.actores else 0
        elif clase == Pelicula:
            self.idx_pelicula = max(self.peliculas.keys()) if self.peliculas else 0
        elif clase == Relacion:
            self.idx_relacion = max(self.relaciones.keys()) if self.relaciones else 0
    
    def obtener_peliculas_por_actor(self, id_estrella):
        ''' Método para obtener las películas de un actor'''
        #ids_peliculas = []
        #for k,v in self.relaciones.items():
        #    print(k, v.id_pelicula, v.id_estrella)
        #    if v.id_estrella == id_estrella:
        #        ids_peliculas.append(v.id_pelicula)
        #print(ids_peliculas)
        ids_peliculas = [relacion.id_pelicula for relacion in self.relaciones.values() if relacion.id_estrella == id_estrella]
        
        return [self.peliculas[id_pelicula] for id_pelicula in ids_peliculas] 

if __name__ == '__main__':
    sistema = SistemaCine()
    sistema.cargar_csv('datos/movies_db - actores.csv', Actor)
    sistema.cargar_csv('datos/movies_db - peliculas.csv', Pelicula)
    sistema.cargar_csv('datos/movies_db - relacion.csv', Relacion)
    sistema.cargar_csv('datos/movies_db - users.csv', User)
    lista_peliculas = sistema.obtener_peliculas_por_actor(1)
    for pelicula in lista_peliculas:
        print(f"{pelicula.id_pelicula}:{pelicula.titulo_pelicula} ({pelicula.fecha_lanzamiento.year})")
    #print(sistema.actores)
    #print(sistema.peliculas)
    #print(sistema.relaciones)
    #print(sistema.usuarios)
    print("Listo!")