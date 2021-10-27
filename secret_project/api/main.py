from flask import Flask
from flask_restful import Api

from secret_project.api.resources import ProductResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/products', 'products/<string:id>')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
