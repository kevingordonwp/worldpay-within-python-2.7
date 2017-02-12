
import os

# assume this works for now
os.system("sudo python ./thrift/lib/py/setup.py install")
print "Assumes thrift installed okay for now..."
os.system("cat README.txt")