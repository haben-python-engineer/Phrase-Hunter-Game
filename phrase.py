class Phrase:
	def __init__(self, phrase):
		self.phrase = phrase.lower()
		self.hidden_phrase = []

	def display(self):
		for character in self.phrase:
			if character.isspace():
				self.hidden_phrase.append(' ')
			else:
				self.hidden_phrase.append('_ ')
		print(''.join(self.hidden_phrase))

	def check_letter(self, guess):
		return guess.lower() in self.phrase

	def check_complete(self):
		if '_ ' in self.hidden_phrase:
			return True
		else:
			return False

	def __str__(self):
		return self.phrase

