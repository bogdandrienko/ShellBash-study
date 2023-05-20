
def postgresql_ubuntu():
    """
    # todo postgresql actions
    sudo systemctl status postgresql
    sudo systemctl stop postgresql
    sudo systemctl restart postgresql
    # todo postgresql actions

    # create password for postgres
    sudo passwd postgres

    # login to postgres user
    sudo -i -u postgres

    # logout to postgres user
    exit

    # enter to SQL database
    psql
    psql postgres

    # database list
    \l

    # table list
    \d

    # unknown
    \c pg_db
    \connect pg_db

    # quit from database
    \q
    \quit

    # todo create new user and database
    # postgres-user
    createuser pgs_usr
    createdb pgs_db -O pgs_usr

    # postgres-psql
    CREATE USER pgs_usr WITH PASSWORD '12345Qwerty!';
    CREATE DATABASE pgs_db OWNER pgs_usr;

    # change password
    alter user pgs_usr with password '12345Qwerty!';

    # grant role
    GRANT ALL PRIVILEGES ON DATABASE pgs_db TO pgs_usr;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to pgs_usr;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to pgs_usr;
    GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to pgs_usr;

    # todo check 1
    CREATE TABLE zarplata ( id serial PRIMARY KEY, username VARCHAR ( 50 ) UNIQUE NOT NULL, salary INT );

    select * from zarplata;

    insert into zarplata (username, salary) VALUES ('Bogdan', '60000'), ('Alice', '80000');

    delete from zarplata where username = 'Bogdan';
    # todo check 1

    # todo check 2
    create table users_new (id serial not null unique, username varchar(255) not null, date_register timestamp not null default now(), active_status bool default 'false');
    alter table users_new drop column registered_at;
    alter table users_new add column registered_at timestamp not null default now();
    \l
    \d
    insert into users_new (username, active_status) values ('Alice', 'false');
    select * from users_new;
    \q
    exit
    # todo check 2

    # todo check 3
    create table books (id serial not null unique, title varchar(255) not null, author varchar(255) not null);
    \q
    exit
    # todo check 3

    # todo share data on net
    sudo nano /etc/postgresql/14/main/postgresql.conf
    <file> /etc/postgresql/14/main/postgresql.conf
    listen_addresses = '*'
    <file> /etc/postgresql/14/main/postgresql.conf

    sudo nano /etc/postgresql/14/main/pg_hba.conf
    <file> /etc/postgresql/14/main/pg_hba.conf
    host    all             all             192.168.0.165/32         scram-sha-256
    host    all             all             all         scram-sha-256
    host    all             all             all         trust (!danger)
    <file> /etc/postgresql/14/main/pg_hba.conf
    # todo share data on net

    """
    pass
