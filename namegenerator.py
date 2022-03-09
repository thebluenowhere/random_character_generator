import random 
name = input(f"What's the name?! ")
nation = random.choice(open('nationalities.txt').readlines()).replace('\n', '')
adjective = random.choice(open('adjectives.txt').readlines()).replace('\n','')
animal = random.choice(open('animals.txt').readlines()).replace('\n', '')
profession = random.choice(open('professions.txt').readlines()).replace('\n','')
profession = profession[:-1]

print(f"Ah, yes. {name.title()}. Also known as The {adjective} {animal} {profession}! He's {nation}!"
