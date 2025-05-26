from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/soma')
def soma():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return jsonify({"resultado": x + y})

@app.route('/multiplicacao')
def multiplicacao():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return jsonify({"resultado": x * y})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

