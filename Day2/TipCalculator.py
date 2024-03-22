# Last edited: 23.55 March 21, 2024


print("Welcome to the tip calculator!")

'''
Here I had to think about making  sure I don't get any input except an integer
Therefore, I had to apply a try except block to check and catch for invalid inputs
and keep asking till the input in valid.
'''
# intFlag = True
# while intFlag:
# 	try:	
# 		totalBill = float(input("What was the total bill?"))
# 		if isinstance(totalBill, float):
# 			intFlag = False
# 	except ValueError:
# 		print("invalid input")

'''
I realised that i would need to check for invalid input for each question
so to keep my code "DRY", I made a function that makes sure that all input is
a float before assigning it a variable.
'''

def inputChecker(question):
    """
    This function takes a question as input, prompts the user for a float value as the answer, 
    and ensures that the input is a valid float. It continues to prompt the user until a valid 
    float value is provided. Finally, it returns the valid float value.

    Parameters:
    question (str): The question to prompt the user for input.

    Returns:
    float: The valid float value provided by the user.
    """
    flag = True  
    while flag:
        try:
            answer = float(input(str(question)))  
            if isinstance(answer, float):  
                flag = False  
        except ValueError:  
            print("Invalid input. Please enter a valid number.")  
    return answer 

bill = inputChecker("What was the total bill? ")
tip = inputChecker("How much tip would you like to give? (in %) ")
splitCount = inputChecker("How many people to split the bill into? ")
totalBill = (bill + (bill*(tip/100))) / splitCount
print(f"Each person should pay: ${totalBill}")


