import math
import time
import random
import sys
# Input
# The input will consist of a number of test cases (more than one per file!). The first line of each test case
# will contain n, the number of stars for that case: 2 ≤ n ≤ 100, 000. The following n lines will contain
# the (x,y) coordinates of successive stars. Each x and y coordinate will be a real number with a minimum
# value of -50,000 and a maximum value of 50,000. The coordinates will be given to two decimal places of
# accuracy. The input will terminate when n=0
# Output
# For each test case, your output should contain a single line that is the minimum distance between two
# points, to four digits of accuracy after the decimal point. You should not print the stars that are closest;
# only the distance. If there are no points closer than a distance of 10,000, you should print out ’infinity’.


# recusivly cut them in half based off x values

# Take number of points and then points
# n = int(input("Enter num of coords: "))

# 2
# 1.25 6.11
# 1.64 1.50

# n = 2
#
# planets = ['1.25 6.11', '1.64 1.50']

# 2
# 0 0
# 0 10001

# n = 2
#
# coords = ['0 0', '0 10001']

# 3
# -6.47 2.24
# 8.90 6.53
# -1.45 5.05

# n = 3
#
# planets = ['-6.47 2.24', '8.90 6.53', '-1.45 5.05']

# 4
# 2.77 -9.81
# -0.19 4.85
# 1.38 9.05
# -4.95 3.93

# n = 4
#
# planets = ['2.77 -9.81', '-0.19 4.85', '1.38 9.05', '-4.95 3.93']

# 10
# 8.15 6.21
# -5.64 -4.31
# -0.03 7.05
# 5.98 -4.64
# 1.49 -1.59
# 4.34 0.67
# -2.79 -0.93
# -7.41 2.89
# -1.79 -6.22
# -0.98 1.74
# 0

# n = 10
#
# planets = ['8.15 6.21', '-5.64 -4.31', '-0.03 7.05', '5.98 -4.64', '1.49 -1.59', '4.34 0.67', '-2.79 -0.93',
#            '-7.41 2.89', '-1.79 -6.22', '-0.98 1.74']


#horizontal line(same y):

# runLaterList = []
# n = 8
# ns = [n]
# planets = ['1 2', '3 2' ,'1.5 2' ,'1000 2' ,'30 2' ,'37 2' ,'90 2' ,'99 2', '10 2', '30 2' ,'10.7 2' ,'10000 2' ,'300 2' ,'370 2' ,'900 2' ,'990 2']
# runLaterList.append(planets)


#vertical line(same x):

# runLaterList = []
# n = 14
# ns = [n]
# planets = ['2 1', '2 3' ,'2 1000' ,'2 30', '2 37' ,'2 90' ,'2 99', '2 10', '2 35' ,'2 10.7' ,'2 10000' ,'2 300' ,'2 370' , '2 1.5' ]
# runLaterList.append(planets)


# n = 3000
# planets = []

#
# for i in range(n):
#     planets.append(sys.stdin.readline())



# for i in range(n):
#     planets.append(str(round(random.uniform(-50000.0,50000.0),2)) + " " + str(round(random.uniform(-50000.0,50000.0),2)))
# runLaterList = []
# ns = []
# ns.append(n)
# runLaterList.append(planets)


runLaterList = []
n = int(sys.stdin.readline().rstrip("\n"))
ns = []
while n != 0:
    planets = []
    for i in range(n):
        planets.append(sys.stdin.readline().rstrip("\n"))
    runLaterList.append(planets)
    ns.append(n)
    #print(n,ns)
    n = int(sys.stdin.readline().rstrip("\n"))



# take xvalue for sort
def xvalue(elem):
    elem1st = elem.split()
    # print(elem1st[0])
    return float(elem1st[0])


# take yvalue for sort
def yvalue(elem):
    elem2nd = elem.split()
    # print(elem2nd[1])
    return float(elem2nd[1])


#
# coordsy = planets.copy()
#
# planets.sort(key=xvalue)
# coordsy.sort(key=yvalue)







#print(coords)
#print(coordsy)

# print(math.sqrt((6 - 0)**2 + (8 - 0)**2))

# sort the pair of points by x coordinate

def findDist(list, first, last):
    # print(first, last)
    # for x in range(first, last):
    #     for j in range(x+1, last):
    #         print("x:",x,"j:",j)
    #         print(list[x], list[j])
    # change the input to x and y
    # sqrt((x2 - x1) ^2 + (y2 - y1)^2 )
    lowestDist = math.sqrt((float(list[1].split()[0]) - float(list[0].split()[0]))**2 + (float(list[1].split()[1]) - float(list[0].split()[1]))**2)

    if len(list) != 2:
        #print("the number", n, list[first], list[last-1], first, last)
        for x in range(first, last):

            for j in range(x+1,last):
                # if x != 0 and j != 1:
                    # find the distance between i and j
                    coord1 = list[x].split()
                    # print(j,n,list)
                    coord2 = list[j].split()
                    # print(x,j)
                    dist = math.sqrt((float(coord2[0]) - float(coord1[0]))**2 + (float(coord2[1]) - float(coord1[1]))**2)

                    # print(coord1, coord2)
                    # print("THE DISTANCEEEeEEEEEE (not strip)",dist)
                    if(dist < lowestDist):
                        lowestDist = dist

    if lowestDist > 10000:
        return "infinity"
    return round(lowestDist, 4)


def findDistInStrip(n, list,lowest):
    # change the input to x and y
    # sqrt((x2 - x1) ^2 + (y2 - y1)^2 )
    if lowest =="infinity":
        lowestDist = 10000
    else:
        lowestDist = lowest

    for x in range(n):
        rangeY = n
        if n > 7:
            rangeY = 7

        for j in range(x+1,rangeY):
            # print("rangeY:",rangeY,"x:", x,"j:",j)
            # find the distance between i and j
            coord1 = list[x].split()
            coord2 = list[j].split()

            # print(coord1,coord2)
            if(float(coord2[1]) - float(coord1[1]) < lowest):
                dist = math.sqrt((float(coord2[0]) - float(coord1[0]))**2 + (float(coord2[1]) - float(coord1[1]))**2)

                # print(coord1, coord2)
                # print("THE DISTANCEEEeEEEEEE",dist)
                if(dist < lowestDist):
                    lowestDist = dist
    if lowestDist > 10000:
        lowestDist = "infinity"
    #print(lowestDist)
    return lowestDist
# findDist(n, coords)


def clostestPair(listx, first, last, listy):
    #print(first, last, last-first)
    if last-first < 4:
        # print(first, last)
        return findDist(listx, first, last)


    half = (math.ceil((last-first) / 2)-1)
    half += first
    # split in half
    # print(half)
    # print("THE FIRST HALF", first, half+1)
    listL = set(listx[first:half+1])
    listyLEFT = []
    listyRIGHT = []
    for item in listy:
        if item in listL:
            listyLEFT.append(item)
        else:
            listyRIGHT.append(item)
    # print(first,last)
    # print("listyLEFT",listyLEFT)
    # print("listyRIGHT",listyRIGHT)
    # print("listX:")
    # for i in range(first, last):
    #     print(listx[i])

    lowest1 = clostestPair(listx, first, half+1, listyLEFT) #[0:half+1])
    # print(listx,listx[half])
    # print("THE SECOND HALF", half+1, last)
    lowest2 = clostestPair( listx, half+1, last, listyRIGHT) #[half+1:])

    # print("LOWEsT",lowest1,lowest2)

    if lowest1 == "infinity" and lowest2 == "infinity":
        lowest = "infinity"
    elif lowest1 == "infinity":
        lowest = lowest2
    elif lowest2 == "infinity":
        lowest = lowest1

    elif lowest1 != "infinity" and lowest2 != "infinity":
        #print("i dont work", lowest2- lowest1)
        if lowest2 - lowest1 > 0:
            lowest = lowest1
        else:
            lowest = lowest2

    if lowest == "infinity":
        lowest = 10001

    #print(lowest)
    # combine STEP(THE STRIP)
    #print("////////////////////////////////////////////////////////////", "strip part")
    strip = []
    median = listx[half].split()
    # print(listx,"\n", half, "\n", median)
    # do it on the y sorted list instead
    for x in listy:
        elem1st = x.split()
        #print(elem1st[0])
        if abs(float(elem1st[0])-float(median[0]))< lowest:
            #print("median", median, elem1st[0], elem1st[1], lowest, ">=", abs(float(elem1st[0])-float(median[0])) )
            strip.append(x)
    lenStrip = len(strip)
    if lenStrip != 0:
        lowestStrip = findDistInStrip(lenStrip, strip,lowest)
    else:
        lowestStrip = lowest
    #print("////////////////////////////////////////////////////////////",lowestStrip)

    if lowestStrip == "infinity":
        lowestStrip = 10001

    #print(lowest, lowestStrip,"lowest")
    if lowestStrip < lowest:
        lowest = lowestStrip
    if lowest > 10000:
        return "infinity"


    return round(lowest, 4)
# if the y coord - other y coord is more than d stop



#print(clostestPair(n, coords, 0, n, coordsy))
# start = time.time()

n = 0
for planets in runLaterList:
    coordsy = planets.copy()

    planets.sort(key=xvalue)
    # print(planets)
    coordsy.sort(key=yvalue)
    # print(coordsy)
    #print(ns[n],planets)
    # print(planets)
    # print(ns[n])
    # print(coordsy)

    # start = time.time()
    closestNUM = clostestPair(planets, 0, ns[n], coordsy)
    # end = time.time()
    # print(end - start)

    # start = time.time()
    # print(findDist(planets, 0, ns[n]))
    # end = time.time()
    # print(end - start)

    if closestNUM == "infinity":
        print(closestNUM)
    else:
        print('{:.4f}'.format(round(closestNUM, 4)))
    n += 1
# end = time.time()
# print(end - start)















