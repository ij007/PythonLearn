stack = []
while True:
  n = input()
  if n == "":
    break
  else:
    stack.append(int(n))
    
stack = sorted(stack)

for x in range(len(stack)):
    for y in range(len(stack)):
        if((stack[x]+stack[y]) in stack and x!=y):
            print(stack[x],stack[y])