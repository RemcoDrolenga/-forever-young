from RobotArm import RobotArm
robotArm = RobotArm('exercise 6')
for x in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for y in range(7):
    for x in range(2):
        robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
robotArm.wait()