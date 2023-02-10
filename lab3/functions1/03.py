def solve(numheads, numlegs): # 35 heads 94 legs
   rabbheads = (numlegs - 2*numheads)//2
   chickheads = abs((numlegs - 4*numheads)//2)
   print(chickheads, rabbheads)

numheads = int(input("numheads is: "))
numlegs = int(input("numlegs is: "))
solve(numheads, numlegs)