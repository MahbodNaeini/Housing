from flask import Flask, render_template, request, redirect, url_for
from models.house import House
from models.owner import Owner
from models.sell import Sell

app = Flask(__name__)

houses = []
owners = []
sells = []

@app.route('/')
def index():
    return render_template('index.html', houses=houses, owners=owners, sells=sells)

@app.route('/add_house', methods=['POST'])
def add_house():
    address = request.form['address']
    state = request.form['state']
    city = request.form['city']
    room = request.form['room']
    measure = request.form['measure']
    owner_id = request.form['owner_id']

    owner = next((o for o in owners if o.get_national_code() == owner_id), None)
    if owner:
        house = House(address, state, city, room, measure, owner)
        houses.append(house)
    return redirect(url_for('index'))

@app.route('/add_owner', methods=['POST'])
def add_owner():
    name = request.form['name']
    surname = request.form['surname']
    national_code = request.form['national_code']
    
    owner = Owner(name, surname, national_code)
    owners.append(owner)
    return redirect(url_for('index'))

@app.route('/sell_house', methods=['POST'])
def sell_house():
    price = request.form['price']
    house_id = int(request.form['house_id'])
    buyer = request.form['buyer']
    date_time = request.form['date_time']
    
    house = houses[house_id]
    sell = Sell(price, house, buyer, date_time)
    sells.append(sell)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
