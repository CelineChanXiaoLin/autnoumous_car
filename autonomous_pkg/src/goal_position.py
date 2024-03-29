#!/usr/bin/env python
# license removed for brevity

import rospy
# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
#Brings in the navigation file to retrieve the position and orientation  that change over time.
from nav_msgs.msg import Odometry
#Expresses velocity messages in free space broken into its linear and angular parts.
from geometry_msgs.msg import Point,Twist
#retrieve the rotation axis and rotation angle 
from tf.transformations import euler_from_quaternion

def movebase_client():

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = -0.547064045226
    goal.target_pose.pose.position.y = -1.89311686738

   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w =  0.836323218712
   

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   #If the result does not reach the server or the server does not work
    if not wait:
        rospy.logerr("Operation server is unavailable!")
        rospy.signal_shutdown("Operation server is unavailable!")
    else:
    # Result of executing the action
        return client.get_result() 
  

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution is complete!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test completed.")
