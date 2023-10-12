import requests
import json
import local_settings as settings #берем переменные (хост и токен) из local_settings

# создание покемона
response_addpoke = requests.post(
    f'{settings.host}/pokemons',
    json = {
        "name":"python_child",
        "photo":"https://dolnikov.ru/pokemons/albums/925.png"
    },
    headers = {
        "Content-Type":"application/json",
        "trainer_token":settings.token
    }
)
print(response_addpoke.json())
mypoke = response_addpoke.json()['id'] # запись id покемона в переменную
print(mypoke)

# смена имени
response_rename = requests.put(
    f'{settings.host}/pokemons',
    json = {"pokemon_id":mypoke,
        "name":"python_child_renamed",
        "photo":"https://dolnikov.ru/pokemons/albums/925.png"
    },
    headers = {
        "Content-Type":"application/json",
        "trainer_token":settings.token
    }
)
print(response_rename.json())

# добавление покемона в покебол
response_inpokeball = requests.post(
    f'{settings.host}/trainers/add_pokeball',
    json = {
        "pokemon_id": mypoke
    },
    headers = {
        "Content-Type":"application/json",
        "trainer_token":settings.token
    }
)
print(response_inpokeball.json()['message'])