logic == True


if logic:

''' Test LED '''
	# while:
	# 	wait(250)
	# 	small_led = 0
	# 	wait(250)
	# 	small_led = 1
	# 	if keyPressed():
	# 		break

	def autonomous_direction():
		""" 
		The position_input will turn right if set to 1,
		left if set to 0 and remain unsteered if set to 0.5

		:param steer_block_L: Controls the left steering block
		:param steer_block_R: Controls the right steering block
		:param ditance_sensor_L: Returns 1 if left senor detects obstacle, else returns 0
		:param ditance_sensor_R: Returns 1 if right senor detects obstacle, else returns 0
		"""
		if ditance_sensor_L.detected() == 1:
			steer_block_L.position_input = 1
			steer_block_R.position_input = 1
		else:
			if ditance_sensor_R.detected() == 1:
				steer_block_L.position_input = 0
				steer_block_R.position_input = 0
			else:
				steer_block_L.position_input = 0.5
				steer_block_R.position_input = 0.5

	def signal_led():
		"""
		:param led_activation: LED will be lit if set to 1, not if set to 0.
		"""
		if ditance_sensor_L or ditance_sensor_R == 1:
			led_activation = 1
		else: led_activation = 0

	def autonomous_throttle():
		"""
		If nothing is detected by the Target Detector,
		Throtlle power to rear wheels will be set to 30%.
		If obstacle is detected, throttle power will be killed
		and continuous brakes will be applied.
		
		:param throttle_input: 0 to 1, adjusts throttle %
		:param continuous_brake: 0 or 1, toggles braking
		:param continuous_spin_L: Controls the rear-left wheel axis 
		:param continuous_spin_R: Controls the rear-right wheel axis 
		"""
		if target_detector.target_detected == 0:
			continuous_spin_L.throttle_input = 0.3
			continuous_spin_R.throttle_input = 0.3
		else:
			continuous_spin_L.throttle_input = 0
			continuous_spin_R.throttle_input = 0

			continuous_spin_L.continuous_brake = 1
			continuous_spin_R.continuous_brake = 1

