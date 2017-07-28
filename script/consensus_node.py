#!/usr/bin/env python
NAME = 'async_idpot_consensus'

import rospy
from async_consensus import cons_data

from async_idpot_consensus.msg import cons_data


class consensus_node:

	def __init__(self, node_id, consensus_type, init_value): #, rate):
		self.id = node_id
		self.consensus_type = consensus_type
		self.x = init_value
		#self.rate = rate

		self.sub = rospy.Subscriber('channel', cons_data, self.my_handler)
		self.pub = rospy.Publisher('channel', cons_data, queue_size=10)


	def my_handler(self, msg):
		print("Received message")
		print("   node_id     = %s" % str(msg.id))
		print("   data        = %s" % str(msg.data))

		if G(i,msg.id) == 1:
			self.x = consensus[consensus_type]([self.x, msg.data])
			print("Consensus update -->  x = %s" % str(self.x))

	def publish(self):
		msg = cons_data()
		msg.id   = self.id
		msg.data = x



def main_loop():

	rospy.init_node(NAME)

	node_id        = rospy.get_param('node_id', 1)
	consensus_type = rospy.get_param('consensus_type', 'max')
	init_value     = rospy.get_param('init_value', 7)
	#rate           = rospy.get_param('rate', 10)

	cons_node = consensus_node(node_id, consensus_type, init_value) #, rate)

	node_rate = rospy.Rate(rate)

	while not rospy.is_shutdown():
		cons_node.publish()
		node_rate.sleep()




if __name__ == '__main__':
	try:
		main_loop()
	except rospy.ROSInterruptException:
		pass