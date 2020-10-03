def Gaussian() : #main statement
    n = int(input()) #input n value
    value = [] #empty list
    loop = 1 #start loop
    while loop <= n : #while statement for input looping
        value.append(list(map(float,input().split()))) #input matrix value
        loop +=1 #loop = loop + 1
    for y in range(n-1) : #statement for y in range stop until n-1
        for x in range(y+1,n) : #statement for x in range start from y+1 until n
            if value[y][y] == 0 : #statement if value[y][y] = 0
                z = x + 1 #z = x + 1
                while z < n and value[z][y] == 0 : #statement while z small than n and value[z][y] = 0
                    z += 1 #z = z + 1
                if z == n : #statement if z = n
                    print('no solution') #print no solution
                    return #return
                value[y],value[z] = value[y],value[z] #value[y],value[z] = value[y],value[z]
            multiple = value[x][y] / value[y][y] #multiple = value[x][y] divided by value[y][y]
            for f in range(0, n+1) : #statement for in range start from 0 until n+1
                value[x][f] = value[x][f] - value[y][f] * multiple #value[x][f] = value[x][f] minus value[y][f] multiplied by multiple
    for y in range(n-1,0,-1) : #statement for y in range start from n-1 until 0 with step is -1
        for x in range(y-1,-1,-1): #statement for x in range start from y-1 until -1 with step is -1
            multiple = value[x][y] / value[y][y] #multiple = value[x][y] divided by value[y][y]
            value[x][y] = 0 #value[x][y] is zero
            value[x][n] = value[x][n] - value[y][n] * multiple #value[x][f] = value[x][f] minus value[y][f] multiplied by multiple
    for y in range(n) : #statement for y in range until n
        if value[y][y] != 1 : #statement if value[y][y] isn't 1
            value[y][n] = value[y][n] / value[y][y] #value[y][n] = value[y][n] divided by value[y][y]
            value[y][y] = 1 #value[y][y] is one
        print(value[y][n]) #print value[y][n]
Gaussian() #run main statement
