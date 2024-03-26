import requests

class Pokemon:

    def __init__(self, nombre):
        self.nombre = nombre
        self.propiedades = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}")
        self.respuesta = self.respuesta.json() if self.respuesta==200 else False

        
    
# def obtener_informacion_pokemon(self):
#     url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
#     respuesta = requests.get(url)
#     return True
#     if respuesta.status_code == 200:
#         datos_pokemon = respuesta.json()
#         nombre = datos_pokemon['name']
#         id = datos_pokemon['id']
#         tipos = [tipo['type']['name'] for tipo in datos_pokemon['types']]
        
#         print(f"Nombre: {nombre}")
#         print(f"ID: {id}")
#         print("Tipos:")
#         for tipo in tipos:
#             print(f"- {tipo}")
#     else:
#         print(f"Error: No se pudo obtener la información del Pokémon {nombre_pokemon}")


    def obtener_habilidades_pokemon(self):
        if(self.respuesta!=False):
            for h in self.propiedades:
                print()
            

    def menu_informacion_pokemon():
        print("1.- Habilidades")
        print("2.- Debilidades")
        print("3.- Propiedades")
        print("4.- Evoluciones")
# Ejemplo de uso
miPokemon = input("Introduce el nombre de un Pokémon: ")

obtener_informacion_pokemon(nombre_pokemon)
