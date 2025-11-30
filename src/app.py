from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
'''
Функция реализует перевод из килограммы в фунты и наоборот по адресу /weight и
перевод из миль в километры по адресу /length
'''
@app.route('/weight', methods=['GET'])
def weight():
    try:
        if 'lb' in request.args:
            lb = float(request.args.get('lb'))
            kg = lb * 0.453592
            return f"{lb} фунтов - {round(kg, 2)} килограммов"
        else:
            kg = float(request.args.get('kg'))
            lb = kg * 2.20462
            return f"{kg} килограммов - {round(lb, 2)} фунтов"
    except (ValueError, TypeError):
        return "Введите число!"

@app.route('/length', methods=['GET'])
def length():
    try:
        if 'mil' in request.args:
            mil = float(request.args.get('mil'))
            km = mil * 1.60934
            return f"{mil} миль - {round(km, 2)} километров"
        else:
            km = float(request.args.get('km'))
            mil = km * 0.621371
            return f"{km} километров - {round(mil, 2)} миль"
    except (ValueError, TypeError):
        return "Введите число!"
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)

