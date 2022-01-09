import sys



allRooms = []

for line in sys.stdin:
    line = line.rstrip("\n")

    line = line.split(" ")
    rooms = []
    if len(line) == 1:
        for x in range(int(line[0])):
            line = sys.stdin.readline().rstrip("\n")
            rooms.append(line)

    allRooms.append(rooms)

#
# print(allRooms)



def daycare(rooms, roomFree, trailerFree):
    last = False

    if len(rooms) <= 1:
        # print(rooms)
        last = True
    currentRoom = rooms[0]
    currentRoomStart = int(currentRoom[0])
    currentRoomFinish = int(currentRoom[1])
    difference = currentRoomFinish - currentRoomStart
    spaceNeeded = currentRoomStart - (roomFree + trailerFree)

    if spaceNeeded < 0:
        spaceNeeded = 0


    trailerFree = spaceNeeded + trailerFree
    # print("roomFree:",roomFree, difference)
    roomFree = roomFree + difference
    if roomFree < 0:
        trailerFree = trailerFree + roomFree
        roomFree = 0
    if trailerFree < 0:
        trailerFree = 0

    # print(currentRoom)
    # print(spaceNeeded,roomFree,trailerFree)
    if spaceNeeded < 0:
        spaceNeeded = 0
    if last:
        return spaceNeeded
    else:
        return spaceNeeded + daycare(rooms[1:], roomFree, trailerFree)



def positive(elem):
    return int(elem[0])

def negative(elem):
    return -(int(elem[0]) + (int(elem[1])- int(elem[0])))

def neutral(elem):
    return int(elem[0])



for i in allRooms:
    pos = []
    neg = []
    neut = []
    for room in i:

        room = room.split(" ")
        diff = int(room[1]) - int(room[0])
        if diff > 0:
            pos.append(room)
        elif diff < 0:
            neg.append(room)
        else:
            neut.append(room)
    pos.sort(key = positive)
    neg.sort(key = negative)
    neut.sort(key = neutral)
    # print(pos, neut, neg)
    i = pos + neut + neg
    # print(i)
    #i = [['2','8'], ['14','10'], ['12','6'], ['11','6'], ['11','4'], ['6','2'], ['8','1']]
    print(daycare(i, 0, 0))



