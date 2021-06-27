{% comment %} install virtualenvironment {% endcomment %}
pip install virtualenv

{% comment %} create venv {% endcomment %}
virtualenv jina_la_env

{% comment %} activate venv {% endcomment %}
source path_to_virtualenv/script/activate


{% comment %} install requirements  {% endcomment %}
pip install -r requirements
--------------------------------------------------------------------------------->

conf database
--------------------------------------------------------------------------------->



{% comment %} query database  {% endcomment %}
py manage.py makemigrations

{% comment %} migrate to database {% endcomment %}
py manage.py migrate

{% comment %} create admin au superuser {% endcomment %}
py manage.py createsuperuser

{% comment %} runserver {% endcomment %}
py manage.py runserver



