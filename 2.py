import web
 
urls = (
    '/index', 'index'
    
)
 
app = web.application(urls, globals())
 
class index:
    def GET(self):
        return 'Hello,mk'
    
 
if __name__ == "__main__":
    app.run()
