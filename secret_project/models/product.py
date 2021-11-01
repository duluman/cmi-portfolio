import json


class Product:
    repository = None

    def __init__(self, prod_id=None, name=None, description=None, price=None):
        self.prod_id = prod_id
        self.name = name 
        self.description = description
        self.price = price
    
    def create(self, **kwargs):
        if kwargs:
            self.prod_id = kwargs["prod_id"]
            self.name = kwargs["name"] 
            self.description = kwargs["description"]
            self.price = kwargs["price"]
        if self.prod_id is None:
            raise ValueError("Invalid product id. Try again with a valid product id.")
        if self.price is None or self.price < 0:
            raise ValueError("Invalid product price. Try again with a price >= 0.")
        product_json = self.to_json()
        self.repository.insert_one(product_json)

    def get(self):
        projection = {
            'prod_id': 1,
            'description': 1
        }
        result = self.repository.get_by_field_value("prod_id", self.prod_id, projection=projection)
        if result:
            result = result[0]
            self.name = result.get("name", None)
            self.description = result.get("description", None)
            self.price = result.get("price", None)

    def edit(self, name=None, description=None, price=None):
        if name is not None:
            self.name = name 
        if description is not None:
            self.description = description
        if price is not None and price >= 0: 
            self.price = price
        product_json = self.to_json()
        self.repository.update_one_by_field(product_json, "prod_id")

    def delete(self):
        self.repository.delete_many("prod_id", self.prod_id)

    def to_json(self):
        product_json = {
            "prod_id": self.prod_id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }
        return product_json


class AllProducts:
    repository = None

    def __init__(self):
        self.products = []

    def get_all(self):
        raw_results = self.repository.get_all()
        if raw_results:
            for result in raw_results:
                product = Product(result["prod_id"],
                                  result["name"],
                                  result["description"],
                                  result["price"])
                self.products.append(product)

    def to_json(self):
        products_json = [product.to_json() for product in self.products]
        return products_json
