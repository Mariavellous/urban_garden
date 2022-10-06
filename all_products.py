import stripe
# This is test secret API key
stripe.api_key = 'sk_test_51LnxGxLeJ6gUVN1HtAzkLzp60PvEXngfpuB65r4t8Sue90iidTFvmkRfajTxiJB2YFPlNquktcSBr0ue5LiC4wzX00lf1EVPJN'


# Responsible for getting all the products and it's prices
def show_all_products():
    products = stripe.Product.list().data


# how to get a dictionary of product and its price
def get_prices():
    prices = stripe.Price.list().data
    list_prices = {}
    for item in prices:
        price = item.unit_amount / 100
        # list_prices.append(price)
        key = item.product
        list_prices[key] = price
    return list_prices



