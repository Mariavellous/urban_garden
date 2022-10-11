import stripe
# This is test secret API key
stripe.api_key = 'sk_test_51LnxGxLeJ6gUVN1HtAzkLzp60PvEXngfpuB65r4t8Sue90iidTFvmkRfajTxiJB2YFPlNquktcSBr0ue5LiC4wzX00lf1EVPJN'

class Product:
    def __init__(self):
        pass

    # responsible for getting product/price from Prices API
    def get_prices(self):
        prices = stripe.Price.list().data
        list_prices = {}
        for item in prices:
            price = item.unit_amount / 100
            # list_prices.append(price)
            key = item.product
            # list_prices[key] = price
            list_prices[key] = {"price": price}
        return list_prices

    # print(get_prices())

    # responsible for getting products data from Products API
    def get_product_data(self):
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

    # print(get_product_data())


    # Responsible for getting all the products' data and its' prices in one
    def get_all_products(self):
        prices = self.get_prices()
        products = self.get_product_data()
        all_products = {}
        for key in products:
            all_products[key] = [products[key], prices[key]]
        return all_products

    #print(get_all_products())

# all_products = Product()
# print(all_products.get_product_data())