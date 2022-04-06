import pygsheets
import numpy as np
#authorization
gc = pygsheets.authorize(service_file='C:/Users/username/Documents/creds.json')


# Open spreadsheet and then worksheet
sh =gc.open('FinnScrap')
wks = sh.sheet1

# Update a cell with value (just to let him know values is updated ;) )
wks.update_value('A2', "Hey yank this numpy array")
my_nparray = np.random.randint(10, size=(3, 4))