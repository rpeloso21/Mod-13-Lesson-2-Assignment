from flask import Blueprint
from controllers.productController import save, find_all, find_all_pagination


product_blueprint = Blueprint('product_bp', __name__)

product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)
