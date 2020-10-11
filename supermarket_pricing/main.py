# Simple prices => prices of an item
# sweet potato $0.79
# Complex prices => prices attached to a bundle of items
# 3 for $1
# $1.99/kg => what's the price of 200g?
# buy 2 get one free

# Does fractional money exists?
# yes, since you can pay with cards

# Audit trail of pricing decisions is needed?
# Yes. A pricing history containing the price and datetime must be added in each product.
# That way a trail can be made to verify the profit product_hist = [(1.00, 11/10/2020 17:55),...]

# Are costs and prices the same class of thing?
# No. Costs are related to what the owner pays for the product,
# prices are related to what the consumer will pay

# If a shelf of 100 cans is priced using "buy two get one free" how the stock is valued?
# The stock can be divided, using a new SKU to track down the prices of two items.
# ex.: 100 products => $100 sku 001
# when the promotion starts: 50 products $50 sku 001 and 50 products $25 sku 002
# When the client checks out if it has quantity % 2 = 0 the sku 002 should be used.
# Otherwise account for the escess with sku 001
