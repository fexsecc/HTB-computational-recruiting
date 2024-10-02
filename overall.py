from collections import namedtuple


health_weight = 0.2
agility_weight = 0.3
charisma_weight = 0.1
knowledge_weight = 0.05
energy_weight = 0.05
resourcefulness_weight = 0.3

def calculate_skill_score(skill_score, weight):
    return round(6 * (int(skill_score) * weight)) + 10

def calculate_overall(health, agility, charisma, knowledge, energy, resourcefulness):
    return round(5 * ((health * 0.18) + (agility * 0.20) + (charisma * 0.21) + (knowledge * 0.08) + (energy * 0.17) + (resourcefulness * 0.16)))

dat = ''
with open("./data.txt", 'r') as f:
    dat = f.read()
    f.close()

scores = []
names = []

for line in str.splitlines(dat):
    name = line.split(' ')[1] + ' ' + line.split(' ')[2]
    health = calculate_skill_score(line.split(' ')[3], health_weight)
    agility = calculate_skill_score(line.split(' ')[4], agility_weight)
    charisma = calculate_skill_score(line.split(' ')[5], charisma_weight)
    knowledge = calculate_skill_score(line.split(' ')[6], knowledge_weight)
    energy = calculate_skill_score(line.split(' ')[7], energy_weight)
    resourcefulness = calculate_skill_score(line.split(' ')[8], resourcefulness_weight)

    overall_value = calculate_overall(health, agility, charisma, knowledge, energy, resourcefulness)

    names.append(name)
    scores.append(overall_value)

profiles = list(zip(names,scores))
profiles.sort(key=lambda x: x[1], reverse=True)
hof = profiles[:14]
for line in hof:
    print(line[0] + ' - ' + str(line[1]),end = ', ')

