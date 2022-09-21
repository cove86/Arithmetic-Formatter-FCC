import re


def arithmetic_arranger(problems, solve=False):
    # Declare Variables
    SPACES = " " * 4
    arranged_problems = ""
    line_one = ""
    line_two = ""
    line_three = ""
    line_four = ""

    # Check if more than problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Loop through problems
    for prob in problems:
        if re.search('[^\s0-9.+-]', prob): # Check numbers/ + -
            if re.search("[/]", prob) or re.search("[*]", prob): # check if * / exists
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        # Split each problem
        num_1 = prob.split(" ")[0]
        sym = prob.split(" ")[1]
        num_2 = prob.split(" ")[2]

        # Check if numbers more than 4 digits
        if len(num_1) > 4 or len(num_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate problem answers
        if sym == "+":
            answer = str(int(num_1) + int(num_2))
        elif sym == "-":
            answer = str(int(num_1) - int(num_2))


        length = max(len(num_1), len(num_2)) + 2 # Calculate print length needed
        top = str(num_1).rjust(length) # assign and position top number
        bottom = sym + str(num_2.rjust(length - 1)) # assign and position symbol
        result = (str(answer).rjust(length)) # assign and position answer
        dash = ""

        # assign number of dashes require
        for _ in range(length):
            dash += "-" 

        # Store each row in array
        top_row = []
        middle_row = []
        dashes = []
        result_arr = []

        # Append each row to array
        if prob != problems[-1]:
            top_row.append(top + SPACES)
            middle_row.append(bottom + SPACES)
            dashes.append(dash + SPACES)
            if solve:
                result_arr.append(result + SPACES)
        else:
            top_row.append(top)
            middle_row.append(bottom)
            dashes.append(dash)
            if solve:
              result_arr.append(result)

        # Loop through each row and append to line string
        for i in range(len(top_row)):
            line_one += top_row[i]
            line_two += middle_row[i]
            line_three += dashes[i]
            try:
                line_four += result_arr[i]
            except IndexError:
                break

    
    # Create return answer string
    if solve:
        arranged_problems = f"{line_one}\n{line_two}\n{line_three}\n{line_four}"
    else:
        arranged_problems = f"{line_one}\n{line_two}\n{line_three}"

    return arranged_problems



print(arithmetic_arranger(['3 + 855', '988 + 40'], False))