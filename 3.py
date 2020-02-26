import web
 
urls = (
    '/index/(.*)', 'index'
    
)
 
app = web.application(urls, globals())
render = web.template.render('templates/')
 
class index:
    def GET(self,name):
        i = web.input(name=None,jj=None)
        return render.index1(i.name,i.jj)
    
 
if __name__ == "__main__":
    app.run()
