print("Welcome to the tip calculator!")

# intFlag = True
# while intFlag:
# 	try:	
# 		totalBill = float(input("What was the total bill?"))
# 		if isinstance(totalBill, float):
# 			intFlag = False
# 	except ValueError:
# 		print("invalid input")


def inputChecker(question):
	flag = True
	while flag:
		try:
			answer = float(input(str(question)))
			if isinstance(answer, float):
				flag = False
		except:
			print("invalid input")
	return answer

bill = inputChecker("What was the total bill? ")
tip = inputChecker("How much tip would you like to give? (in %) ")
splitCount = inputChecker("How many people to split the bill into? ")
totalBill = (bill + (bill*(tip/100))) / splitCount
print(f"Each person should pay: ${totalBill}")