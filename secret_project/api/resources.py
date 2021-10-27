import json

from flask import Response
from flask_restful import Resource, request

from secret_project.api.startup import product_repository
from secret_project.models.product import Product, AllProducts

Product.repository = product_repository
AllProducts.repository = product_repository


class ProductResource(Resource):
    def get(self, id=None):
        if id is not None:
            product = Product(prod_id=id)
            product.get()
            return Response(json.dumps(product.to_json()), status=200,
                            content_type="application/json")

        all_products = AllProducts()
        all_products.get_all()
        return Response(json.dumps(all_products.to_json()), status=200,
                        content_type="application/json")

    def post(self):
        body = request.json
        try:
            product = Product()
            product.create(prod_id=body["prod_id"], name=body["name"],
                           description=body["description"], price=body["price"])
            return Response(status=200, content_type="application/json")
        except Exception as e:
            error = {
                'error': str(e)
            }
            return Response(error, status=500, content_type="application/json")

    def put(self):
        pass

    def delete(self):
        pass
