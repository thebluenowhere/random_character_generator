import random 

nation = random.choice(open('nationalities.txt').readlines()).replace('\n', '')
adjective = random.choice(open('adjectives.txt').readlines()).replace('\n','')
animal = random.choice(open('animals.txt').readlines()).replace('\n', '')
profession = random.choice(open('professions.txt').readlines()).replace('\n','')
profession = profession[:-1]

print(f"Ah, yes. Andy. Also known as The {adjective} {animal} {profession}! He's {nation}!"
