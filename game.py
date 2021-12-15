import random
import sys
from phrase import Phrase
from string import ascii_lowercase as alphabet

class Game:
	def __init__(self):
		self.missed = 0
		self.phrases = [
			'When nothing goes right go left',
			'You get what you give',
			'The best revenge is massive success',
			'Your patience is your power',
			'No pressure no diamonds'
		]
		self.active_phrase = None
		self.guesses = []

# Starts the Phrase Hunter Game
	def start(self):
			self.welcome()
			self.active_phrase = Phrase(self.get_random_phrase())
			self.active_phrase.display()
			while self.active_phrase.check_complete() and self.missed != 7:
				try:
					guess = self.get_guess()
					if len(guess) > 1 or guess not in alphabet:
						raise ValueError('Please enter only one character that is not a number or anything outside of the alphabet.')
				except ValueError as error:
					print(f'Oh no that was a invalid value ({error})')
				else:
					if self.active_phrase.check_letter(guess):
						# Checks the current phrase that matches with the current
						# Guess and stores the index where the match occurred
						index_letter_occurs = [
							index for index, letter in enumerate(self.active_phrase.phrase) if letter == guess
						]
						# Takes the indexes from index_letter_occurs and
						# Uses those indexes to find where in the hidden
						# Phrase a character should be updated to the
						# The value of the current guess
						for index in index_letter_occurs:
							self.active_phrase.hidden_phrase[index] = guess
					else:
						self.missed += 1
						print(f'Watch out! You only have {7-self.missed} out 7 of  chances left')
				print(''.join(self.active_phrase.hidden_phrase))
			self.game_over()
			# Prompts user if they would like to play again
			play_again = input('Wanna play again? ([Y]es/[N]o): ').lower()
			if play_again == 'y':
				self.missed = 0
				self.start()
			elif play_again == 'n':
				sys.exit()
			else:
			# Makes sure that the user is inputting the proper characters (Y or N)
				while play_again != 'y' or play_again != 'n':
					print('Please select either Y to continue or N end the game')
					play_again = input('Wanna play again? ([Y]es/[N]o): ').lower()
					if play_again == 'y':
						self.missed = 0
						self.start()
					elif play_again == 'n':
						break
					else:
						continue


	def get_random_phrase(self):
		return random.choice(self.phrases)

	def welcome(self):
		print('WELCOME TO THE PHRASE HUNTER GAME!')

	def get_guess(self):
		self.guess = input('Guess a letter: ')
		self.guesses.append(self.guess)
		return self.guess

	def game_over(self):
		if self.missed == 7:
			print("""\nOh no! You ran out of attempts. "YOU LOSE GENERAL KENOBI" """)
		else:
			print('\nAWESOME JOB! You discovered the hidden phrase!')

