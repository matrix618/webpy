import web
 
urls = (
    '/picturepath/(.*)', 'picturepath'
    
)
 
app = web.application(urls, globals())
 
class picturepath:
    def GET(self,picpath):
        i = web.input(picpath=None,pictype=None)
        
        s="["+ str(i.picpath) + "],[" + str(i.pictype) + "]"
        
        return s
    
 
if __name__ == "__main__":
    app.run()
