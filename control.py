import sys
import drivers

def run(request):
	turn = 'null'
	motor = 'null'

	try:
		turn = request.form['turn']
		drivers.turn(int(turn))
	except:
		turn = 'null'
	try:
		motor = request.form['motor']
		drivers.motor(int(motor))
	except:
		motor = 'null'

	return turn + ' ' + motor
