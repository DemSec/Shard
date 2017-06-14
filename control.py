import sys
import drivers

def run(request):
        try:
                if (len(request.form['run_mode']) > 0):
                        run_mode = request.form['run_mode']
                        drivers.run_mode()
                else:
                        run_mode = 'null'
        except:
                run_mode = 'null'

        try:
                turn = int(request.form['turn'])
                drivers.turn(turn)
        except:
                turn = 'null'

        try:
                motor = int(request.form['motor'])
                drivers.motor(motor)
        except:
                motor = 'null'

        return 'null'
