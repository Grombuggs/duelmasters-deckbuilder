from bs4 import BeautifulSoup
import requests
import pathlib
import subprocess

def antifandomize():
    with open("dm01Img", 'r') as f:
        lines = [line.replace('fandom', 'antifandom') for line in f]
    with open ("dm01Img, 'w") as f:
        f.write(''.join(lines))
        f.close()

    with open("dm02Img", 'r') as f:
        lines = [line.replace('fandom', 'antifandom') for line in f]
    with open ("dm02Img, 'w") as f:
        f.write(''.join(lines))
        f.close()

URL = "https://duelmasters.fandom.com/wiki/DM-01_Base_Set_Gallery_(TCG)"
page = requests.get(URL)

with open("dm01Raw", 'a') as f:
    soup = BeautifulSoup(page.content, "html.parser")
    for a_href in soup.find_all("a", href=True):
        print(a_href["href"], file=f)
    f.close()

URL = "https://duelmasters.fandom.com/wiki/DM-02_Evo-Crushinators_of_Doom_Gallery_(TCG)"
page = requests.get(URL)

with open("dm02Raw", 'a') as f:
    soup = BeautifulSoup(page.content, "html.parser")
    for a_href in soup.find_all("a", href=True):
        print(a_href["href"], file=f)
    f.close()

subprocess.call(['sh', './trimFat.sh'])

open('dm01', 'w').writelines([ line for line in open('dm01Raw') if "/wiki/" in line])
open('dm01Img', 'w').writelines([ line for line in open('dm01Raw') if '.jpg' in line])
open('dm02', 'w').writelines([ line for line in open('dm02Raw') if "/wiki/" in line])
open('dm02Img', 'w').writelines([ line for line in open('dm01Raw') if '.jpg' in line])

antifandomize()

pathlib.Path.unlink('dm01Raw')
pathlib.Path.unlink('dm02Raw')

subprocess.call(['sh', './trimPics.sh'])
subprocess.call(['sh', './sortDecks.sh'])