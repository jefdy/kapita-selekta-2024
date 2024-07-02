from flask import Flask, send_from_directory
from flask_restful import Api
from controller.products_controller import ProductsController

# Flask setup
app = Flask(__name__, static_folder='frontend', static_url_path='')
api = Api(app)

# Setup API routes
api.add_resource(ProductsController, '/products', '/products/<string:productId>')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
