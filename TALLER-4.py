import sqlite3

# Conectar a la base de datos
def connect():
    return sqlite3.connect("database.db")

conn = connect()
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        quantity INTEGER,
        category TEXT
    )
""")
conn.commit()
conn.close()

def create_product(nombre, precio, cantidad, categoria):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)", 
                   (nombre, precio, cantidad, categoria))
    conn.commit()
    conn.close()
    print(f"Producto {nombre} creado con éxito.")

def read_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    
    print("\nLista de productos:")
    for product in products:
        print(product)

def update_product_price(id, precio_nuevo):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (precio_nuevo, id))
    conn.commit()
    conn.close()
    print(f"Precio del producto con ID {id} actualizado.")

def update_product_quantity(id, nueva_cantidad):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (nueva_cantidad, id))
    conn.commit()
    conn.close()
    print(f"Cantidad del producto con ID {id} actualizada.")

def delete_product(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print(f"Producto con ID {id} eliminado.")

def menu():
    while True:
        print("\nMenú de Gestión de Productos")
        print("1. Crear Producto")
        print("2. Ver Productos")
        print("3. Actualizar Precio")
        print("4. Actualizar Cantidad")
        print("5. Eliminar Producto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = int(input("Precio: "))
                cantidad = int(input("Cantidad disponible: "))
                categoria = input("Categoría: ")
                create_product(nombre, precio, cantidad, categoria)
            elif opcion == "2":
                read_products()
            elif opcion == "3":
                id = int(input("ID del producto: "))
                nuevo_precio = int(input("Nuevo precio: "))
                update_product_price(id, nuevo_precio)
            elif opcion == "4":
                id = int(input("ID del producto: "))
                nueva_cantidad = int(input("Nueva cantidad: "))
                update_product_quantity(id, nueva_cantidad)
            elif opcion == "5":
                id = int(input("ID del producto a eliminar: "))
                delete_product(id)
            elif opcion == "6":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()
