import requests


class Pokemon:

    def __init__(self, nombre):
        self.nombre = nombre
        self.propiedades = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}")
        self.respuesta = self.propiedades.json() if self.propiedades.status_code==200 else False
        if self.respuesta:
            continue:
        self.id=""
        self.tipo = ""
        self.altura = ""
        self.peso = ""
    def criatura(self):
        self.tipo = self.respuesta.get("id",[])
        self.altura = self.respuesta.get("height",[])
        self.peso = self.respuesta.get("weight",[])
        self.peso = self.respuesta.get("weight",[])
        print("Id: " + str(self.id))
        print("Tipo: " + str(self.tipo))
        print("Altura: " + str(self.altura))
        print("Peso: " + str(self.peso))
        
    def debilidades(self):
        
        tabla_tipos = {
            "Fire": {"Fire": 0.5, "Water": 0.5, "Grass": 2, "Electric": 1},  # Example of weaknesses and resistances of the Fire type
            "Water": {"Fire": 2, "Water": 0.5, "Grass": 0.5, "Electric": 1},  # Example of weaknesses and resistances of the Water type
            "Steel": {"Steel": 0.5, "Fighting": 2, "Fire": 1, "Water": 0.5, "Grass": 1, "Flying": 1, "Psychic": 1, "Fairy": 1, "Ground": 2},
            "Bug": {"Bug": 1, "Fighting": 0.5, "Flying": 2, "Fire": 0.5, "Grass": 2, "Poison": 0.5, "Rock": 2, "Fairy": 0.5},
            "Dragon": {"Dragon": 1, "Fairy": 0, "Ice": 2, "Dragon": 2, "Steel": 0.5},
            "Electric": {"Electric": 0.5, "Ground": 2},
            "Ghost": {"Ghost": 1, "Normal": 0, "Fighting": 0, "Ghost": 2, "Psychic": 2},
            "Fairy": {"Fairy": 1, "Poison": 0.5, "Steel": 0.5, "Fire": 0.5, "Fighting": 2},
            "Ice": {"Ice": 0.5, "Fire": 2, "Fighting": 1, "Rock": 1, "Steel": 0.5, "Fairy": 1},
            "Fighting": {"Fighting": 1, "Flying": 0.5, "Psychic": 0.5, "Fairy": 2, "Bug": 0.5, "Poison": 0.5, "Rock": 2},
            "Normal": {"Normal": 1, "Fighting": 2},
            "Grass": {"Grass": 0.5, "Fire": 0.5, "Flying": 0.5, "Ice": 2, "Poison": 0.5, "Ground": 2},
            "Psychic": {"Psychic": 1, "Bug": 2, "Ghost": 2, "Steel": 0.5},
            "Rock": {"Rock": 0.5, "Water": 2, "Grass": 2, "Fighting": 0.5, "Ground": 1, "Steel": 1, "Ice": 2},
            "Dark": {"Dark": 1, "Fighting": 0.5, "Bug": 1, "Fairy": 2, "Ghost": 0, "Psychic": 2},
            "Ground": {"Ground": 1, "Flying": 0.5, "Ice": 2, "Water": 2, "Grass": 0.5, "Steel": 2},
            "Poison": {"Poison": 0.5, "Ground": 0.5, "Psychic": 2, "Fairy": 0.5},
            "Flying": {"Flying": 1, "Electric": 0.5, "Rock": 0.5, "Ice": 2},
        }


        if self.respuesta.get(["types"][0]["type"]["name"]) in tabla_tipos:
            return tabla_tipos[self.respuesta.get(["types"][0]["type"]["name"])]
        else:
            return "Tipo de Pokémon no válido"

    def habilidades(self): 
        if self.respuesta:
            habilidades = self.respuesta.get("abilities", [])
            if habilidades:
                for habilidad in habilidades:
                    print(habilidad["ability"]["name"])
            

def menu_informacion_pokemon(Pokemon):
    print("1.- Habilidades")
    print("2.- Debilidades")
    print("3.- Propiedades")
    print("4.- Evoluciones")
    opcion = float(input("Introduce el numero de consulta"))
    if opcion == 1:
        Pokemon.habilidades()
    if opcion == 2:
        Pokemon.Debilidades()
    if opcion == 3:
        Pokemon.criatura()
        
        
    
    
# Ejemplo de uso

continuar = True
while continuar:
    nombrePokemon = input("Introduce el nombre de un Pokémon o 'salir' para terminar el programa > ")
    if(nombrePokemon.lower()== "salir"):
        continuar==False
    else:
        miPokemon = Pokemon(nombrePokemon)
        menu_informacion_pokemon(miPokemon)