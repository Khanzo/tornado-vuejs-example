import tornado.web
import sqlite3
from tornado_cors import CorsMixin #CORS access-control-allow
import json
import datetime
from random import *

def _execute(query):
    #run sqllite db query
    connection = sqlite3.connect('sotrud.db')
    cursorobj = connection.cursor()
    try:
        cursorobj.execute(query)
        result = cursorobj.fetchall()
        connection.commit()
    except Exception:
        raise
    connection.close()
    return result
    

def verifyDatabase(): 
    #create tables
    query = 'CREATE TABLE IF NOT EXISTS sotrud (\
            id INTEGER PRIMARY KEY,\
            FIO TEXT,\
            Datr TEXT,\
            Phone TEXT,\
            Sex INTEGER,\
            Otdel TEXT)'    
    _execute(query)
    
    query = 'CREATE TABLE IF NOT EXISTS zarplati (\
            id INTEGER PRIMARY KEY,\
            Sotrud INTEGER,\
            Sumz FLOAT,\
            Datz TEXT)'    
    _execute(query)
    print('Init db')

class RandomHandler(CorsMixin, tornado.web.RequestHandler):
    #get random number
    CORS_ORIGIN = '*'
    
    def get(self):
        self.write({ 'randomNumber': str(randint(1, 100)) })
        
class MainHandler(CorsMixin, tornado.web.RequestHandler):
    
    CORS_ORIGIN = '*'
    
    def initialize(self, bundle_path):	
        self.bundle_path = bundle_path

    def get(self):	
        self.render('index.html', bundle_path = self.bundle_path)
        
class SotrudHandler(CorsMixin, tornado.web.RequestHandler):  
    #REST API sotrudniki
    CORS_ORIGIN = '*'
    CORS_METHODS = 'POST,DELETE,PUT,OPTIONS'
    CORS_CREDENTIALS = True
    CORS_HEADERS = 'access-control-allow-origin,authorization,content-type'
    
    def json_response(self, data, status_code=200):
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)
    
    def get(self, item_id = None):
        # sotrud for item_id info or all sotrud
        #curl -X "GET" http://localhost:5000/api/info/1        
        if item_id == None:
            query = '''select * from sotrud'''
        else:
            query = '''select * from sotrud where id = %s ''' %(item_id)
        rows = _execute(query) 
        resultat = []
        for row in rows:
            ro = {}
            ro["id"] = row[0]
            ro["fio"] = { 'id': row[0], 'fio': row[1] }
            ro["datr"] = row[2]            
            ro["phone"] = row[3]
            ro["sex"] = row[4]
            ro["otdel"] = row[5]
            resultat.append(ro)
        self.set_status(200) 
        self.json_response(json.dumps(resultat))       
        
    def put(self, item_id = None):
        # update info sotrud for item_id
        #curl -X "PUT" -d "fio=Ivanov Oleg Ptrenko&phone=1123344&sex=0&otdel=magazine&datr=11.03.1666" http://localhost:5000/api/info/3
        
        if item_id == None:         
            return self.finish("Invalid key")
        
        data = tornado.escape.json_decode(self.request.body)
        fio = tornado.escape.xhtml_escape(data.get('fio'))
        phone = tornado.escape.xhtml_escape(data.get('phone'))
        sex = int(data.get('sex'))
        otdel = tornado.escape.xhtml_escape(data.get("otdel"))
        datr = tornado.escape.xhtml_escape(data.get("datr"))
        
        query = '''update sotrud set FIO='%s', Datr='%s', Phone='%s', 
        Sex=%d, Otdel='%s' where id = %s''' %(fio, datr, phone, sex, otdel, item_id)
        _execute(query)
        self.set_status(200)
        
    def post(self):
        # new sotrud info
        #curl -d "fio=Ivanov Oleg Ptrenko&phone=1123344&sex=0&otdel=magazine&datr=11.03.1666" http://localhost:5000/api/info
        data = tornado.escape.json_decode(self.request.body)
        fio = tornado.escape.xhtml_escape(data.get('fio'))
        phone = tornado.escape.xhtml_escape(data.get('phone'))
        sex = int(data.get('sex'))
        otdel = tornado.escape.xhtml_escape(data.get("otdel"))
        datr = tornado.escape.xhtml_escape(data.get("datr"))
        
        query = '''insert into sotrud (FIO, Datr, Phone, Sex, Otdel) 
        values ('%s', '%s', '%s', %d, '%s') ''' %(fio, datr, phone, sex, otdel)
        _execute(query)
        self.set_status(200) 

    def delete(self, item_id = None):
        # delete sotrud for item_id
        #curl -X "DELETE" http://localhost:5000/api/info/1              
        if item_id == None:
            self.set_status(400)
            return self.finish("Invalid key")
        
        query = '''delete from sotrud where id = %s ''' %(item_id)
        _execute(query)
        self.set_status(200)
        
class ZarplataHandler(CorsMixin, tornado.web.RequestHandler):  
    #REST API zarplati
    CORS_ORIGIN = '*'
    CORS_METHODS = 'POST,DELETE,PUT,OPTIONS'
    CORS_CREDENTIALS = True
    CORS_HEADERS = 'access-control-allow-origin,authorization,content-type'
    
    def json_response(self, data, status_code=200):
        self.set_status(status_code)
        self.set_header("Content-Type", 'application/json')
        self.write(data)
    
    def get(self, item_id=None):
        # sotrud for item_id info or all sotrud     
        if item_id == None:
            self.set_status(400)
            return self.finish("Invalid key")
        
        query = '''select datz, (Select fio from sotrud where id = %s) as fio,
        sumz from zarplati where sotrud = %s ''' %(item_id,item_id)
        rows = _execute(query) 
        resultat = []
        for row in rows:
            ro = {}
            ro["datz"] = row[0]
            ro["fio"] = row[1] 
            ro["sumz"] = row[2] 
            resultat.append(ro)
        self.set_status(200) 
        self.json_response(json.dumps(resultat))       
        
        
    def post(self):
        # add zarplata info        
        data = tornado.escape.json_decode(self.request.body)        

        sotrud = int(data.get('sotrud'))
        sumz = float(data.get('sumz'))
        datr = datetime.date.today()
        
        query = '''insert into zarplati (sotrud, datz,sumz) 
        values (%d, '%s',%f) ''' %(sotrud, datr.strftime("%d-%m-%Y"),sumz)
        _execute(query)
        self.set_status(200) 