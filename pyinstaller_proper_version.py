import subprocess
import shutil
import os

cmd = input("file name: ") # asks user for filename
extra = input("extra commands? eg -w -F if using two or more put a space between: ") # asks for extra options
suros = "pyinstaller "+ extra + " " + cmd + ".py" # sets run command
current_workin_path = os.getcwd() # gets current working path
dirt = current_workin_path + "/"+ cmd # set current working path for folder creation
os.mkdir(dirt) # creates folder for working path and for a copy
shutil.copy(cmd + ".py", current_workin_path + "/" + cmd + "/" + cmd + ".py") # creats copy of python file in the newly set path
os.chdir(current_workin_path + "/" + cmd + "/") # changes current working path to newly created one
subprocess.run(suros) # runs the command set eariler
os.remove(cmd + ".py") # delete the copy of python file
