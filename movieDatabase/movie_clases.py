''' Clases del sistema de películas, actores y actrices'''
import csv
from hashlib import sha256
from datetime import datetime

class Actor:
    ''' Clase Actor'''
    def __init__(self,id_estrella,nombre,fecha_nacimiento,ciudad_nacimiento,url_imagen,username):
        self.id_estrella       = id_estrella
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
    
class Pelicula:
    ''' Clase Película'''
    def __init__(self, id_pelicula,titulo_pelicula,fecha_lanzamiento,url_poster):
        ''' Constructor de la clase Película'''
        self.id_pelicula       = id_pelicula
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
    
class Relacion:
    ''' Clase Relación: Relación entre actores y películas'''
    def __init__(self,id_relacion,id_pelicula,id_estrella):
        ''' Constructor de la clase Relación'''
        self.id_relacion = id_relacion
        self.id_pelicula = id_pelicula  
        self.id_estrella = id_estrella
    
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
        self.actores = []
        self.peliculas = []
        self.relaciones = []
        self.usuarios = []
        self.usuario_actual = None
    
    def cargar_csv(self, archivo, clase):
        ''' Método para cargar datos desde un archivo CSV'''
        with open(archivo, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if clase == Actor:
                    self.actores.append(Actor(**row))
                elif clase == Pelicula:
                    self.peliculas.append(Pelicula(**row))
                elif clase == Relacion:
                    self.relaciones.append(Relacion(**row))
                elif clase == User:
                    self.usuarios.append(User(**row))

if __name__ == '__main__':
    sistema = SistemaCine()
    sistema.cargar_csv('datos/movies_db - actores.csv', Actor)
    sistema.cargar_csv('datos/movies_db - peliculas.csv', Pelicula)
    sistema.cargar_csv('datos/movies_db - relacion.csv', Relacion)
    sistema.cargar_csv('datos/movies_db - users.csv', User)
    print(sistema.actores)
    print(sistema.peliculas)
    print(sistema.relaciones)
    print(sistema.usuarios)