import web
 
urls = (
    '/db/', 'index',
    '/db/add','add'
    
)
 
app = web.application(urls, globals())
render = web.template.render('templates/')
db = web.database(dbn='mysql', host='127.0.0.1', port=3306,
                  db='forum', user='root', pw='123456')
 
class index:
    def GET(self):
       email = db.select('mintest')
       return render.index5(email)

class add:
    def POST(self):
        i=web.input()
        n=db.insert('mintest',email=i.title,NAME=i.email)
        raise web.seeother('/db/')
 
if __name__ == "__main__":
    app.run()
