import requests
import json

class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.propiedades = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}")
        try:
            self.respuesta = self.propiedades.json()
            if len(self.respuesta) == 0:
                print("¡No se encontró información del Pokémon!")
                self.encontrado = False
            else:
                print("¡Se encontró la información del Pokémon!")
                self.id = self.respuesta["id"]
                self.altura = self.respuesta["height"]
                self.peso = self.respuesta["weight"]
                self.tipo = self.respuesta["types"][0]["type"]["name"]
                self.encontrado = True
        except AttributeError:
            print("¡No se encontró información del Pokémon!")
            self.encontrado = False
            
    def encontrado(self):
        return self.encontrado
    
    def criaturas(self):
        if self.respuesta:
            print("Id:", self.id)
            print("Tipo:", self.tipo)
            print("Altura:", self.altura)
            print("Peso:", self.peso)
            
        else:
            print("No se encontraron propiedades para este Pokémon.")
        
    def debilidades(self):
        
        tabla_tipos = {
            "fire": {"fire": 0.5, "water": 0.5, "grass": 2, "electric": 1},  
            "water": {"fire": 2, "water": 0.5, "grass": 0.5, "electric": 1},
            "steel": {"steel": 0.5, "fighting": 2, "fire": 1, "water": 0.5, "grass": 1, "flying": 1, "psychic": 1, "fairy": 1, "ground": 2},
            "bug": {"bug": 1, "fighting": 0.5, "flying": 2, "fire": 0.5, "grass": 2, "poison": 0.5, "rock": 2, "fairy": 0.5},
            "dragon": {"dragon": 1, "fairy": 0, "ice": 2, "dragon": 2, "steel": 0.5},
            "electric": {"electric": 0.5, "ground": 2},
            "ghost": {"ghost": 1, "normal": 0, "fighting": 0, "ghost": 2, "psychic": 2},
            "fairy": {"fairy": 1, "poison": 0.5, "steel": 0.5, "fire": 0.5, "fighting": 2},
            "ice": {"ice": 0.5, "fire": 2, "fighting": 1, "rock": 1, "steel": 0.5, "fairy": 1},
            "fighting": {"fighting": 1, "flying": 0.5, "psychic": 0.5, "fairy": 2, "bug": 0.5, "poison": 0.5, "rock": 2},
            "normal": {"normal": 1, "fighting": 2},
            "grass": {"grass": 0.5, "fire": 0.5, "flying": 0.5, "ice": 2, "poison": 0.5, "ground": 2},
            "psychic": {"psychic": 1, "bug": 2, "ghost": 2, "steel": 0.5},
            "rock": {"rock": 0.5, "water": 2, "grass": 2, "fighting": 0.5, "ground": 1, "steel": 1, "ice": 2},
            "dark": {"dark": 1, "fighting": 0.5, "bug": 1, "fairy": 2, "ghost": 0, "psychic": 2},
            "ground": {"ground": 1, "flying": 0.5, "ice": 2, "water": 2, "grass": 0.5, "steel": 2},
            "poison": {"poison": 0.5, "ground": 0.5, "psychic": 2, "fairy": 0.5},
            "flying": {"flying": 1, "electric": 0.5, "rock": 0.5, "ice": 2},
        }


        if self.tipo in tabla_tipos:
            print("Debilidades del tipo", self.tipo)
            for tipo, factor in tabla_tipos[self.tipo].items():
                print(f"{tipo}: {factor}")
        else:
            print("Tipo de Pokémon no válido")

    def habilidades(self): 
        if self.respuesta:
            habilidades = self.respuesta.get("abilities", [])
            if habilidades:
                print("Habilidades:")
                for habilidad in habilidades:
                    print(habilidad["ability"]["name"])

   
    def evoluciones(self):
        query_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.nombre.lower()}")
        if query_pokemon.status_code == 200:
            json_evoluciones = requests.get(query_pokemon.json()["evolution_chain"]["url"])

            evoluciones = []

            def obtener_recursivo(chain):
                if "species" in chain:
                    evoluciones.append(chain["species"]["name"])
                    print(chain["species"]["name"])
                if "evolves_to" in chain and chain["evolves_to"]:
                    for evolucion in chain["evolves_to"]:
                        obtener_recursivo(evolucion)

            if "chain" in json_evoluciones.json():
                print("Evoluciones:")
                obtener_recursivo(json_evoluciones.json()["chain"])


        else:
            print("No se pudieron obtener las evoluciones de este Pokémon.")


def menu_informacion_pokemon(pokemon):
    print("1.- Habilidades")
    print("2.- Debilidades")
    print("3.- Propiedades")
    print("4.- Evoluciones")
    print("5.- Otro pokemon")
    opcion = input("Introduce el número de consulta: ")
    if opcion == "1":
        pokemon.habilidades()
    elif opcion == "2":
        pokemon.debilidades()
    elif opcion == "3":
        pokemon.criaturas()
    elif opcion == "4":
        pokemon.evoluciones()
    elif opcion == "5":
        return False
    else:
        print("Opción no válida.")
        
    return True

continuar = True
while continuar:
    nombre_pokemon = input("Introduce el nombre de un Pokémon o 'salir' para terminar el programa: ")
    if nombre_pokemon.lower() == "salir":
        continuar = False
    else:
        mismoPokemon = True
        while mismoPokemon:
            mi_pokemon = Pokemon(nombre_pokemon)
            mismoPokemon = mi_pokemon.encontrado
            if mismoPokemon:
                print("¡Se encontró la información del Pokémon!")
                mismoPokemon = menu_informacion_pokemon(mi_pokemon)
            else:
                print("No se pudo encontrar información para el Pokémon ingresado.")

            
            
