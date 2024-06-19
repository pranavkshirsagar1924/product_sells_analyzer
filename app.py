from flask import Flask,render_template,request,jsonify
import appy

app = Flask(__name__)

@app.route('/')
def reT():
    return render_template('index.html')

@app.route('/data',methods=['GET'])
def data():
    args = request.args.get('country')
    if args:
        print(args)
        country_data = appy.returnData(args)
        if True:
            return jsonify({'data': country_data})
        else:
            return jsonify({'error': 'No data found for the specified country'}), 404
    else:
        return jsonify({'error': 'Country parameter is required'}), 400

if __name__ == "__main__":
    app.run(debug=True)