import web
import datetime
import uuid



urls = (
    '/picturepath/(.*)', 'picturepath',
    '/pictureupload', 'pictureupload'
)
 
app = web.application(urls, globals())
 
class picturepath:
    def GET(self,picpath):
        i = web.input(picpath=None,pictype=None)


        #uppack
        tt1=str(i.picpath)
        
        strid=''
        pic1=''
        pic2=''
        pic3=''
        picjson=''
        
        f1 = tt1.find(',')
        strid = tt1[:f1]
        tt1=tt1[f1+1:]
        
        f1 = tt1.find(',')
        pic1 = tt1[:f1]
        tt1=tt1[f1+1:]

        f1 = tt1.find(',')
        pic2 = tt1[:f1]
        tt1=tt1[f1+1:]

        f1 = tt1.find(',')
        pic3 = tt1[:f1]
        
        picjson=tt1[f1+1:]

        print(strid)
        print(pic1)
        print(pic2)
        print(pic3)
        print(picjson)

        
        

        #code
        

        
        
        s="["+ str(i.picpath) + "],[" + str(i.pictype) + "]"
        
        return s

 

class pictureupload:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return """<html><head><title>Upload</title></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="txt" name="mykey" />
<br/>
<input type="submit" />
</form>
</body></html>"""
    def POST(self):
        time1=datetime.datetime.now()

        areyouok=False
        
        x = web.input(myfile = {})
 
##        if 'mykey' in x:
##            bkey=x.mykey
##            if bkey != 'xxxxx':
##                return areyouok


        strid=''
        pic1=''
        pic2=''
        pic3=''
        picjson=''
            
        if 'mykey' in x:
            bkey=x.mykey
            print(bkey)

            tt1=bkey
            
            f1 = tt1.find(',')
            strid = tt1[:f1]
            tt1=tt1[f1+1:]
            
            f1 = tt1.find(',')
            pic1 = tt1[:f1]
            tt1=tt1[f1+1:]

            f1 = tt1.find(',')
            pic2 = tt1[:f1]
            tt1=tt1[f1+1:]

            f1 = tt1.find(',')
            pic3 = tt1[:f1]
            
            picjson=tt1[f1+1:]

            print(strid)
            print(pic1)
            print(pic2)
            print(pic3)
            print(picjson)
            

        filename = ''
        filedir = 'images'  
        if 'myfile' in x:
            try:
                filepath = x.myfile.filename.replace('\\','/')  
                filename = filepath.split('/')[-1]  
                filename = str(uuid.uuid1()) + '_' + filename  #guid 
                fout = open(filedir +'/'+ filename,'wb')  
                fout.write(x.myfile.file.read()) # writes  
    #            fout.write(x.myfile.value) # writes the uploaded file to the newly created file.
                fout.close()  
                areyouok=True
            except:
                pass

        #code
        
             
        time2=datetime.datetime.now()
        print(time2-time1)

        return areyouok
##        raise web.seeother('/upload')
        
if __name__ == "__main__":
    app.run()
