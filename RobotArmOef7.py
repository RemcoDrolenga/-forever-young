from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for x in range(5):
    for x in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for x in range(2):
        robotArm.moveRight()
robotArm.wait()