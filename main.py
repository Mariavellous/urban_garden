import os
from flask import Flask, redirect, request, url_for, render_template
from flask_wtf import FlaskForm
from all_products import Product
import stripe
# This is test secret API key
stripe.api_key = 'sk_test_51LnxGxLeJ6gUVN1HtAzkLzp60PvEXngfpuB65r4t8Sue90iidTFvmkRfajTxiJB2YFPlNquktcSBr0ue5LiC4wzX00lf1EVPJN'

app = Flask(__name__)
MY_DOMAIN = 'http://localhost:5009'
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


### If product does not create product and price
# stripe.Product.create(
#     id="kalamansi",
#     name="Calamansi (Philippine lime)",
#     images=["https://www.justlovelylittlethings.com/wp-content/uploads/2019/05/315ED45D-CF90-4F3A-AA61-B263F027A41F.jpeg"],
#     unit_label="lb",
# )

# Create a price for kalamansi
# stripe.Price.create(
#     currency="usd",
#     product="kalamansi",
#     unit_amount="150"
# )

# @app.route('/products', methods=['GET'])
# def show_all_products():
#     products = stripe.Product.list()
#     prices = stripe.Price.list()
#     return render_template('products.html', products=products.data, prices=prices.data)

@app.route('/', methods=['GET'])
def home():
    return "This is the homepage"


@app.route('/products', methods=['GET'])
def show_all_products():
    all_products = Product().get_all_products()
    print(all_products)
    return render_template('products.html', products=all_products)
#
# class AddCartForm(FlaskForm):
#     submit= SubmitField()

@app.route('/cart', methods=['POST'])
def add_to_cart():
# I have price_id here
    data = request.form
    count = int(data['count'])
    price_id = data['price_id']
    print(data)
    return render_template('success.html')

@app.route('/create-checkout-session', methods=['GET'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            cancel_url=MY_DOMAIN + '/cancel',
            success_url=MY_DOMAIN + '/success',
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1LoDIxLeJ6gUVN1H5wcvMEuS',
                    'quantity': 5,
                    'adjustable_quantity': {
                        'enabled': True,
                        'minimum': 1,
                        'maximum': 10,
                    },
                },
            ],
            mode='payment',
            currency='usd',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

@app.route('/cancel', methods=['GET'])
def cancel():
    return render_template('cancel.html')

if __name__ == "__main__":
    app.run(port=5009)