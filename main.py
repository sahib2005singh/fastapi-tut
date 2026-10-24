from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get("/sort")
def sort_pokemon(sort_by: str = Query(..., description= "Enter the parameter you want to sort the data by",example = "Base Exp"), order: str = Query(..., description= "Order of sorting", example = "ASC")):
    valid_fields_sorting = ['Base Exp', 'Speed Base', 'Defense Base', 'Attack Base']
    valid_fields_order = ["ASC", "DESC"]
    if sort_by not in valid_fields_sorting:
        raise HTTPException(status_code = 400, detail = f"Choose from {valid_fields_sorting}")
    if order not in valid_fields_order:
        raise HTTPException(status_code = 400, detail = f"Choose from {valid_fields_order}")
    data = load_pokemon_data()
    sort_order = True if order == "DESC" else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data