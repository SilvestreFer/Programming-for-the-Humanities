import requests
from time import sleep

url = 'https://api.github.com/users/octocat'

def ver_info_usuario(usuario):
    response = requests.get(url)
    dados = response.json()
    print(f"Nome: {dados.get('name')}")
    print(f"Empresa: {dados.get('company')}")
    print(f"Localização: {dados.get('location')}")
    print(f"Bio: {dados.get('bio')}")
    print(f"Repositórios públicos: {dados.get('public_repos')}")
    print(f"Seguidores: {dados.get('followers')}")

ver_info_usuario(url)
