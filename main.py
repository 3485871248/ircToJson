import json

PATH = "山雀 - 万能青年旅店.lrc"
with open(PATH, "r", encoding='utf-8') as f:
    lines = f.readlines()
ircDist = {}


def time_to_seconds(time_str):
    minutes, seconds = time_str.split(':')
    minutes = int(minutes)
    seconds = float(seconds)
    total_seconds = minutes * 60 + seconds
    return f"{total_seconds:.1f}"


for i in range(len(lines)):
    timeAndIrc = lines[i].split("]")
    timeAndIrc[0] = timeAndIrc[0].strip('[')
    timeAndIrc[0] = str(time_to_seconds(timeAndIrc[0]))
    timeAndIrc[1] = timeAndIrc[1].strip('\n')
    ircDist['time' + str(i+1)] = timeAndIrc[0]
    ircDist['text' + str(i+1)] = timeAndIrc[1]

for i in range(int(len(ircDist) / 2) - 1):
    ircDist['time' + str(i+1)] = round(float(ircDist['time' + str(i+2)]) - float(ircDist['time' + str(i+1)]), 1)

ircDist['time' + str(int(len(ircDist) / 2))] = 0.0

with open('ircDist.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(ircDist, indent=1, ensure_ascii=False))
