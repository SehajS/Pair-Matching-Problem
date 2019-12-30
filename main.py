numbers = []
onlineDecisions = []
offlineDecisions = []

def parseInput(inputNum):
    try:
        # convert the input to float
        # eval allows to add rational inputs of the form a/b
        inputNum = float(eval(inputNum))

        # rational numbers should be in teh range is [0,1]
        if(inputNum > 1 or inputNum < 0):
            print("Input numbers should be between 0 and 1 \n")

        # rational numbers should be distinct   
        if(inputNum in numbers):
            print("Input numbers should be distinct in the range [0,1]\n")
            return None
        return inputNum
    except:
        print("Provide an input number in the correct format \n")
        return None

def check_pairs(num1, num2):
    return (num1+num2) == 1

def deterministic_online_decisions(number):
    matching_pair = False
    # 0.5 will always get 'R'
    if number != 0.5:
        for num in numbers:
            if(check_pairs(number, num)):
                matching_pair = True
                break
    onlineDecisions.append('A' if matching_pair else 'R')
    print(onlineDecisions)

def main():
    while(True):
        inputNum = input("Enter a rational number between 0 and 1 (Press 'E' to exit): ")
        
        if(inputNum == 'E'):
            break

        inputNum = parseInput(inputNum)
        numbers.append(inputNum)
        deterministic_online_decisions(inputNum)        

main()



