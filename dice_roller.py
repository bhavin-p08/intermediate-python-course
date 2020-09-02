from random import randint

def main():
	dice = int(input('How many dice would you like to roll? '))
	dice_size = int(input('How many sides are the dice? '))
	total= 0
	for _ in range(dice):
		roll = randint(1,dice_size)
		total += roll
		if roll == 1:
			print(f'You rolled a {roll}! Critical Fail')
		elif roll == 6:
			print(f'You rolled a {roll}! Critical Success!')
		else:
			print(f'You rolled a {roll}')
	print(f'You have rolled a total of {total}')
if __name__== "__main__":
  main()