
def arithmetic_arranger(problems, Answer_display = False):

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''
    first_problem = True

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        first_number = problem.split()[0]
        second_number = problem.split()[2]
        operand = problem.split()[1]
        try:
            int(first_number)
        except:
            return 'Error: Numbers must only contain digits.'
        
        try:
            int(second_number)
        except:
            return 'Error: Numbers must only contain digits.'

        try:
            if operand != "+" and operand != "-":
                raise BaseException
        except:
            return "Error: Operator must be '+' or '-'."

        try:
            if  len(first_number) > 4 or len(second_number) > 4:
                raise BaseException
        except:
            return "Error: Numbers cannot be more than four digits."


        space = max(len(first_number),len(second_number))

        if Answer_display == False:
            if first_problem == True:
                first_line += first_number.rjust(space + 2, " ")
                second_line += operand + " "+ second_number.rjust(space," ")
                third_line += ("-"*(space + 2))  
                first_problem = False   
            else:
                first_line += " "*4 + first_number.rjust(space + 2, " ")
                second_line +=" "*4 + operand + " "+ second_number.rjust(space," ")
                third_line += " "*4 + ("-"*(space + 2))
        else:
            if operand == "+":
                result = int(first_number) + int(second_number)
            else:
                result = int(first_number) - int(second_number)
            result = str(result) 

            if first_problem == True:
                first_line += first_number.rjust(space + 2, " ")
                second_line += operand + " "+ second_number.rjust(space," ")
                third_line += ("-"*(space + 2))
                fourth_line += result.rjust(space + 2, " ")
                first_problem = False
            else:
                first_line += " "*4 + first_number.rjust(space + 2, " ")
                second_line +=" "*4 + operand + " "+ second_number.rjust(space," ")
                third_line += " "*4 + ("-"*(space + 2))
                fourth_line += " "*4 + result.rjust(space + 2, " ")

    if Answer_display == True:             
        return first_line + "\n" +second_line + '\n'+third_line + "\n" + fourth_line

    return first_line + "\n" +second_line + '\n'+third_line    



print(arithmetic_arranger(["32 + 698", "801 + 2252", "8888 + 4444", "123 + 49", "66 + 9502"], True))
