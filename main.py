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


# Create a price for kalamansi
# stripe.Price.create(
#     currency="usd",
#     product="kalamansi",
#     unit_amount="150"
# )



@app.route('/', methods=['GET'])
def home():
    return "This is the homepage"


@app.route('/products', methods=['GET'])
def show_all_products():
    all_products = Product().get_all_products()
    print(all_products)
    return render_template('products.html', products=all_products)


def update_cart(data):
    #update the cart
    current_cart = []
    # current_cart.append({"key": 3})
    current_cart.append(data)
    # print(current_cart)
    return(current_cart)

@app.route('/cart', methods=['POST'])
def add_to_cart():
# I have price_id here
    data = request.form
    count = int(data['quantity'])
    price_id = data['price']
    # print(data)
    updated_cart = update_cart(data)
    print(updated_cart)
    return redirect(url_for("show_all_products"))

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