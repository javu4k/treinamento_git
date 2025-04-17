import requests

def ola_mundo():
    response = requests.get("https://api.github.com")
    return f"Olá, turma! API Status: {response.status_code}"

if __name__ == "__main__":
    print(ola_mundo())
