from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
i= 10
for x in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        i -= 1
        for y in range(i, 0, -1):
            robotArm.moveRight()
        robotArm.drop()
        for r in range(i -1):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        i -= 1
robotArm.wait()