def FileEdit():
    Edit=open("GIT","w+")
    Edit.seek(0)
    
    Edit.write("Hello.This is not an adventure.Beware")
FileEdit()