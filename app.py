import requests

APP_URL = "github.com"
CURRENT_VERSION = "1.0.0"

def updateApplication():
    print('Running update!')

def checkForUpdate(url, version):
    REPO_CURRENT_VERSION = "1.0.0"
    print(f'Current version from repo: {REPO_CURRENT_VERSION}')
    if version != REPO_CURRENT_VERSION:
        print(f'Versions do not match!\nOur version: {version}\nRepo version {REPO_CURRENT_VERSION}')
        updateApplication()
    else:
        print('Nothing to do!')


if __name__ == '__main__':
    checkForUpdate(APP_URL,CURRENT_VERSION)



