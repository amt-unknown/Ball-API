from concurrent.futures.process import _chain_from_iterable_of_lists
from operator import concat
from flask import (Blueprint, request, redirect, render_template, jsonify)
from flask_sqlalchemy import SQLAlchemy
from . import models

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

def create_dict(obj):
    return {
            'id': obj.id,
            'common_name': obj.common_name,
            'scientific_name': obj.scientific_name,
            'native_habitat': obj.native_habitat,
            'conservation_status': obj.conservation_status, 
            'fun_fact': obj.fun_fact

        }

def create_dict_list(lst):
    temp_lst = []
    for data in lst:
        temp_lst.append(create_dict(data))

    return temp_lst


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        native_habitat = request.form['native_habitat']
        conservation_status = request.form['conservation_status']
        fun_fact = request.form['fun_fact']

        new_reptile = models.Reptile(common_name=common_name, scientific_name=scientific_name, native_habitat=native_habitat, conservation_status=conservation_status, fun_fact=fun_fact)
        models.db.session.add(new_reptile)
        models.db.session.commit()

        return redirect('/reptiles')
    
    results = models.Reptile.query.all()


    return jsonify(create_dict_list(results))

@bp.route('/<int:id>', methods=['GET'])
def show(id):
    reptile = models.Reptile.query.filter_by(id=id).first()

    return create_dict(reptile)