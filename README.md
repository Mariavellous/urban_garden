### Current Project
# E-commerce website 

  The Urban Garden is an online shopping website selling organic fruits and vegetables in my mom's backyard garden located in the heart of San Jose, CA. The website will allow her to sell the products online and reach a wider audience. 
* I add various fruits and vegetables that my mom plants in her garden, including each product's name, price, and image, to the Stripe database by making a request to the `Products` and `Prices` API 
* I create a `Product` class that is responsible for returning all the products and their price
* The `/product` route makes a request to the Stripe's Products API to display the collection of the products available for purchase.
* The shoppers can add different products to the shopping cart, and when ready for checkout, the app leverages Stripe's payment processing platform to complete the shopper's transaction. 

## Deployment

1. Create/update `requirements.txt`

```
pip freeze > requirements.txt
```
