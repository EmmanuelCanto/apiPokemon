import requests

# Elige un Pokémon
pokemon_name = "Pikachu"

# Crea la URL de la API
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name

# Haz una llamada a la API
response = requests.get(url)

# Si la llamada a la API es exitosa, analiza la respuesta
if response.status_code == 200:
    data = response.json()
    # Imprime el nombre del Pokémon
    print("Nombre:", data["name"])

    # Imprime los tipos del Pokémon
    print("Tipos:", data["types"])

    # Imprime las habilidades del Pokémon
    print("Habilidades:", data["abilities"])

    # Imprime las estadísticas del Pokémon
    print("Estadísticas:", data["stats"])

else:
    # Imprime un mensaje de error
    print("Error:", response.status_code)
