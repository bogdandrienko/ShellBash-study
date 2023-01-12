# TODO EXTRA ###########################################################################################################

def extra():
    """

    """
    pass

# TODO EXTRA ###########################################################################################################

#

# TODO SYSTEMS #########################################################################################################

def ubuntu_first_setup():
    """
    # todo basic
    # create ubuntu VM (2023_01_05_ubuntu_22_04_desktop)
    # change VM settings (network, ram, core, shared folder, shared clipboard...)
    # setup ubuntu desktop lts (Normal installation (user + user-PC) + download updates + install third-party software)
    # todo basic

    # todo insert vbox-guest-additions
    # insert guest additions iso => Files >> CD Drive (VBOX_GAs_6.1.32) >> autorun.sh (Right-click) >> Run as a Program
    sudo adduser user vboxsf
    # eject guest additions
    # todo insert vbox-guest-additions

    # todo update system
    # update system with app ubuntu-software

    # update system repositories and dependencies
    sudo apt-get update -y
    sudo apt update -y
    sudo apt-get upgrade -y
    sudo apt upgrade -y
    # todo update system

    # todo customization
    # set dark theme and color (settings -> appearance)
    # disable show personal folder (settings -> appearance)
    # set panel to bottom (settings -> appearance -> dock)
    # set backgroud image (settings -> backgroud)
    # remove apps from panel
    # add russian language (settings -> region & language)
    # add russian to keyboard (settings -> keyboard)
    # hide bottom(left) panel
    sudo apt install gnome-shell-extensions -y
    # >> Apps >> Extension manager >> disable ubuntu dock
    # hide top panel
    sudo apt install gnome-shell-extension-manager -y
    # >> Apps >> Extension manager >> Browse >> Hide Top Bar >> Install >> Apps >> gnome-shell-extensions (disable all checkboxes without 'show in overview')
    # todo customization

    # todo install modules
    # main modules
    sudo apt-get install -y curl wget git build-essential gcc make libpq-dev unixodbc-dev zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev gettext

    # additional modules
    sudo apt-get install -y nginx gunicorn docker-compose postgresql postgresql-contrib redis openssh-server
    sudo snap install -y --classic certbot gh
    # todo install modules

    # todo install google-chrome
    cd ~/Downloads
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
    sudo rm google-chrome-stable_current_amd64.deb
    # todo install google-chrome

    # todo install python
    sudo apt-get install -y python3-dev python3-pip python3-venv
    # todo install python

    # todo install go
    sudo apt install -y golang-go
    # todo install go

    # todo install rust
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    # set 1
    source "$HOME/.cargo/env"
    # todo install rust

    # todo install node-js
    curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
    source ~/.bashrc
    nvm ls-remote
    nvm install 18.10.0
    nvm use 18.10.0
    # todo install node-js

    # todo install python ide
    sudo snap install pycharm-professional --classic
    # todo install python ide

    # todo install go ide
    sudo snap install -y goland --classic
    # todo install go ide

    # todo install rust ide
    sudo snap install intellij-idea-ultimate --classic
    # todo install rust ide

    # todo install react ide
    sudo snap install code --classic
    # todo install react ide

    # todo install github-desktop
    cd ~/Downloads
    sudo wget https://github.com/shiftkey/desktop/releases/download/release-3.1.1-linux1/GitHubDesktop-linux-3.1.1-linux1.deb
    sudo dpkg -i GitHubDesktop-linux-3.1.1-linux1.deb
    sudo rm GitHubDesktop-linux-3.1.1-linux1.deb
    # todo install github-desktop

    # todo install putty-ssh-client
    sudo apt install -y putty
    # todo install putty-ssh-client

    # todo install postgresql-pgadmin4
    curl -fsSL https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/pgadmin.gpg
    sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list'
    sudo apt install -y pgadmin4-desktop
    # todo install postgresql-pgadmin4

    # TODO install virtualbox
    sudo apt-get install -y virtualbox virtualbox-ext-pack virtualbox-guest-additions-iso virtualbox-guest-utils dkms virtualbox-dkms
    # TODO install virtualbox
    """
    pass

def windows_first_setup():
    """
    update system
    install DWS and SSD Mini Tweaker
    insert guest-additions and install
    install all need programs
    """
    pass

def ubuntu():
    """
    # enter as root user
    sudo -i

    # update os
    sudo apt-get update -y
    sudo apt update -y
    sudo apt-get upgrade -y
    sudo apt upgrade -y

    # clear terminal
    clear

    # remove file
    sudo rm temp.txt

    # create file
    touch file

    # change file / create file
    sudo nano new.json

    # move file
    sudo mv /temp1/data.json /temp2/data.json

    # todo change file role
    sudo chmod +x

    # todo check all dependencies
    sudo apt install -f

    # reboot system
    sudo reboot

    # clear cached dependencies
    sudo apt autoremove -y
    sudo apt-get autoremove -y

    # ufw role
    sudo ufw allow 'Nginx Full'

    # todo work with system workers
    sudo service nginx start

    sudo systemctl status gunicorn.service

    sudo systemctl enable --now gunicorn.service
    sudo systemctl disable gunicorn

    sudo systemctl start gunicorn
    #sudo systemctl stop gunicorn
    sudo systemctl restart gunicorn

    sudo systemctl daemon-reload
    # todo work with system workers

    # TODO work with openssh-server
    sudo systemctl start ssh
    sudo systemctl restart ssh
    # TODO work with openssh-server

    # todo disable swap
    free -m
    swapon -s
    swapon -show
    sudo swapoff -v /swapfile
    sudo rm -f /swapfile
    # todo disable swap

    # todo enable swap
    dd if =/dev/zero of=/swapfile bs=1024 count=1048576
    # todo enable swap

    # todo clear system cache
    # login to root user
    sudo -i
    # clear all caches (echo 1|echo 2|echo 3)
    sync; echo 3 > /proc/sys/vm/drop_caches
    # todo clear system cache
    """
    pass

def debian():
    """
    su
    apt install sudo
    nano /etc/sudoers
    su debian
    sudo nano /etc/apt/sources.list
    # <file> /etc/apt/sources.list
    deb http://deb.debian.org/debian bullseye main
    deb-src http://deb.debian.org/debian bullseye main
    deb http://http.us.debian.org/debian/ testing non-free contrib main
    # </file> /etc/apt/sources.list
    """
    pass

def windows():
    """
    # remove folder with data
    rmdir /Q /S react

    # move folder with data
    move frontend/build react

    # todo shell variables
    cd ~
    mkdir Downloads
    cd Downloads
    set /p project_variable= "Please set your project name: "
    IF "%project_variable%"=="" (set project_variable="project_folder")
    mkdir %project_variable% && cd %project_variable%
    set /p env_variable= "Please set your virtual environment name: "
    IF "%env_variable%"=="" (set env_variable="env")
    python -m venv %env_variable%
    call %env_variable%/Scripts/activate.bat
    # todo shell variables
    """
    pass

# TODO SYSTEMS #########################################################################################################

#

# TODO ADDITIONAL ######################################################################################################

def git_ubuntu():
    """
    git init
    git clone https://... project
    git add urls.py
    git add -A
    git commit -a -m"description"
    git push
    git pull
    """
    pass

def pip_ubuntu_windows():
    """
    # todo linux
    cd ~/Downloads
    mkdir web && cd web
    pip3 install --upgrade pip --user

    python3 -m venv env
    source env/bin/activate
    pip install --upgrade pip --user

    pip install lxml
    # todo linux

    # todo windows
    cd ~/Downloads
    mkdir web && cd web
    python.exe -m pip install --upgrade pip
    pip install env

    python -m venv env
    call .\env\Scripts\activate.bat
    python.exe -m pip install --upgrade pip

    pip install lxml
    # todo windows
    """
    pass

# TODO ADDITIONAL ######################################################################################################

#

# TODO SQL #############################################################################################################

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

# TODO SQL #############################################################################################################

#

# TODO WEB BACKEND #####################################################################################################

def web_framework_structure():
    """
    База языка
        Переменные
        Функции
        Циклы
        Классы и структуры
    База фреймворка:
        Развёртывание
        Маршрутизация
        Контроллеры
        Работа с базой данных
        ОРМ
        Шаблонизатор
        Кэширование
        Автодокументация
        Логирование
    """
    pass

def django_ubuntu_python():
    """
    pip3 install --upgrade pip --user
    python3 -m pip3 install --upgrade pip

    cd ~/Downloads
    mkdir django-rest-api && cd django-rest-api
    python3 -m venv env
    source env/bin/activate

    pip install --upgrade pip --user
    python -m pip install --upgrade pip

    pip install wheel
    pip install django django-environ django-grappelli gunicorn psycopg2-binary pillow
    pip install djangorestframework djangorestframework-simplejwt django-cors-headers celery redis
    pip install -r requirements.txt
    pip freeze > requirements.txt

    django-admin startproject django_settings .
    django-admin startapp django_app

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser --username admin --email bogdandrienko@gmail.com

    python manage.py collectstatic --noinput
    python manage.py createcachetable
    python manage.py check --database default

    python manage.py runserver 0.0.0.0:8000
    gunicorn --bind 0.0.0.0:8000 django_settings.wsgi
    """
    pass

def go():
    """
    # todo create new project
    cd ~/Downloads
    mkdir gin-rest-api && gin-rest-api
    go mod init example/gin-rest-api

    # todo add needs and remove trash libs
    go mod tidy

    # todo download all libs
    go get

    # todo download selected lib
    go get -u github.com/lib/pq
    go get -u github.com/xuri/excelize/v2
    go get -u github.com/gin-gonic/gin

    # todo create binary(linux) or .exe(windows) temp file and run it
    go run main.go

    # todo create binary(linux) or .exe(windows) file
    go build main.go
    go build -o x.exe -C bar


    """
    pass

def go_gin_rest_api():
    """
    cd ~/Downloads
    mkdir gin-rest-api && gin-rest-api
    go mod init example/gin-rest-api
    cd gin-rest-api
    nano main.go
    <file>
    package main

    import (
        "net/http"

        "github.com/gin-gonic/gin"
    )

    func main() {
        r := gin.New()

        r.GET("/books", listBooksHandler)
        r.POST("/books", createBookHandler)
        r.DELETE("/books/:id", deleteBookHandler)

        r.Run()
    }

    type Book struct {
        ID     string `json:"id"`
        Title  string `json:"title"`
        Author string `json:"author"`
    }

    var books = []Book{
        {ID: "1", Title: "Harry Potter", Author: "J. K. Rowling"},
        {ID: "2", Title: "The Lord of the Rings", Author: "J. R. R. Tolkien"},
        {ID: "3", Title: "The Wizard of Oz", Author: "L. Frank Baum"},
    }

    func listBooksHandler(c *gin.Context) {
        c.JSON(http.StatusOK, books)
    }

    func createBookHandler(c *gin.Context) {
        var book Book

        if err := c.ShouldBindJSON(&book); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{
                "error": err.Error(),
            })
            return
        }

        books = append(books, book)

        c.JSON(http.StatusCreated, book)
    }

    func deleteBookHandler(c *gin.Context) {
        id := c.Param("id")

        for i, a := range books {
            if a.ID == id {
                books = append(books[:i], books[i+1:]...)
                break
            }
        }

        c.Status(http.StatusNoContent)
    }
    </file>

    go get
    go run main.go
    # browse http://127.0.0.1:8080/books
    """
    pass

def rust():
    """
    # todo create new project
    cd ~/Downloads
    cargo new actix-rest-api

    # todo create binary(linux) or .exe(windows) temp file and run it
    cargo run

    # todo create binary(linux) or .exe(windows) file
    cargo build
    """
    pass

def rust_actix_rest_api():
    """
    # create rust project
    cd ~/Downloads
    cargo new actix-rest-api
    cd actix-rest-api

    nano Cargo.toml
    <file>
    ...
    [dependencies]
    actix-web = "4"
    </file>

    nano src/main.rs
    <file>
    use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};

    #[get("/")]
    async fn hello() -> impl Responder {
        HttpResponse::Ok().body("Hello world!")
    }

    #[post("/echo")]
    async fn echo(req_body: String) -> impl Responder {
        HttpResponse::Ok().body(req_body)
    }

    async fn manual_hello() -> impl Responder {
        HttpResponse::Ok().body("Hey there!")
    }

    #[actix_web::main]
    async fn main() -> std::io::Result<()> {
        HttpServer::new(|| {
            App::new()
                .service(hello)
                .service(echo)
                .route("/hey", web::get().to(manual_hello))
        })
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
    }
    </file>
    cargo run
    # browse http://127.0.0.1:8080/
    """
    pass

# TODO WEB #############################################################################################################

#

# TODO WEB FRONTEND ####################################################################################################

def react_ubuntu_javascript_node():
    """
    # todo create new project
    cd ~/Downloads
    mkdir web && cd web
    npx -y  create-react-app frontend --template redux-typescript
    npx -y create-react-app frontend --template pwa-typescript

    npm install prettier axios react-redux react-router-dom
    npm install react-bootstrap react-router-bootstrap react-player

    npm install
    npm init

    npm start
    npm run build
    """
    pass

# TODO WEB FRONTEND ####################################################################################################

#

# TODO WEB #############################################################################################################

def gunicorn_ubuntu_python_django():
    """
    sudo nano /etc/systemd/system/gunicorn.socket
    <file>
    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/run/gunicorn.sock

    [Install]
    WantedBy=sockets.target
    </file>


    sudo nano /etc/systemd/system/gunicorn.service
    <file>
    [Unit]
    Description=Gunicorn for the Django example project
    Requires=gunicorn.socket
    After=network.target

    [Service]
    Type=notify

    User=bogdan
    Group=www-data

    RuntimeDirectory=gunicorn
    WorkingDirectory=/home/bogdan/web
    ExecStart=/home/bogdan/web/env/bin/gunicorn --workers 5 --bind unix:/run/gunicorn.sock backend.wsgi:application
    ExecReload=/bin/kill -s HUP $MAINPID
    KillMode=mixed
    TimeoutStopSec=5
    PrivateTmp=true

    [Install]
    WantedBy=multi-user.target
    </file>
    sudo systemctl daemon-reload
    sudo systemctl start gunicorn
    sudo systemctl enable --now gunicorn.service
    sudo systemctl daemon-reload
    sudo systemctl restart gunicorn
    sudo systemctl status gunicorn.service
    #sudo systemctl disable gunicorn
    #sudo systemctl stop gunicorn
    """
    pass

def nginx_ubuntu_gunicorn_python_django():
    """
    sudo usermod -aG user www-data

    sudo nano /etc/nginx/sites-available/web-km-kz-http.conf
    <file>
    server {
    listen 80;
    listen [::]:80;

    server_name web.km.kz www.web.km.kz;

    root /home/bogdan/web;

    location /.well-known/acme-challenge/ {}

    location /favicon.ico {
        alias /home/bogdan/web/static/logo.png;

        access_log off; log_not_found off;

        expires max;
    }

    location /robots.txt {
        alias /home/bogdan/web/static/robots.txt;

        access_log off; log_not_found off;

        expires max;
    }

    location /static/ {
        alias /home/bogdan/web/static/;

        expires max;
    }

    location /media/ {
        alias /home/bogdan/web/static/media/;

        expires max;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_buffering off;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
    }
    </file>

    sudo ln -s /etc/nginx/sites-available/web-km-kz-http.conf /etc/nginx/sites-enabled/web-km-kz-http.conf
    sudo service nginx start
    sudo systemctl status nginx.service
    sudo ufw allow 'Nginx Full'
    sudo systemctl reload nginx.service

    sudo mv /etc/nginx/sites-available/web-km-kz-http.conf /etc/nginx/sites-available/web.km.kz-https.conf
    sudo nano /etc/nginx/sites-available/web-km-kz-http.conf
    <file>
    server {
    listen 80;
    listen [::]:80;

    server_name web.km.kz www.web.km.kz;

    root /home/bogdan/web;

    location /.well-known/acme-challenge/ {}

    location / {
        return 301 https://$server_name$request_uri;
    }
    }
    </file>

    sudo certbot certonly --webroot -w /home/bogdan/web -d web.km.kz -m bogdandrienko@gmail.com --agree-tos
    sudo openssl dhparam -out /etc/nginx/dhparam.pem 2048

    sudo nano /etc/nginx/sites-available/web-km-kz-https.conf
    <file>
    server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    ssl_certificate /etc/letsencrypt/live/web.km.kz/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/web.km.kz/privkey.pem;

    ssl_session_timeout 1d;
    ssl_session_cache shared:MozSSL:10m;

    ssl_dhparam /etc/nginx/dhparam.pem;

    ssl_protocols TLSv1.2;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;

    ssl_stapling on;
    ssl_stapling_verify on;

    ssl_trusted_certificate /etc/letsencrypt/live/web.km.kz/chain.pem;

    resolver 1.1.1.1;

    client_max_body_size 30M;

    server_name web.km.kz www.web.km.kz;

    root /home/bogdan/web;

    location /.well-known/acme-challenge/ {}

    location /favicon.ico {
        alias /home/bogdan/web/static/logo.png;

        access_log off; log_not_found off;

        expires max;
    }

    location /robots.txt {
        alias /home/bogdan/web/static/robots.txt;

        access_log off; log_not_found off;

        expires max;
    }

    location /static/ {
        alias /home/bogdan/web/static/;

        expires max;
    }

    location /media/ {
        alias /home/bogdan/web/static/media/;

        expires max;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_buffering off;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
    }
    </file>

    sudo ln -s /etc/nginx/sites-available/web-km-kz-https.conf /etc/nginx/sites-enabled/web-km-kz-https.conf
    sudo service nginx start
    sudo systemctl status nginx.service
    sudo ufw allow 'Nginx Full'
    sudo systemctl reload nginx.service
    """
    pass

def celery_python_django():
    """

    # todo check redis
    redis-server
    redis-cli
    ping # PONG
    exit
    # todo check redis

    source env/bin/activate
    pip install celery redis django
    pip freeze > requirements.txt

    # django_setting/celery.py
    import os
    from celery import Celery

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_settings.settings")
    app = Celery("django_settings")
    app.config_from_object("django.conf:settings", namespace="CELERY")
    app.autodiscover_tasks()
    # django_setting/celery.py

    # django_setting/__init__.py
    from .celery import app as celery_app

    __all__ = ("celery_app",)
    # django_setting/__init__.py

    # django_setting/settings.py
    CELERY_APP_TIMEZONE = 'Asia/Almaty'
    CELERY_APP_TASK_TRACK_STARTED = True
    CELERY_APP_TASK_TIME_LIMIT = 1800

    CELERY_BROKER_URL = "redis://localhost:6379"
    CELERY_RESULT_BACKEND = "redis://localhost:6379"
    # CELERY_BROKER_URL = "amqp://myuser:mypassword@localhost:5672/myvhost"
    # CELERY_RESULT_BACKEND = "redis://localhost:6379"
    # django_setting/settings.py

    # sh (env)
    python -m celery -A django_settings worker -l info
    # sh (env)

    # django_app/celery.py
    # parsing(get data from another web-sites), analyze, reports, image refactor, send mass mail
    @shared_task
    def add(x, y):
        return x + y

    @shared_task
    def count_users():
        time.sleep(3.0)
        return User.objects.count()

    @shared_task
    def send_mass_email(recipients: list, message: dict, skip_error=True):
        results = []
        for recipient in recipients:
            success = False
            error = ""
            try:
                # send_mail(recipient, message)
                pass
            except Exception as error:
                print(error)
                error = error
                if skip_error is False:
                    break
            else:
                success = True
            finally:
                results.append((success, error))
        # return results  # [(True, ""), (False, "timeout error")]
        return [(True, ""), (False, "timeout error")]
    # django_app/celery.py

    # django_app/view.py
    from django_app import celery as current_celery
    from celery.result import AsyncResult
    from django_settings.celery import app as celery_app

    task_id = current_celery.send_mass_email.apply_async([1, 2, 3], {}, skip_error=True, countdown=20)  #
    old_task_id = "33779111-0f42-4a96-bdec-d5643e57a018"

    result = AsyncResult(old_task_id, app=celery_app)
    # print()

    if result.state != "PENDING":
    result = f"status: {result.state} | result: {result.get()}"
    else:
    result = f"status: {result.state} | result: {None}"
    print(result)
    # django_app/view.py
    """
    pass

def docker_python_django():
    """
    mkdir web && cd web
    python3 -m venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install wheel
    pip install Django gunicorn psycopg2 Pillow
    django-admin startproject django_settings .
    django-admin startapp core
    cd core
    mkdir management && cd management
    nano __init__.py       #ctr s ctrl x
    mkdir commands && cd commands
    nano __init__.py  #ctr s ctrl x

    nano wait_for_db.py
    # wait_for_db.py
    import time
    from django.db import connections
    from django.db.utils import OperationalError
    from django.core.management import BaseCommand


    class Command(BaseCommand):
        '''Django command to pause execution until db is available'''

        def handle(self, *args, **options):
            self.stdout.write('Waiting for database...')
            db_conn = None
            while not db_conn:
                try:
                    db_conn = connections['default']
                except OperationalError:
                    self.stdout.write('Database unavailable, waititng 1 second...')
                    time.sleep(1)

            self.stdout.write(self.style.SUCCESS('Database available!'))
    # wait_for_db.py

    nano django_settings/settings.py
    # settings.py
    import os

    DEBUG = os.environ.get("DEBUG", True)
    ALLOWED_HOSTS = ["*"]

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'core',
    ]

    DATABASES = {
        "default": {
            "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
            "USER": os.environ.get("SQL_USER", "user"),
            "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
            "HOST": os.environ.get("SQL_HOST", "localhost"),
            "PORT": os.environ.get("SQL_PORT", "5432"),
        }
    }

    STATIC_ROOT = Path(BASE_DIR/"static")
    # settings.py

    nano .env
    # .env
    # django
    DEBUG=1


    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=django_db
    SQL_USER=django_usr
    SQL_PASSWORD=Qwerty12345!
    SQL_HOST=db
    SQL_PORT=5432

    # postgres
    POSTGRES_DB=django_db
    POSTGRES_USER=django_usr
    POSTGRES_PASSWORD=Qwerty12345!
    # .env

    python3 manage.py runserver 0.0.0.0:8000
    cd ..

    nano docker-compose.yml
    # docker-compose.yml
    version: '3.7'

    services:

      db:
        container_name: db
        image: postgres:latest
        restart: on-failure
        networks:
          - main
        env_file:
          - ./web/.env
        volumes:
          - postgres_data:/var/lib/postgresql/data
      web:
        container_name: web
        restart: on-failure
        depends_on:
          - db
        networks:
          - main
        build:
          context: .
          dockerfile: ./Dockerfile
        env_file:
          - ./web/.env
        image: web
        volumes:
          - .:/web
        ports:
          - 8000:8000
        command: >
          sh -c "python manage.py wait_for_db && python manage.py collectstatic --noinput &&
                 python manage.py makemigrations --noinput && python3 manage.py migrate --noinput &&
                 python manage.py runserver 0.0.0.0:8000"
                 # gunicorn django_settings.wsgi -bind 0.0.0.0:8000
    volumes:
      postgres_data:
    networks:
       main:
         driver: bridge
    # docker-compose.yml

    nano Dockerfile
    # Dockerfile
    FROM python:latest

    ENV PYTHONUNBUFFERED 1
    ENV PYTHONDONTWRITEBYTECODE 1

    RUN apt-get update && apt-get install -y build-essential && apt-get install -y libpq-dev && apt-get install -y gettext \
      && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && rm -rf /var/lib/apt/lists/*

    RUN mkdir /web_build
    COPY ./web /web_build

    COPY ./web/requirements.txt /requirements.txt
    RUN pip install -r /requirements.txt

    WORKDIR /web_build
    # Dockerfile

    nano start.sh
    # start.sh
    #!/bin/bash

    docker-compose run web sh -c "django-admin startproject django_settings app"
    # sudo docker-compose build
    sudo docker-compose up --build
    # sudo docker-compose up -d --build
    # sudo docker compose down
    # start.sh

    source start.sh
    """
    pass

def certbot_ubuntu_python_django():
    """
    sudo systemctl list-timers | grep 'certbot\|ACTIVATES'
    sudo nano /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh
    <file>
    #!/bin/bash
    /usr/bin/systemctl reload nginx.service
    sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh
    sudo certbot renew --dry-run
    </file>
    """
    pass

def curl_ubuntu():
    """
    # curl -v -X GET -H 'x-id:1' 127.0.0.1:8080/todos
    # curl -v -X POST -H 'x-id:1' 127.0.0.1:8080/todos -d '{"userId":2,"id":2,"title":"11111111111111","completed":true}'

    // Create
    // curl -v -X POST 127.0.0.1:8080/books -d '{"id":4,"title":"Amon Ra","author":"V.Pelevin"}'

    // Read
    // curl -v -X GET 127.0.0.1:8080/books/1

    // Read all
    // curl -v -X GET 127.0.0.1:8080/books

    // Update
    // curl -v -X PUT 127.0.0.1:8080/books/1 -d '{"title":"War and peace","author":"N.Tolstoy"}'

    // Delete
    // curl -v -X DELETE 127.0.0.1:8080/books/1
    """
    pass

# TODO WEB #############################################################################################################
