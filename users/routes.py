from flask import jsonify, request
import sqlite3
from users import app
from users.db import (create_tables_if_needed, insert_data_into_tables,
                      get_data_from_db_per_page, get_user_stats_between_two_dates)


@app.before_first_request
def check_if_tables_exist() -> bool:
    connection = sqlite3.connect('users/users.db')
    with connection:
        cursor = connection.cursor()
        users_table = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'users'").fetchone()
        user_stats = cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'users_statistic'")
        user_stats.fetchone()
        if users_table is not None and user_stats is not None:
            app.logger.info("DB Exists")
        else:
            create_tables_if_needed()
            insert_data_into_tables()


@app.route('/', methods=['GET'])
def home():
    return jsonify('Home Page')


@app.route('/api/v1/fetch_users', methods=['GET'])
def fetch_users():
    page = request.args.get('page')
    amount = request.args.get('amount')
    if page and amount:
        try:
            return jsonify(get_data_from_db_per_page(int(amount), int(page))), 200
        except ValueError:
            return jsonify('Bad request: either page or amount is not an integer'), 400
    return jsonify('Bad request: either page or amount is missing'), 400
