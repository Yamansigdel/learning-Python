
import file
# file=open('d:/Python Programming/My Works/Revise/file.txt','w')
# file.write('This is a practice session \n')
# file.close()
# file=open('d:/Python Programming/My Works/Revise/file.txt','a')
# file.write('Appending the file')
# file.close()

# file=open('d:/Python Programming/My Works/Revise/file.txt','r')
# file.read()
# file.close()

#for filing with binary storage
import shelve

# shelfile=shelve.open('mydata')
# shelfile['cats']=['zombie','hina','sina','oren']
# shelfile.close()
# shelfile=shelve.open('mydata')
# shelfile['cats']
# list(shelfile.keys())

#for copying and moving files
import shutil

#for deleting a file using unlink
import os
# os.getcwd()
# os.unlink('mydata.dir')

#for del files upto recyclebin
import send2trash
# send2trash.send2trash('mydata.dat')

