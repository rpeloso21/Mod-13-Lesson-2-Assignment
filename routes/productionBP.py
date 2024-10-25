from flask import Blueprint
from controllers.productionController import save, find_all, find_employee_production


production_blueprint = Blueprint('production_bp', __name__)

production_blueprint.route('/', methods=['POST'])(save)
production_blueprint.route('/', methods=['GET'])(find_all)
production_blueprint.route('/employees', methods=['GET'])(find_employee_production)