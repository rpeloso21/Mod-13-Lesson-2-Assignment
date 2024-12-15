from flask import Blueprint
from controllers.productController import save, find_all, find_all_pagination, top_selling_products, produced_by_date


product_blueprint = Blueprint('product_bp', __name__)

product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)
product_blueprint.route('/top_selling', methods=['GET'])(top_selling_products)
product_blueprint.route('/by_date', methods=['GET'])(produced_by_date)
