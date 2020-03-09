import web
 
urls = (
    '/db/', 'index'
    
)
 
app = web.application(urls, globals())
render = web.template.render('templates/')
db = web.database(dbn='mysql', host='127.0.0.1', port=3306,
                  db='forum', user='root', pw='123456')
 
class index:
    def GET(self):
       email = db.select('mintest')
       return render.index4(email)    
    
 
if __name__ == "__main__":
    app.run()
