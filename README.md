# PICTURE VIEWER

**picture-viewer** is a FullStack application which continuously which lists and shows all Pictures added to the database in a paginated response. It provides all the CRUD functionalities for the pictures. It also provides feature to search Pictures by names.

---

**Deployment Link**: [picture-viewer](https://picture-viewer.herokuapp.com/)  
**Source Code Link**: [picture-viewer](https://github.com/Pratyush1606/picture-viewer)

## **Technologies**

* Publicly Deployed on Heroku: [picture-viewer](https://picture-viewer.herokuapp.com/)
* [Django](https://www.djangoproject.com/): Django builds better web apps with less code
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Rest APIs with Django
* Database used: [SQLite](https://www.sqlite.org/index.html) (for local testing), [PostgreSQL](https://www.psycopg.org/) (for deployment)

---

## **API Reference**

### **GET** /

This API lists the first 9 Gallery Images as Cards(3 cards per row) in paginated form on the 1st Page. Next 9 entries on the 2nd Page and so on.

**Example Successful Response**

***Status Code***

`200`

Rendered response will be in paginated form with `Previous` and `Next` button to naviagate.

![pictures_paginated_list](https://drive.google.com/uc?export=view&id=18zzOEizc-a2vgsQ-WSjEM7qfaUro5G6V)

### **GET** /?query={query string}

This API searches Image by names.

**Example Successful Response**

***Status Code***

`200`

![picture_search](https://drive.google.com/uc?export=view&id=1S80_-RBx4FblcOxEG7IbzF8HwDhBdROK)

### **GET** /show/:id

This API lists details of images. This will be on click of the above Card.

**Example Successful Response**

***Status Code***

`200`

Rendered response with `Delete` and `Edit` Button.

![picture_detail](https://drive.google.com/uc?export=view&id=1a5bSl8YXs9JnW5gj1oDP57aNVu_MuzAz)

### **GET** /new

This API shows a form for adding new images. The form contains Image Name, Image URL & Image details as mandatory fields to be filled.

**Example Successful Response**

***Status Code***

`200`

![picture_add](https://drive.google.com/uc?export=view&id=12IKAC0qVCfJWiCx7ZDBTDhIPC23M25FS)

### **POST** /

This API submits the above form and add it to the database.

**Example Successful Response**

***Status Code***

`201`

After the image gets added to the database, the app redirects to list the images.

### **GET** /:id/edit

This API shows a form which has a prefilled Image Name & it must be possible to change Image URL & Image Details.

**Example Successful Response**

***Status Code***

`200`

Rendered response with the image edit form

![picture_edit](https://drive.google.com/uc?export=view&id=1o1r0zXVhIAW2VNmcDkwRBefzDMN5nSOk)

### **PUT** /:id/edit

This API submits the above form and change the appropriate details in the database.

**Example Successful Response**

***Status Code***

`200`

After the image gets updated in the database, the app redirects to list the images.

### **DELETE** /delete/:id

This API deletes that particular image(with selected id) from the database.

**Example Successful Response**

***Status Code***

`200`

After the image gets updated in the database, the app redirects to list the images.

---

## **Local Setup**

* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python [here](https://www.python.org/downloads/).

* Get the Source Code, either Clone the repository or use the zip file

  * Using HTTPS

    ```sh
    git clone https://github.com/Pratyush1606/picture-viewer.git
    ```
  
  * Using SSH

    ```sh
    git clone git@github.com:Pratyush1606/picture-viewer.git
    ```

* Download [pip](https://pip.pypa.io/en/stable/installing/) and add it to the path

* Change your working directory to the the cloned folder

    ```bash
    cd path/to/picture-viewer
    ```

* Download all the dependencies

    ```bash
    pip install -r requirements.txt
    ```

    Use `pip3` if `pip` not working

* Make a `.env` file in this directory only and put the following

    ```python
    DJANGO_SECRET_KEY = django-insecure-%a37a2uf4oz8h=bue_7)7p_&r1tqr&dlh7+-3r+*h)+y)@p9!u
    DJANGO_DEBUG = True
    ```

  * While putting `DEBUG = False`, remember to modify `ALLOWED_HOSTS` (for just quick reference, modify as `ALLOWED_HOSTS = ['*']`)

  * For generating a Django ***SECRET_KEY***, many different sites are there. This [site](https://miniwebtool.com/django-secret-key-generator/) can be used for quick reference.

### Before proceeding further, make sure ```Directory``` looks like

```
picture-viewer
├── pic_app
|    ├── migrations
|    ├── templates
|    |    ├── image_add.html
|    |    ├── image_detail.html
|    |    ├── image_edit.html
|    |    └── image_list.html
|    ├── __init__.py
|    ├── admin.py
|    ├── apps.py
|    ├── models.py
|    ├── pagination.py
|    ├── serializers.py
|    ├── tests.py
|    ├── urls.py
|    └── views.py
├── picture_viewer
|   ├── __init__.py
|   ├── settings.py
|   ├── asgi.py
|   ├── wsgi.py
|   └── urls.py
├── screenshots
├── .gitignore
├── .env
├── manage.py
├── Procfile
├── README.md
└── requirements.txt
```

* Migrate to the database

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

    Use `python3` if `python` not working

    After this, you would see a new file named `db.sqlite3` in your parent folder

* Run server

    ```sh
    python manage.py runserver
    ```

---

## **Customizations**

* **Pagination** can be customized by modifying the parameters in `CustomPagination` class present in `pic_app/pagination.py`

* The correspnding result in pagination can be obtained using the parameter `p`.
Example url is `https://picture-viewer.herokuapp.com/?p=2`
