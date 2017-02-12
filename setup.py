
import os

os.system("git submodule init")
os.system("git submoduel update")
# assume this works for now
os.system("cd ./thrift/lib/py/; sudo python setup.py install")
print "Assumes thrift installed okay for now..."
os.system("cat README.md")
