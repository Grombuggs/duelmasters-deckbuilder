import re

with open('dm01Info', 'r') as f:
    lines = f.readlines()
    f.close()

with open('dm01Trimmed', 'a') as f:
    for i, line in enumerate(lines):
        if '						View source' in line:
            try:
                print("Name: ", lines[i - 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Japanese (base)' in line:
            try:
                print("Japanese Name: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Civilization:' in line:
            try:
                print("Civilization: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Card Type:' in line:
            try:
                print("Card Type: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Mana Cost:' in line:
            try:
                print("Mana Cost: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Race:' in line:
            try:
                print("Race: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'English Text:' in line:
            try:
                print("Card Info: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Power:' in line:
            try:
                print("Power: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Mana Number:' in line:
            try:
                print("Mana Number: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Illustrator:' in line:
            try:
                print("Illustrator: ", lines[i + 1].strip(), file=f)
                print("\n", file=f)
            except IndexError:
                pass

with open('dm02Info', 'r') as f:
    lines = f.readlines()
    f.close()

with open('dm02Trimmed', 'a') as f:
    for i, line in enumerate(lines):
        if '						View source' in line:
            try:
                print("Name: ", lines[i - 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Japanese (base)' in line:
            try:
                print("Japanese Name: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Civilization:' in line:
            try:
                print("Civilization: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Card Type:' in line:
            try:
                print("Card Type: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Mana Cost:' in line:
            try:
                print("Mana Cost: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Race:' in line:
            try:
                print("Race: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'English Text:' in line:
            try:
                print("Card Info: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Power:' in line:
            try:
                print("Power: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Mana Number:' in line:
            try:
                print("Mana Number: ", lines[i + 1].strip(), file=f)
            except IndexError:
                pass
        elif 'Illustrator:' in line:
            try:
                print("Illustrator: ", lines[i + 1].strip(), file=f)
                print("\n", file=f)
            except IndexError:
                pass
