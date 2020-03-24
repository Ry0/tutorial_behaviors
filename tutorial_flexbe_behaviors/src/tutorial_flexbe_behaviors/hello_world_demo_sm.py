#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.wait_state import WaitState
from flexbe_states.log_state import LogState
from flexbe_manipulation_states.moveit_to_joints_state import MoveitToJointsState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Mar 24 2020
@author: Ryo
'''
class HelloWorldDemoSM(Behavior):
	'''
	test
	'''


	def __init__(self):
		super(HelloWorldDemoSM, self).__init__()
		self.name = 'Hello World Demo'

		# parameters of this behavior
		self.add_parameter('waiting_time', 5)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		hello = "baka!!"
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.target_joint = [0,0,0]

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('Initial_Wait',
										WaitState(wait_time=self.waiting_time),
										transitions={'done': 'test_moveit'},
										autonomy={'done': Autonomy.Off})

			# x:27 y:171
			OperatableStateMachine.add('Print_Greeting',
										LogState(text=hello, severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.High})

			# x:172 y:148
			OperatableStateMachine.add('test_moveit',
										MoveitToJointsState(move_group='Gantry', joint_names=["small_long_joint", "torso_rail_joint", "torso_base_main_joint"], action_topic='/ariac/gantry/move_group'),
										transitions={'reached': 'Print_Greeting', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_config': 'target_joint'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
