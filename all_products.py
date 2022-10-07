import stripe
# This is test secret API key
stripe.api_key = 'sk_test_51LnxGxLeJ6gUVN1HtAzkLzp60PvEXngfpuB65r4t8Sue90iidTFvmkRfajTxiJB2YFPlNquktcSBr0ue5LiC4wzX00lf1EVPJN'


# # Responsible for getting all the products and it's prices
# def show_all_products():
#     products = stripe.Product.list().data

# responsible for getting product/price from Prices API
def get_prices():
    prices = stripe.Price.list().data
    list_prices = {}
    for item in prices:
        price = item.unit_amount / 100
        # list_prices.append(price)
        key = item.product
        # list_prices[key] = price
        list_prices[key] = {"price": price}
    return list_prices

print(get_prices())

# responsible for getting data from Products API
def get_product_data():
    products = stripe.Product.list().data
    list_products = {}
    for item in products:
        id = item.id
        name = item.name
        image = item.images[0]
        list_products[id] = {"name": name,
                             "image": image,
                             }
    return list_products

print(get_product_data())

def get_all_products():
    prices = get_prices()
    # print(prices)
    products = get_product_data()
    # print(products)
    all_products = {}
    for key in products:
        # TODO: make values as dictionary instead of list
        all_products[key] = [products[key], prices[key]]
    return all_products

print(get_all_products())

