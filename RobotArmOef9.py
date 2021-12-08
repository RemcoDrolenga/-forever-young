from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for x in range(3):
    robotArm.moveRight()
for i in range(5,1,-1):
    for x in range(i -1):    
        robotArm.grab()
        for x in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(5):
            robotArm.moveLeft()
    robotArm.moveLeft()
robotArm.wait()


# for i in range(1,5):
#     for x in range(1,i):
#         robotArm.grab()
#         for x in range(1,5):
#             robotArm.moveRight()
#         robotArm.drop()
#         for x in range(1,5):
#             robotArm.moveLeft()
#     robotArm.moveRight()