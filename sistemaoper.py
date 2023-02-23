import os

print(os.environ)
#print(os.getlogin()) no funciona pq trabajamos desde la nube. hacelo en visual studio
path=os.getcwd()
print(os.listdir(path))
os.chdir('../') #como si hicieramos cd..
path=os.getcwd()
print(os.listdir(path))

parent_dir = "Maite"
misistemaficher=os.getcwd()
path = os.path.join(misistemaficher,parent_dir)
os.mkdir(path)
""" directory = input("")  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '%s' created" %directory) """
  