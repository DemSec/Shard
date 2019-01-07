import sys
import drivers

def run(request):
	turn = 'null'
	motor = 'null'

	#try:
	#	if (len(request.form['run_mode']) > 0):
	#		run_mode = request.form['run_mode']
	#		drivers.run_mode()
	#	else:
	#		run_mode = 'null'
	#except:
	#	run_mode = 'null'

	#try:
	#	turn = request.form['turn']
	#	drivers.turn(int(turn))
	#except:
	#	turn = 'null'

	#try:
	#	motor = request.form['motor']
	#	drivers.motor(int(motor))
	#except:
	#	motor = 'null'

	#try:
	#	lights = int(request.form['lights'])
	#	drivers.lights(lights)
	#except:
	#	lights = 'null'

	drivers.turn(int(request.form['turn']))
	drivers.motor(int(request.form['motor']))

	text = turn + ' ' + motor
	return text
