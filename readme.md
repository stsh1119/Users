### Users task
Technologies: Python, SQLlite

- Data represents a list of users (users.json file) and user statistics on the website (users_statistic.json file)
- Create a sript, that will check if needed tables are present in DB, and if not - will create them and add data from .json files
- Develop a funcionality for selecting a list of users and information about them
(users table and users_statistic table ) with pagination (**amount of users and current page will** be receieved from request coming from Front-end)
- Develop functionality for selecting statistics data (users_statistic table)
using **user id** with ability to **filter results by date** ("from" and "till" will be receieved from request)
- All data coming from Front-end should be validated and suit certain format