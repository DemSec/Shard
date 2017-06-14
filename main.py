from flask import Flask, request, render_template#, send_file
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
        return render_template('index.html')

@app.route('/', methods=['POST'])
def control():
        import control # Breaks if import is global
        control.run(request)
        return render_template('index.html')

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)
