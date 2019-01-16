Проект Сотрудники
----------
frontend (vue spa): 
- vue 2.5.22 (https://ru.vuejs.org)
с использованием:
- bootstrap-vue (https://bootstrap-vue.js.org)
- vue-bootstrap-datetimepicker (https://github.com/ankurk91/vue-bootstrap-datetimepicker)

backend (python 3.6.5)
- реализация RESTAPI на tornado (https://www.tornadoweb.org/en/stable/)
с использованием:
- tornado-cors (https://github.com/globocom/tornado-cors)
- СУБД SQLite
----------
Установка под Windows, developer mode

1.frontend

cd frontend
npm install
npm install bootstrap-vue --save
npm install vue-bootstrap-datetimepicker --save

запуск: npm run dev

2.backend

python -m venv backend
cd backend/scripts
activate.bat
cd ..
pip install -r requirements.txt

запуск: python app.py dev

TODO:
- tornado-sqlalchemy