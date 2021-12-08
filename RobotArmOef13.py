from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)

Opnieuw = True
u = 1
while Opnieuw == True:
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        Opnieuw = False
    for x in range(u):
        robotArm.moveRight()
    robotArm.drop()
    for y in range(u):
        robotArm.moveLeft()
    u += 1
robotArm.wait()