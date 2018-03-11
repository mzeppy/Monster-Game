from Monster import Monster
import re

monsterNames = [['demon', 5], ['goblin', 3], ['stogie', 2], ['cheese', 2], ['oz', 5], ['matt', 4], ['vampire', 3]]
monsters = []

print('Monsters avaialble:')

for i in range(len(monsterNames)):
	monsters.append(Monster(monsterNames[i][0], monsterNames[i][1]))
	monsterType = monsters[i].type
	monsterHealth = monsters[i].health
	print('%s. %s - health %i' %(i+1, monsterType, monsterHealth))

alive = True

while alive:
	damage = input('Type hit [monster] [damage] (IE: hit demon 2): ')
	damage = damage.split(' ')
	if damage[0] == 'hit':
		for givenMonster in monsters:
			if str.lower(damage[1]) == str.lower(givenMonster.type):
				print('Monster located')
				if len(damage) == 2:
					damage.append('1')
				selectedMonster = givenMonster
				if(re.search(r'[1-5]', damage[2])):
					health = selectedMonster.damage(int(damage[2]))
					if not health:
						monsters.remove(selectedMonster)
						if len(monsters) == 0:
							alive = False
					else:
						print(selectedMonster.type + '’s health is now ' + str(selectedMonster.health))
				else:
					print('Enter correct number for damage.')
				break
		else:
			print('Monster not found')
	else:
		print('Command not found.')
		
