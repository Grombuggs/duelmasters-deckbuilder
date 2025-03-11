with open("dm01Img", 'a') as f:
    lines = [line.replace('fandom', 'antifandom') for line in f]
with open ("dm01Img, 'w") as f:
    f.write(''.join(lines))
    f.close()

with open("dm02Img", 'a') as f:
    lines = [line.replace('fandom', 'antifandom') for line in f]
with open ("dm02Img, 'w") as f:
    f.write(''.join(lines))
    f.close()