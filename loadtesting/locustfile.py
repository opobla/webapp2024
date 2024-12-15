import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_all_catalog(self):
        self.client.get("/products")

    @task
    def manager_create_product(self):
        product = {
            'category': 'testing',
            'description': 'testing description',
            'name': 'test_name',
            'price': 123.45
        }
        self.client.post("/products", json=product)

