import web
 
urls = (
    '/index(\d+)', 'index'
    
)
 
app = web.application(urls, globals())
 
class index:
    def GET(self,name):
        if not name:
            name = 'lala'
        return 'Hello,ID:' + name 
    
 
if __name__ == "__main__":
    app.run()
