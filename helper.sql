PRAGMA foreign_keys = ON; -- to enable Foeign Keys reference

SELECT name -- to check if tables exist
FROM sqlite_master
WHERE type = 'table'
AND name = 'users_statistic'
OR name = 'users';

create table if not exists users (
                    id integer primary key,
                    first_name text not null,
                    last_name text not null,
                    email text not null unique,
                    gender text not null,
                    ip_address text not null
                    );

create table if not exists users_statistic (
                              user_id integer not null,
                              date text not null,
                              page_views integer not null,
                              clicks integer,
                              foreign key(user_id) references users(id) on delete cascade
                             );


select u.*, sum(us.page_views) total_clicks, sum(us.clicks) total_page_views
from users u, users_statistic us
where u.id = us.user_id
group by u.id
limit {value}
offset {value};
