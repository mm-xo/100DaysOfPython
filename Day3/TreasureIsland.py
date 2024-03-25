
print("Welcome to the Treasure Island!\nYour mission is to find the treasure.\nYou're at a crossroad. Where do you want to go?")

def validate(question, *answer):
	flag = True
	while flag:
		choice = input(question)
		choice.lower()
		if choice in answer:
			flag = False
	return choice

flag = True
while flag:
	options_1 = "Type \"left\" or \"right\".  "
	choice_1 = validate(options_1, "left", "right")
	if choice_1 == "left":
		print("You've come to a lake. There is an island in the middle of the lake.")
		options_2 = "Type \"wait\" to wait for a boat. Type \"swim\" to swim across.  "
		choice_2 = validate(options_2, "wait", "swim")
		if choice_2 == "wait":
			print("You arrive at the island unharmed. There is a house with 3 doors.")
			options_3 = "One red, one yellow and one blue. Which colour do you choose?  "
			choice_3 = validate(options_3, "red", "yellow", "blue")
			if choice_3 == "red":
				print("It's a room full of fire. Game Over.")
				flag = False
			elif choice_3 == "yellow":
				print("You found the treasure! You Win!")
				flag = False
			elif choice_3 == "blue":
				print("You enter a room of beasts. Game Over.")
				flag = False
		elif choice_2 == "swim":
			print("You get attacked by an angry trout. Game Over.")
			flag = False
	elif choice_1 == "right":
		print("You fell into a hole. Game Over.")
		flag = False










