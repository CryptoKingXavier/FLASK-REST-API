# Setting Up Database in Terminal
>>> flask shell

# Initializing Database
# From Flask Shell
>>> db.create_all()
>>> from app import Product

# Showing all products
>>> Product.query.all()

# Showing individual product
>>> Product.query.get(id)

# Modelling the product
>>> Product(name, description, price, qty)

# Adding to the database the modelled product
>>> db.session.add(Product(name, description, price, qty))

# Committing to the database the modelled product
>>> db.session.commit()

# Deleting modelled product from database
>>> db.session.delete(Product.query.get(id))

# Updating Product
>>> Product.query.get(id).name = new_name
>>> Product.query.get(id).description = new_description
>>> Product.query.get(id).price = new_price
>>> Product.query.get(id).qty = new_quantity

# To Run Flask App
>>> python app.py -h "Hostname" -p "Port Name" -d "Debug Boolean Value"