import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        cantidad INTEGER,
        Categoria TEXT
    )
""")
conn.commit()
conn.close()
# Crea un producto en la base de datos con los datos proporcionados y los imprime en consola
def create_product(nombre, precio, cantidad, categoria):
    cursor.execute("INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)", 
                   (nombre, precio, cantidad, categoria))
    conn.commit()
    print(f"Producto {nombre} creado con éxito.")
# Lee los productos de la base de datos y los imprime
def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    
    print("\nLista de productos:")
    for product in products:
        print(product)
# Actualiza el precio de un producto en la base de datos y lo imprime en consola
def update_product_price(id, precio_nuevo):
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (id, precio_nuevo))
    conn.commit()
    print(f"Precio del producto con ID {id} actualizado.")
# Actualiza la cantidad de un producto en la base de datos y lo imprime en consola 
def update_product_quantity(id, nueva_cantidad):
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (id, nueva_cantidad))
    conn.commit()
    print(f"Cantidad del producto con ID {id} actualizada.")
# Elimina un producto de la base de datos con el ID proporcionado y lo imprime en consola
def delete_product(id):
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    print(f"Producto con ID {id} eliminado.")

