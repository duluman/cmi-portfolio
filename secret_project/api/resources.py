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
            response = Response(status=200, content_type="application/json")
        except ValueError as ve:
            error = {
                'error': str(ve)
            }
            response = Response(response=json.dumps(error), status=400, content_type="application/json")
        except Exception as e:
            error = {
                'error': str(e)
            }
            response = Response(response=json.dumps(error), status=500, content_type="application/json")
        return response

    def put(self):
        body = request.json
        prod_id = body.get("prod_id", None)
        if prod_id is None:
            error = {
                "error": "Invalid id provided."
            }
            return Response(response=json.dumps(error), status=400, content_type="application/json")
        data = body.get("data", None)
        if data is None or data == {}:
            error = {
                "error": "Invalid product data provided."
            }
            return Response(response=json.dumps(error), status=400, content_type="application/json")
        try:
            product = Product(prod_id=prod_id)
            product.edit(name=data.get("name", None),
                         description=data.get("description", None),
                         price=data.get("price", None))
            response = Response(status=200, content_type="application/json")
        except ValueError as ve:
            error = {
                "error": str(ve)
            }
            response = Response(response=json.dumps(error), status=400, content_type="application/json")
        except Exception as e:
            error = {
                "error": str(e)
            }
            response = Response(response=json.dumps(error), status=500, content_type="application/json")
        return response

    def delete(self):
        body = request.json
        prod_ids = body.get("prod_ids", None)
        if prod_ids is None:
            error = {
                "error": "Missing product ids."
            }
            response = Response(response=json.dumps(error), status=400, content_type="application/json")
        else:
            try:
                for prod_id in prod_ids:
                    product = Product(prod_id=prod_id)
                    product.delete()
                response = Response(status=200, content_type="application/json")
            except Exception as e:
                error = {
                    'error': str(e)
                }
                response = Response(response=json.dumps(error), status=500, content_type="application/json")
        return response
