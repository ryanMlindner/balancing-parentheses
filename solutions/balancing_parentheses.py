def balancing_parentheses(string):

    # solve keeping dynamic track of parenthesis mismatch
    openings = 0
    missings = 0

    for i in range(len(string)):

        if string[i] == '(':
            openings += 1
            continue

        if openings > 0:
            openings -= 1
        else:
            missings += 1

    return openings + missings

    # solve using stack data structure
    '''
    stack = []

    extra = 0

    for i in range(len(string)):

        if string[i] == '(':
            stack.append('(')

        elif string[i] == ')':

            if len(stack) > 0:
                stack.pop()

            else:
                extra += 1

    extra += len(stack)

    return extra
    '''

if __name__ == '__main__':
    print("Expecting: 0")
    print(balancing_parentheses('(()())'))

    print("")

    print("Expecting: 2")
    print(balancing_parentheses('()))'))

    print("")

    print("Expecting: 1")
    print(balancing_parentheses(')'))

    print("")

    print("Expecting: 0")
    print(balancing_parentheses('()'))

    print("")

    print("Expecting: 1")
    print(balancing_parentheses('('))

    print("")

    print("Expecting: 2")
    print(balancing_parentheses(')('))

    print("")

    print("Expecting: 1")
    print(balancing_parentheses(')()'))

    print("")

    print("Expecting: 2")
    print(balancing_parentheses(')((((()))((())))()(()))('))

    print("")

    print("Expecting: 3")
    print(balancing_parentheses(')))'))

    print("")

    print("Expecting: 3")
    print(balancing_parentheses('((('))

# Please add your pseudocode to this file
##################################################################################
# initialize missing to 0 (will store unmatched closing parens count)
# initialize openings to 0 (will store opening parens count)
#
# iterate over string:
#   if char == '(':
#     increment openings
#   else:
#     if openings is 0:
#       increment missing
#     else:
#       decrement openings
#
# return missing + openings
##################################################################################

# And a written explanation of your solution
##################################################################################
# We can calculate the number of parentheses needed by counting the number of opening
# parentheses that occur in the string and decrementing that count any time a closing
# parenthesis is encountered after that. If we encounter a closing parenthesis and there
# are no opening parentheses (openings = 0), we add to missing. Once we've iterated 
# over the whole string, we just need to add the missing count with the openings count,
# since the openings count will track any opening parentheses for which there were no
# matching closing ones.
##################################################################################