# https://www.hackerrank.com/challenges/py-the-captains-room/problem

k, allocation = int(input()), input().split()

rooms, group_rooms = set(), set()
for r in allocation:
    if r in rooms:
        group_rooms.add(r)
    else:
        rooms.add(r)

captains_room = rooms - group_rooms
print(captains_room.pop())  