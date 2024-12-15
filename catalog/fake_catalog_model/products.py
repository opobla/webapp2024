from faker import Faker
import uuid
import random


fake = Faker()
def generate_product(categories):
    product = {
        "name": fake.word(),
        "description": fake.sentence(),
        "price": fake.pyfloat(min_value=10, max_value=1000, positive=True),
        "sku": str(uuid.uuid4()),
        "category": random.choice(categories)
    }
    return product

# Generate 10 fake categories
categories = [fake.word() for _ in range(10)]

# Generate 1000 products using the generated categories
products = [generate_product(categories) for _ in range(10)]


def get_all_products():
    return products


def get_product_by_sku(sku):
  for product in products:
    if product['sku'] == str(sku):
      return product
  return None

