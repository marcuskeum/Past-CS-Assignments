import sys



titleNames = []
allTitles = []
allTitlesFast = []



for line in sys.stdin:
    line = line.rstrip("\n")
    line = line.split(" ")
    # print(line)
    title = []
    titleFast = []
    if len(line) == 3:
        titleNames.append(line[0] + ":")
        #get the rows
        for x in range(int(line[1])):
            rowItems = sys.stdin.readline().rstrip("\n").split(" ")
            rowFast = []
            row = []
            # print("rowItems:",rowItems)
            #append the items in the row
            for i in range(int(line[2])):
                row.append(int(rowItems[i]))
                rowFast.append(0)
            x += 1
            #append the rows to make colums
            title.append(row)
            titleFast.append(rowFast)


        allTitles.append(title)
        allTitlesFast.append(titleFast)

# print(allTitles[0][2][0])
# print(allTitlesFast)
# print(titleNames)

#print(allTitles[0][0][1])

def drainage(map, fastmap, row, col):
    if fastmap[row][col] != 0:
        return fastmap[row][col]

    current = map[row][col]
    left = 0
    right = 0
    up = 0
    down = 0
    #left
    if (col-1 >= 0):
        if (map[row][col-1] < current):
            # print("left" , map[row][col-1], current)
            left = drainage(map,fastmap, row, col-1)
    #right
    if (col+1 < len(fastmap[row]) ):
        # print("length of row:", len(fastmap[row]))
        if (map[row][col+1] < current):
            # print("right", current, map[row][col+1])
            right = drainage(map,fastmap, row, col+1)
    #down
    if (row+1 < len(fastmap)):
        if (map[row+1][col] < current):
            # print("down")
            down = drainage(map,fastmap, row+1, col)
    #up
    if (row-1 >= 0):
        if (map[row-1][col] < current):
            # print("up")
            up = drainage(map,fastmap, row-1, col)

    if (left == 0) and (right == 0) and (up == 0) and (down == 0):
        fastmap[row][col] = 1
        return 1

    fastmap[row][col] = 1 + max(left,right, up, down)
    # print("FASTMAP:", fastmap[row][col], "CURRENT", current)
    return fastmap[row][col]

for i in range(len(allTitles)):
    for row in range(len(allTitles[i])):
        # print("ROW", row)
        for col in range(len(allTitles[i][row])):
            # print("COLUMN", col)
            drainage(allTitles[i], allTitlesFast[i], row, col)
            # print(drainage(allTitles[i], allTitlesFast[i], row, col))

    maxSet = set()
    for elem in range(len(allTitlesFast[i])):
        row = allTitlesFast[i][elem]
        # print("ROW", row)
        rowSet = set(row)
        maxRow = max(rowSet)
        # print(maxRow)
        maxSet.add(maxRow)
    print(titleNames[i],max(maxSet))




