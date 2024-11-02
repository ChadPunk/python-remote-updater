import requests
import yaml

APP_URL = "https://raw.githubusercontent.com/ChadPunk/python-remote-updater/refs/heads/main/settings.yaml"
CURRENT_VERSION = "1.0.0"

def updateApplication():
    print('Running update!')

def checkForUpdate(url, version):
    try:
        response = requests.get(url)
        response.raise_for_status()
        settings = yaml.safe_load(response.text)
        REPO_CURRENT_VERSION = settings['version']
        print(f'Current version from repo: {REPO_CURRENT_VERSION}')
        
        if version != REPO_CURRENT_VERSION:
            print(f'Versions do not match!\nOur version: {version}\nRepo version: {REPO_CURRENT_VERSION}')
            updateApplication()
        else:
            print('Nothing to do!')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching update information: {e}")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")

if __name__ == '__main__':
    checkForUpdate(APP_URL, CURRENT_VERSION)
