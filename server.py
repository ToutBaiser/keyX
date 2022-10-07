import random,string
from time import sleep
import requests
import os
from github import Github

# generate password
def generatePassword():
    return ''.join(random.choice(string.printable) for i in range(300))

def main():
    while(True):
        g = Github("key here")
        repo = g.get_repo("ToutBaiser/keyX")
        contents = repo.get_contents("key.nigger")
        commit = generatePassword()
        repo.update_file(contents.path, "Key Update", commit, contents.sha, branch="main")
        sleep(86400)
if __name__ == "__main__":
    main()
