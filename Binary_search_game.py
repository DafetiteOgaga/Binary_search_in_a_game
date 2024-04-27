#!/usr/bin/env python3

import random, sys

# a simple demonstration of using a binary search algorithm in a
# number guessing game.

def main ():
	"""a number guesing game aimed at demonstrating the principle of
		binary search algorithm.
	"""
	start_num = random.randint(1, 10) # adjust this range to change the gap of possible random numbers
	
	# start_num = 1

	range_of_num = [x for x in range(start_num, start_num + 10)] # adjust the number '10' to change the length of number list to be generated
	
	random.shuffle(range_of_num )
	lucky_num = random.choice(range_of_num)
	sorted_list = sorted(range_of_num)

	count = 0
	limit = 5 # adjust this number to change the number of attempts
	
	# print ('lucky_num:', lucky_num)
	text = "\nYou have {} total attempts to find the lucky number. Use [q] to quit".format(limit - 1)
	print (text)
	print("".rjust(len(text), "."), "\n")
	print ("List: {}".format(sorted_list))
	while True:
		count += 1
		if count == limit:
			print('You have exhausted 3 attempts.\nThe lucky number is {}\nTry again.'.format(lucky_num))
			sys.exit(0)
		sorted_list2 = sorted_list
		try:
			if count > 1:
				prompt1 = "Guess again"
				attempts = "You have {} more attempt(s)".format(limit - count)
				newline = "\n"
			else:
				prompt1 = "Guess the lucky number"
				attempts = newline = ""
			print(attempts, end=newline)
			guess = input ("{} between [{}] and [{}] >>> ".format(prompt1, sorted_list[0], sorted_list[-1]))
			if guess.lower() == "q":
				print()
				print('Cheers.')
				sys.exit(0)
			guess = int(guess)
		except ValueError:
			print ('You must enter a number.')
			print ()
			continue

		index_half = (len(sorted_list)//2)
		half = sorted_list[index_half]
		less_than_half = guess < half

		if guess not in sorted_list:
			print()
			print ('Invalid! Your guess not in list.\n{}'.format(sorted_list))
			break
		
		if guess != lucky_num:
			if less_than_half:
				sorted_list = sorted_list [:index_half]
			else:
				sorted_list = sorted_list [index_half:]
		else:
			print()
			print('You Won!')
			break

		if len (sorted_list) == 1:
			print()
			print ('You failed. The lucky number is {}'.format(lucky_num))
			break 

		if lucky_num not in sorted_list:
			sorted_list = sorted_list2
			if less_than_half:
				print('Nope, move up your guess =>')
				print()
				continue
			else:
				print('Nope, move down your guess <=')
				print()
				continue

		print ()
		print ('Halved list:', sorted_list)
	print ("Number of attempt(s): {}".format(count))

if __name__ == "__main__":
	main()
