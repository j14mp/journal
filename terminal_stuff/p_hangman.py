import random
import sys

word_list = ['bulbasaur', 'charmander', 'ivysaur',
			'pikachu', 'raichu', 'cyndaquil', 'chikorita',
			'haunter', 'gengar', 'geodude', 'zubat']

class Hangman:
	def __init__(self, word_list):
		self.word_list = word_list
		self.chosen_word = ''
		self.progress = []
		self.guesses = []
		self.wrong_guess = 0

	def choose_word(self):
		word = random.choice(self.word_list)
		self.chosen_word = word
		self.progress = ['_' for letter in word]	

	def show_progress(self):
		print(*self.progress)

	def restart_game(self):
		print(f'The correct answer was {self.chosen_word}.')
		player_quit = input('Would you like to play again? y/n ')
		if player_quit != 'y':
			print('Goodbye!')
			sys.exit()
		else:
			self.guesses = []
			self.wrong_guess = 0

	def start_game(self):
		while True:
			print('\n\n++++POKEMON HANGMAN++++\n\n')
			self.choose_word()
			#print(self.chosen_word)
			self.show_progress()
			while self.wrong_guess < 6 and '_' in self.progress:
				user_letter = input('\n\nPlease enter a letter: ')
				if user_letter in self.guesses:
					print(f'The letter {user_letter} has already been guessed. Please guess again.\n')
					continue
				elif user_letter not in self.guesses:
					self.guesses.append(user_letter)
					if user_letter in self.chosen_word:
						for letter in range(len(self.chosen_word)):
							if user_letter == self.chosen_word[letter]:
								self.progress[letter] = self.chosen_word[letter]
					else:
						self.wrong_guess += 1
						print(f'There is no {user_letter}. Try again.\n')
				self.show_progress()

			if '_' not in self.progress:
				print('Congratulations, you won!')
				self.restart_game()
				

			if self.wrong_guess == 6:
				print('\nSorry, you guessed wrong too many times.')
				self.restart_game()
				


hangman = Hangman(word_list)
hangman.start_game()
