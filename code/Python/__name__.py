url = 'https://sanboxdnac.cisco.com'
username = 'devnetuser'
password = 'Cisco123!'
if __name__ == '__main__':

# __main__ is the name of the current file or script to run locally and not imported, before start to run a python script python
#set a couple a variables including __name__ and if that script is local that means that __name__ is equal to __main__, otherwise if you 
#were importing a module out from local script the variable __name__ from that module would be the name of that module and not __main_
#so this help to know from where you want to start running your script or when you import a module to have control from where python
#would start running your script

  print(url)
  print(username)
  print(password)
  print(__name__)
  


    
