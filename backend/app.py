import os
import sys
import tornado.ioloop
import tornado.web
import handlers      

def make_app(bundle_path, debug):
    return tornado.web.Application(
       template_path = os.path.join(os.path.dirname(__file__), "views"),
       static_path = os.path.join(os.path.dirname(__file__), "public"),
       debug = debug,
       handlers = [
           (r"/", handlers.MainHandler, dict(bundle_path=bundle_path)),
           (r".*/api/random", handlers.RandomHandler),
           (r"/api/all", handlers.SotrudHandler),
           (r"/api/info", handlers.SotrudHandler),
           (r"/api/info/(\d+$)", handlers.SotrudHandler),
           (r"/api/zarplata", handlers.ZarplataHandler),
           (r"/api/zarplata/(\d+$)", handlers.ZarplataHandler)
           ],
       )

if __name__ == "__main__":   
    debug = False
    handlers.verifyDatabase()
    
    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        bundle_path = 'http://localhost:5000/'
        debug = True
    app = make_app(bundle_path, debug)
    app.listen(5000)
    print('http://localhost:5000')
    tornado.ioloop.IOLoop.current().start()
