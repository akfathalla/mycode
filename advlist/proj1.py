#!/usr/bin/env python3
"""
Group 2
"""
#Run-time code
def main():
	#Greet the player
	user = input("Welcome!, how may we call you?\n>>")

	print("We are going to play a game where we ask you a lot of questions.")
	print("Fill in the blanks")


	#Start the game
	print("Python is a ____adj1_____ language that lets you ___verb1____ more ___verb2____ and integrate your ____poss_pronoun1____ more effectively.")
	print("You can learn to _____verb3____ Python and see almost ____adj2_____  ____verb4_____ in productivity and ___verb5____  maintenance costs.")


	adj1 = input("Python is a _________ (don't think about snakes) \n")
	verb1 = input("lets you _________ (Somehow you have to make a living no?) \n")
	verb2 = input("More? _________ (Yes, there is more) \n")
	object1 = input("Anything you use _________ (Don't be shy) \n")
	verb3 = input("synonym of manipulate _________ (I am wondering now...)  \n")
	adj2 = input("Now? _________ (chop chop) \n")
	verb4 = input("It is a win, but is not money _________ \n")
	verb5 = input("Just pick a word _________ (Any word?) \n")
	print(f"Python is a {adj1} language that lets you {verb1} more {verb2} and integrate your {object1} more effectively.")
	print(f"You can learn to {verb3} Python and see almost {adj2} {verb4} in productivity and {verb5}  maintenance costs.") 



if __name__ == "__main__":
	main()
