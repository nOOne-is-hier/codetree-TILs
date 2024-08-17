stack = []

for _ in range(int(input())):
    
    order = input().split()

    if order[0] == 'push_back':
        stack.append(order[1])

    elif order[0][0] == 'g':
        print(stack[int(order[1])-1])

    elif order[0][0] == 's':
        print(len(stack))

    elif order[0] == 'pop_back':
        stack.pop()