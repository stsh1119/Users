import sqlite3
import json
from users.date_validator import validate_date_format
from users.utils import prettify_pagination_output, prettify_user_stats
from users import app


def create_tables_if_needed() -> None:
    '''Checks if tables are present in db, if not - creates them'''
    connection = sqlite3.connect('users/users.db')
    with connection:
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        cursor.execute("""create table if not exists users (
                          id integer primary key,
                          first_name text not null,
                          last_name text not null,
                          email text not null unique,
                          gender text not null,
                          ip_address text not null)
                          """
                       )

        cursor.execute("""create table if not exists users_statistic (
                          user_id integer not null,
                          date text not null,
                          page_views integer not null,
                          clicks integer,
                          foreign key(user_id) references users(id) on delete cascade
                          )"""
                       )
    app.logger.info("Tables created successfully")


def insert_data_into_tables() -> None:
    with open('src/users.json') as users_file:
        data = json.load(users_file)  # reads data from the users file
        connection = sqlite3.connect('users/users.db')
        with connection:
            cursor = connection.cursor()
            for user in data:
                cursor.execute(
                            """insert into users values(:id, :first_name, :last_name, :email, :gender, :ip_address)""",
                            {
                                'id': user['id'],
                                'first_name': user['first_name'],
                                'last_name': user['last_name'],
                                'email': user['email'],
                                'gender': user['gender'],
                                'ip_address': user['ip_address']
                            }
                            )

        with open('src/users_statistic.json') as users_file:
            data = json.load(users_file)  # reads data from users_statistic file
            connection = sqlite3.connect('users/users.db')
            with connection:
                cursor = connection.cursor()
                for user in data:
                    cursor.execute(
                                """insert into users_statistic values(:user_id, :date, :page_views, :clicks)""",
                                {
                                    'user_id': user['user_id'],
                                    'date': user['date'],
                                    'page_views': user['page_views'],
                                    'clicks': user['clicks']
                                }
                                )
    app.logger.info("Data is added to the tables")


def get_data_from_db_per_page(amount_on_page: int, page_number: int) -> list:
    connection = sqlite3.connect('users/users.db')
    with connection:
        cursor = connection.cursor()
        query_result = cursor.execute("""
                                      select u.*, sum(us.page_views) total_clicks, sum(us.clicks) total_page_views
                                      from users u, users_statistic us
                                      where u.id = us.user_id
                                      group by u.id
                                      limit ?
                                      offset ?
                                      """,
                                      (amount_on_page, (page_number-1)*amount_on_page)
                                      ).fetchmany(amount_on_page)
    json_result = prettify_pagination_output(query_result)

    return json_result


def get_user_stats_between_two_dates(user_id: int, start_date: str, end_date: str) -> list:
    connection = sqlite3.connect('users/users.db')
    start_date = validate_date_format(start_date)
    end_date = validate_date_format(end_date)
    with connection:
        cursor = connection.cursor()
        query_result = cursor.execute("""
                                      select *
                                      from users_statistic
                                      where user_id = ?
                                      and date >= ?
                                      and date <= ?
                                      """,
                                      (user_id, start_date, end_date)
                                      ).fetchall()
    json_result = prettify_user_stats(query_result)
    return json_result
