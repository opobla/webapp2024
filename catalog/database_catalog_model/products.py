from database_catalog_model import database


def get_all_products():
    db = database.get_db()
    cursor = db.cursor()
    postgreSQL_select_Query = "select name, description, price, sku, category from productos"

    cursor.execute(postgreSQL_select_Query)
    products = cursor.fetchall()

    response = []
    for product in products:
        response.append({
            "name": product[0],
            "description": product[1],
            "price": product[2],
            "sku": product[3],
            "category": product[4]
        })
    return response


def get_product_by_sku(sku):
    """Gets a product by its SKU from the 'productos' table.

    Args:
        conn: A psycopg2 connection object.
        sku: The SKU of the product to retrieve.

    Returns:
        The product as a dictionary, or None if not found.
    """
    conn = database.get_db()
    sql = "SELECT * FROM productos WHERE sku = %s"

    with conn.cursor() as cur:
        cur.execute(sql, (str(sku),))
        result = cur.fetchone()
        if result:
            return {
                'category': result[0],
                'description': result[1],
                'name': result[2],
                'price': result[3],
                'sku': result[4]
            }
        else:
            return None


def insert_product(category, description, name, price):
    """Inserts a new product into the 'productos' table.

    Args:
        category: The category of the product.
        description: The description of the product.
        name: The name of the product.
        price: The price of the product.

    Returns:
        The inserted product ID.
    """

    conn = database.get_db()
    sql = """
        INSERT INTO productos (category, description, name, price)
        VALUES (%s, %s, %s, %s)
        RETURNING sku;
    """
    with conn.cursor() as cur:
        cur.execute(sql, (category, description, name, price))
        product_id = cur.fetchone()[0]
        conn.commit()
        return product_id
