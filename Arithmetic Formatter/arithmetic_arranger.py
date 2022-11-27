def arithmetic_arranger(problems, outcome=False):
    arranged_lines = []

    for problem in problems:  # split list into separate problems
        line = problem.split()
        #  ['3', '+', '855']

        try:  # check if each number (operand) contains digits
            int(line[0])
            int(line[2])
        except:
            return "Error: Numbers must only contain digits."

        if len(line[0]) > 4 or len(line[2]) > 4:  # check if each operand consists of max four digits
            return "Error: Numbers cannot be more than four digits."

        a = int(line[0])
        b = int(line[2])
        operator = line[1]

        if operator != "+" and operator != "-":
            return "Error: Operator must be \'+\' or \'-\'."

        if len(problems) > 5:  # check if there are too many problems supplied to the function, the limit is five
            return "Error: Too many problems."

        longest_value = max(len(line[0]), len(line[2]))
        width = longest_value + 2

        # separate problem into lines
        l1 = f"{a:>{width}}"
        l2 = f"{operator} {b:>{longest_value}}"
        dashes = f"{'-' * width}"

        # check if there is already a problem, if it is, add spaces
        try:
            arranged_lines[0] += (" " * 4) + l1
        except IndexError:
            arranged_lines.append(l1)

        try:
            arranged_lines[1] += (" " * 4) + l2
        except IndexError:
            arranged_lines.append(l2)

        try:
            arranged_lines[2] += (" " * 4) + dashes
        except IndexError:
            arranged_lines.append(dashes)

        if operator == "+":
            ans = a + b
        else:
            ans = a - b

        answr = f"{ans:>{width}}"

        if outcome:
            try:
                arranged_lines[3] += (' ' * 4) + answr
            except:
                arranged_lines.append(answr)

    output = f"{arranged_lines[0]}\n{arranged_lines[1]}\n{arranged_lines[2]}"

    if outcome:
        output = output + f"\n{arranged_lines[3]}"

    return output
