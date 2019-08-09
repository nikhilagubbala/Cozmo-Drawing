import cozmo
import cozmo_movement as actions

def main(robot: cozmo.robot.Robot):
    # YOUR CODE HERE

    '''actions.drive_in_cm(robot,2)
    actions.change_lift(robot,1) 
    actions.turn(robot,-90)
    actions.drive_in_cm(robot,-.5)
    actions.change_lift(robot,0)
    actions.drive_in_cm(robot,2)
    actions.change_lift(robot,1) 
    actions.turn(robot,-90)
    actions.drive_in_cm(robot,-.5)
    actions.change_lift(robot,0)
    actions.drive_in_cm(robot,2)
    actions.change_lift(robot,1) 
    actions.turn(robot,-90)
    actions.drive_in_cm(robot,-.5)
    actions.change_lift(robot,0)
    actions.drive_in_cm(robot,2)
    actions.change_lift(robot,1) 
    actions.turn(robot,-90)
    actions.drive_in_cm(robot,-.5)
    actions.change_lift(robot,0)
    actions.drive_in_cm(robot,2)
    actions.change_lift(robot,1) 
    actions.turn(robot,-90)
    actions.drive_in_cm(robot,-.5)
    actions.change_lift(robot,0)
    actions.drive_in_cm(robot,2)
    actions.change_lift(robot,1) 
    actions.turn(robot,-90)
    actions.drive_in_cm(robot,-.5)
    actions.change_lift(robot,0)
    actions.drive_in_cm(robot,2)
    actions.change_lift(robot,1) 
    actions.turn(robot,-90)
    actions.drive_in_cm(robot,-.5)
    actions.change_lift(robot,0)
    actions.drive_in_cm(robot,2)
    actions.change_lift(robot,1) 
    actions.turn(robot,-90)
    actions.drive_in_cm(robot,-.5)
    actions.change_lift(robot,0)
    actions.drive_in_cm(robot,2)
    actions.change_lift(robot,1) 
    actions.turn(robot,-90)
    actions.drive_in_cm(robot,-.5)
    actions.change_lift(robot,0)
    actions.drive_in_cm(robot,2)'''


    actions.turn(robot,360)  #circle
    actions.change_lift(robot,1) #arm up
    actions.drive_in_cm(robot,-2) #backwards
    actions.turn(robot,-90) #right
    actions.drive_in_cm(robot,3) #forward
    actions.turn(robot,90) #left
    actions.change_lift(robot,0) #down
    actions.drive_in_cm(robot,-3.5) #back
    actions.change_lift(robot,1) #up
    actions.drive_in_cm(robot,-2) #back
    actions.change_lift(robot,0) #down
    actions.drive_in_cm(robot,-3.5) #back
    actions.change_lift(robot,1) #up
    actions.turn(robot,90)  #circle
    actions.drive_in_cm(robot,7)
    actions.turn(robot,-90)  #circle  
    actions.drive_in_cm(robot,1)
    actions.change_lift(robot,0) #down
    actions.drive_in_cm(robot,9) #back



   ''' actions.turn(robot,360)  #circle
    actions.change_lift(robot,1) #arm up
    actions.drive_in_cm(robot,-2) #backwards
    actions.turn(robot,-90) #right
    actions.drive_in_cm(robot,3) #forward
    actions.turn(robot,90) #left
    actions.change_lift(robot,0) #down
    actions.drive_in_cm(robot,-3.5) #back (eyes)
    actions.change_lift(robot,1) #up
    actions.drive_in_cm(robot,-2) #back
    actions.change_lift(robot,0) #down
    actions.drive_in_cm(robot,-3.5) #back
    actions.change_lift(robot,1) #up
    actions.turn(robot,90)  #circle
    actions.drive_in_cm(robot,3) # dist between eyes and mouth
    actions.turn(robot,-180)  #circle
    actions.drive_in_cm(robot,1)
    actions.change_lift(robot,0) #down
    actions.drive_in_cm(robot,5) #back
    actions.turn(robot,180) #semi circle '''

    

    










    # END OF YOUR CODE
    return


# vvv DON'T TOUCH THIS vvv
if __name__ == "__main__":
    cozmo.run_program(main)