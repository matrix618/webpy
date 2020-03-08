import web
import datetime


urls = (
    '/picturepath/(.*)', 'picturepath',
    '/upload', 'Upload'
)
 
app = web.application(urls, globals())
 
class picturepath:
    def GET(self,picpath):
        i = web.input(picpath=None,pictype=None)
        
        s="["+ str(i.picpath) + "],[" + str(i.pictype) + "]"
        
        return s

 

class Upload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><title>Upload</title></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""
    def POST(self):
        time1=datetime.datetime.now()

        areyouok=False
        
        x = web.input(myfile = {})
 
        if 'mykey' in x:
            bkey=x.mykey
            if bkey != 'xxxxx':
                return areyouok
        
        filedir = 'images' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath = x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename = filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
#            fout.write(x.myfile.value) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
            areyouok=True
             
        time2=datetime.datetime.now()
        print(time2-time1)

        return areyouok
##        raise web.seeother('/upload')
        
if __name__ == "__main__":
    app.run()
