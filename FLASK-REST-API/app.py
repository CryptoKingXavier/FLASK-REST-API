from flask import Flask, request, jsonify, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, snoop

snoop.install(out="./backend/app.txt", overwrite=True)   # Tracking Backend Functionality

app = Flask(__name__)  # Init App
basedir = os.path.abspath(os.path.dirname(__file__))  # Path for locating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')  # Setting up database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # Initialize db
ma = Marshmallow(app)  # Initialize marshmallow

# Database Setup
@snoop
def DBSetup():
    return "Setting Up Database!"
    db.create_all()


# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200), unique=True)
    price = db.Column(db.Float, unique=True)
    qty = db.Column(db.Integer, unique=True)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# Initialize Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@app.route('/404')
@snoop
def error_404():
    return render_template("404.html", title="PAGE NOT FOUND")

@app.route('/jquery-404')
@snoop
def jquery_404():
    return render_template("jquery_404.html", title="ITEMS NOT FOUND")

# Home Page
@app.route('/')
@snoop
def index():
    return render_template("index.html", title="Home Page")

# Create a Product
@app.route('/add_product/<name>/<description>/<price>/<qty>', methods=['GET'])
@snoop
def add_product(name, description, price, qty):
    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()  # Committing to database
    product = Product.query.all()[-1]
    return render_template("jsonify_product.html", products=product, md="New Product")

@app.route('/new', methods=['GET', 'POST'])
@snoop
def new():
    if request.method == 'POST':
        name = request.form['product-name']
        description = request.form['product-description']
        price = request.form['product-price']
        qty = request.form['product-quantity']
        if (name=="" and description=="" and price=="" and qty==""):
            return redirect('/404')
        elif (name=="" or description=="" or price=="" or qty==""):
            return redirect('/404')
        else:
            return redirect(f'/add_product/{name}/{description}/{price}/{qty}')
    else:
        return render_template('product_new.html', title="New Product Home")


@app.route('/product_update/<id>/<name>/<description>/<price>/<qty>', methods=['GET'])
@snoop
def product_update(id, name, description, price, qty):
    product = Product.query.get(id)
    product.name = name
    product.description = description
    product.price = price
    product.qty = qty
    db.session.commit()  # Committing to database
    return render_template("jsonify_product.html", products=product, md="Update Product")

@app.route('/update', methods=['GET', 'POST'])
@snoop
def update():
    if request.method == 'POST':
        id = request.form['product-id']
        name = request.form['product-name']
        description = request.form['product-description']
        price = request.form['product-price']
        qty = request.form['product-quantity']
        if (id=="" and name=="" and description=="" and price=="" and qty==""):
            return redirect('/404')
        elif (id=="" or name=="" or description=="" or price=="" or qty==""):
            return redirect('/404')
        else:
            return redirect(f'/product_update/{id}/{name}/{description}/{price}/{qty}')
    else:
        return render_template('product_update.html', title="Product Update Home")


# Delete Single Product
@app.route('/product_delete/<id>', methods=['GET'])
@snoop
def product_delete(id):
    product = Product.query.get(id)
    db.session.delete(product)  # Removing Product
    db.session.commit()
    return render_template("jsonify_product.html", products=product, md="Delete Product")

@app.route('/delete', methods=['GET', 'POST'])
@snoop
def delete():
    if request.method == 'POST':
        id = request.form['product-id']
        product = Product.query.get(id)
        return redirect(f'/product_delete/{id}')
    else:
        return render_template("product_delete.html", title="Product Delete Home")


# Get Single Product
@app.route('/product/<id>', methods=['GET'])
@snoop
def get_product(id):
    if len(Product.query.all()) == 0:
        return redirect('/404')
    else:
        product = Product.query.get(id)
        result = product_schema.dump(product)
        return render_template("jsonify_product.html", products=product, md="View Product")


@app.route('/map_product', methods=['GET', 'POST'])
@snoop
def map_product():
    if request.method == 'POST':
        id = request.form['product-id']
        product = Product.query.get(id)
        return redirect(f'/product/{id}')
    else:
        return render_template("product_view.html", title="Product View Home")


# Get All Products
@app.route('/products', methods=['GET'])
@snoop
def get_products():
    if len(Product.query.all()) == 0:
        return redirect('/jquery-404')
    else:
        all_products = Product.query.all()
        result = products_schema.dump(all_products)
        return render_template("jsonify_products.html", products=result)
        # return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
