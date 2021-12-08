from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
u = 8
o = 7
for i in range(4):
    robotArm.grab()
    for x in range(u, 0, -1):
        robotArm.moveRight()
    u -= 2
    robotArm.drop()
    for y in range(o, 0, -1):
        robotArm.moveLeft()
    o -= 2

robotArm.wait()