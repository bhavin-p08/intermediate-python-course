from random import randint

def main():
	dice = 2
	total= 0
	for _ in range(dice):
		roll = randint(1,6)
		total += roll
		print(f'You rolled a {roll}')
	print(f'You have rolled a total of {total}')
if __name__== "__main__":
  main()