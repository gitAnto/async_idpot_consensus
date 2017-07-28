#!/usr/bin/env python
NAME = 'async_idpot_consensus'

import rospy
from consensus_params import *
from async_idpot_consensus.msg import cons_data


class consensus_node:

	def __init__(self, node_id, consensus_type, init_value): #, rate):
		self.id = node_id
		self.consensus_type = consensus_type
		self.x = init_value
		#self.rate = rate
                print("Initializing node with %s %s %s" % (str(self.id), str(self.x), consensus_type))

		self.sub = rospy.Subscriber('channel', cons_data, self.my_handler)
		self.pub = rospy.Publisher('channel', cons_data, queue_size=10)


	def my_handler(self, msg):
		print("Received message")
		print("   node_id     = %s" % msg.id)
		print("   data        = %s" % msg.data)

		if G[self.id][int(msg.id)] == 1:
                        type_of_x = str(type(self.x))
                        type_of_x = type_of_x[7:-2]
#                        print "type_of_x: " + type_of_x
#                        print eval(type_of_x+"(msg.data)")
#                        print consensus_dict[self.consensus_type]
#                        print consensus_dict[self.consensus_type]([self.x, eval(type_of_x+'(msg.data)')])
#                        print consensus_dict[self.consensus_type]([3, 45])
			self.x = consensus_dict[self.consensus_type]([self.x, eval(type_of_x+'(msg.data)')])
			print("Consensus update -->  x = %s" % str(self.x))

	def publish(self):
#                print("I am publishing")
		msg = cons_data()
		msg.id   = str(self.id)
		msg.data = str(self.x)
#                print msg
                self.pub.publish(msg)


def main_loop():

	rospy.init_node(NAME, anonymous=True)

	node_id        = rospy.get_param('node_id', 0)
	consensus_type = rospy.get_param('consensus_type', 'max')
	init_value     = rospy.get_param('init_value', 7)
	rate           = rospy.get_param('rate', 1)

	cons_node = consensus_node(node_id, consensus_type, init_value) #, rate)

	node_rate = rospy.Rate(rate)

	while not rospy.is_shutdown():
                #print("I am in the loop")
		cons_node.publish()
		node_rate.sleep()




if __name__ == '__main__':
	try:
		main_loop()
	except rospy.ROSInterruptException:
		pass
