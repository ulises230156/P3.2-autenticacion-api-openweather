import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def consultar_clima():
    if not API_KEY or API_KEY == "tu_clave_de_openweather_aqui":
        print("Error: API Key no configurada correctamente en el archivo .env.")
        return

    ciudad = input("Ingrese el nombre de la ciudad: ").strip()
    if not ciudad:
        print("Error: Debe ingresar una ciudad válida.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 401:
            print("Error (401): API Key inválida o no activada.")
            return
        elif response.status_code == 404:
            print(f"Error (404): La ciudad '{ciudad}' no existe.")
            return

        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        descripcion = data["weather"][0]["description"].capitalize()
        nombre = data["name"]
        pais = data["sys"]["country"]

        print(f"\n--- Clima en {nombre}, {pais} ---")
        print(f"Temperatura actual: {temp}°C")
        print(f"Descripción: {descripcion}")

    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")

if __name__ == "__main__":
    consultar_clima()