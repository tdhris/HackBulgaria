def final_position(commands, limitA, limitB):
	position = 0
	number_of_commands = len(commands)

	for i in range(number_of_commands):
		if commands[i] == 'R' and position != limitB:
			position+=1
		elif commands[i] == 'L' and position != -limitA:
			position-=1

	return position