class Monster():
	def __init__(self, type, health):
		self.name = "monster"
		self.type = type
		self.health = health
		
	def type(self):
		return self.type
		
	def health(self):
		return self.health
		
	def damage(self, level):
		self.health -= level
		if self.health > 3:
			print('%s is still standing strong.' %self.type)
		elif self.health == 3:
			print('%s’s leg fell off!' %self.type)
		elif self.health == 2:
			print('%s’s arm fell off!' %self.type)
		elif self.health == 1:
			print('%s was hit in the torso!' %self.type)
		elif self.health <= 0:
			print('%s’s is dead!' %self.type)
		return self.health >= 1
