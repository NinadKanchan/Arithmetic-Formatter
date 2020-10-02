from prettytable import PrettyTable

def arithmeticRepr(listOfOperations):
    try:
        if type(listOfOperations) == list:
            operand1 = []
            operator = []
            operand2 = []
            result = []
            decoration = []
            for i in listOfOperations:
                if i.find("-") > 0:
                    operand1.append(i[0:i.find("-")].strip())
                    operator.append(i[i.find("-")].strip())
                    operand2.append(i[i.find("-"):].strip())
                    result.append(int(i[0:i.find("-")].strip()) - int(i[i.find("-")+1:].strip()))
                    decoration.append("-------------")
                elif  i.find("+") > 0:
                    operand1.append(i[0:i.find("+")].strip())
                    operator.append(i[i.find("+")].strip())
                    operand2.append(i[i.find("+"):].strip())
                    result.append(int(i[0:i.find("+")].strip()) + int(i[i.find("+")+1:].strip()))
                    decoration.append("--------------")
                elif i.find("*") > 0:
                    operand1.append(i[0:i.find("*")].strip())
                    operator.append(i[i.find("*")].strip())
                    operand2.append(i[i.find("*"):].strip())
                    result.append(int(i[0:i.find("*")].strip()) * int(i[i.find("*")+1:].strip()))
                    decoration.append("--------------")
                elif i.find("/") > 0:
                    operand1.append(i[0:i.find("/")].strip())
                    operator.append(i[i.find("/")].strip())
                    operand2.append(i[i.find("/"):].strip())
                    result.append(int(i[0:i.find("/")].strip()) / int(i[i.find("/")+1:].strip()))
                    decoration.append("--------------")
                else:
                    raise Exception  
            t = PrettyTable()
            t.border = False
            t.header = False
            t.add_row(operand1)
            t.add_row(operand2)
            t.add_row(decoration)
            t.add_row(result)
            t.align = "r"
            return t  
        else:
            raise Exception
    except:
        print("Enter Inputs Correctly")


arithmeticRepr(["30 + 4", "40 * 60", "5 - 10", "12 / 6"])


