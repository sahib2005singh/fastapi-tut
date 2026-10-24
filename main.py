from fastapi import FastAPI, Path, HTTPException
import json
app = FastAPI()

def load_pokemon_data():
    with open("pokemonDB_dataset.json", "r") as f:
        data =  json.load(f)
        return data


@app.get("/")
def pokemon():
    return "Hii User, This is a service to give you the information about pokemons."


@app.get("/pokemon/{pokemon_name}")
def information(pokemon_name: str = Path(..., description="Enter name of the pokemon",example="Pikachu")):
    data = load_pokemon_data()
    if pokemon_name in data:
        return data[pokemon_name]
    else:
        raise HTTPException(status_code=404, detail="Pokemon Not Found")



