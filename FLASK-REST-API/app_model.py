from app import Product, db
import snoop

snoop.install(out="./backend/app_model.txt", overwrite=True)   # Tracking Backend Functionality

model = Product.query.all
modelGet = Product.query.get
dbAdd = db.session.add
dbCommit = db.session.commit
dbDelete = db.session.delete

@snoop
def model_choice():
    return "1. Update Name, 2. Update Description, 3. Update Price, 4. Update Quantity"

@snoop
def newProduct():
    name = input("Name: ")
    description = input("Description: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    return name, description, price, qty

@snoop
def modelProduct(id):
    print(model_choice())
    status_update = int(input("Enter Choice: "))
    if status_update == 1:
        new_name = input("New Name: ")
        modelGet(id).name = new_name
    if status_update == 2:
        new_description = input("New Description: ")
        modelGet(id).description = new_description
    if status_update == 3:
        new_price = float(input("New Price: "))
        modelGet(id).price = new_price
    if status_update == 4:
        new_qty = int(input("New Quantity: "))
        modelGet(id).qty = new_qty
    print(f"{modelGet(id)} Updated!")

@snoop
def modelView(id):
    print(f"ID: {modelGet(id).id}, Name: {modelGet(id).name}, Description: {modelGet(id).description}, Price: {modelGet(id).price}, Quantity: {modelGet(id).qty}")

