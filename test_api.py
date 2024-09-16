import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = os.getenv("REPO_NAME")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

base_url = "https://api.github.com"


def create_repo():
    url = f"{base_url}/user/repos"
    payload = {
        "name": REPO_NAME,
        "description": "Тестовый репозиторий для автоматизации API",
        "private": False,
    }
    response = requests.post(url, json=payload, headers=headers)
    assert (
        response.status_code == 201
    ), f"Не удалось создать репозиторий: {response.status_code}. Ответ: {response.json()}"
    print(f"Репозиторий '{REPO_NAME}' успешно создан.")


def check_repo_exists():
    url = f"{base_url}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.get(url, headers=headers)
    assert (
        response.status_code == 200
    ), f"Репозиторий '{REPO_NAME}' не найден: {response.status_code}. Ответ: {response.json()}"
    print(f"Репозиторий '{REPO_NAME}' существует.")


def delete_repo():
    url = f"{base_url}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.delete(url, headers=headers)
    assert (
        response.status_code == 204
    ), f"Не удалось удалить репозиторий: {response.status_code}. Ответ: {response.json()}"
    print(f"Репозиторий '{REPO_NAME}' успешно удален.")


if __name__ == "__main__":
    create_repo()
    check_repo_exists()
    delete_repo()
