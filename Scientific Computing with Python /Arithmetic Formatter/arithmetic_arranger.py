def arithmetic_arranger(problems, solve=False):
  # Check if problem more than 5
  if len(problems) > 5:
    return "Error: Too many problems."

  # Create a list with 4 empty string elements
  lines = ["", "", "", ""]

  # Loop through problems
  for problem in problems:
    # Check if problem involves * or /
    if '*' in problem or '/' in problem:
      return "Error: Operator must be '+' or '-'."

    # Split problem into operands and operator
    num1, operator, num2 = problem.strip().split()

    # Check if operands are numbers
    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."

    # Check if operands have more than 4 digits
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Prepare and append the lines
    # Check max width of problem
    width = max(len(num1), len(num2)) + 2
    lines[0] += num1.rjust(width)
    lines[1] += operator.ljust(1) + num2.rjust(width - 1)
    lines[2] += '-' * width
    lines[3] += str(eval(problem)).rjust(width)

    # Add spaces between problems
    if problem != problems[-1]:
      for i in range(4):
        lines[i] += '    '

  if solve:
    arranged_problems = '\n'.join(lines)
  else:
    arranged_problems = '\n'.join(lines[:3])
  
  return arranged_problems