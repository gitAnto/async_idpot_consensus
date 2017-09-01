cmake_minimum_required(VERSION 2.8.3)
project(async_idpot_consensus)

find_package(catkin REQUIRED COMPONENTS rospy message_generation std_msgs geometry_msgs)

add_message_files(
	DIRECTORY msg
	FILES
	cons_data.msg
	trigger_data.msg
)

generate_messages(DEPENDENCIES std_msgs geometry_msgs)

catkin_package(CATKIN_DEPENDS message_runtime std_msgs geometry_msgs)


