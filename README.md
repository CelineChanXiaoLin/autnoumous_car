# Setup

    First, follow the steps in

    http://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_raspi_cam/

    Then, run

    git clone https://github.com/ros-teleop/teleop_twist_keyboard.git

# Steps

   # [REMOTE PC]

    roscore

   # [TURTLEBOT3 RPi]

    roslaunch turtlebot3_bringup turtlebot3_robot.launch
    Setup two TURTLEBOT3 RPi.

   # [TURTLEBOT3 RPi1]

    roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch

   # [REMOTE PC]

    rosrun image_transport republish compressed in:=raspicam_node/image raw out:=/raspicam_node/image

   # [REMOTE PC] 
    the Camera is ready to capture image

    rosrun find_object_2d find_object_2d image:=raspicam_node/image

    Pick an object to recognise and save it. 

   # [REMOTE PC]

    roslaunch autonomous_pkg autonomous_pkg.launch

    The turtlebot should move along when it sees the object. When it sees the object disappear from the camera image, it will      turn over to search its goal position.
    
# [TURTLEBOT3 RPi2] 
Run RVIZ
 # [REMOTE PC]
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml
# [REMOTE PC]
rosrun auntonomous_pkg goal_position.py


   

