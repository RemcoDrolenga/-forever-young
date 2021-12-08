from RobotArm import RobotArm
robotArm = RobotArm('exercise 4')
for x in range(3):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
for y in range(3):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
robotArm.wait()