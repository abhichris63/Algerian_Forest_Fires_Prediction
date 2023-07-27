import pymongo
import pandas as pd
from Logger import log

# This class is for connecting to Mongodb and fetching the records from Mongodb
class MongodbConnection: 
    # __init__ it is reserved method for python class.
    # __init__ is a constructor of class.
    # __init__ is called when object is created from class & allows class to initialize attributes of class.
    def __init__(self,dbname,recordname,username,password):
        try:
            # self is an instance of class through self we can access methods and attributes of class.
            self.dbname = str(dbname)
            self.recordname = str(recordname)
            self.username = str(username)
            self.password = str(password)
            # Mongodb atlas connection url  
            self.url = f"mongodb+srv://{self.username}:{self.password}@cluster0.b16luzv.mongodb.net/?retryWrites=true&w=majority"
        except Exception as e:
            raise e
    
    # Connection function to connect Mongodb
    def dbconnect(self):
        try:
            client = pymongo.MongoClient(self.url)
            return client
        except Exception as e:
            log.error('Error while establishing Mongodb connection !!!')
            raise e    

    # Function to Fetch records in the form of list
    def fetchrecords(self):
        try:
            clientconnect = self.dbconnect()
            db_Name = clientconnect[self.dbname]
            col_Name = db_Name[self.recordname]
            cursor = col_Name.find()
            return list(cursor)
        except Exception as e:
            log.error('Error while fetching Dataset from mongodb !!!')
            raise e
        
    # Function to convert from list to pandas DataFrame & returns the results
    def bulk_results(self):
        try:
            cr = self.fetchrecords()
            df  =   pd.DataFrame(columns=['Temperature','Ws','FFMC','DMC','ISI'])
            results = []
            for i in cr:
                bulk_dict = {'Temperature':i['Temperature'],
                            'Ws':i['Ws'],
                            'FFMC':i['FFMC'],
                            'DMC':i['DMC'],
                            'ISI':i['ISI']}
                results.append(bulk_dict)
            #returns first_row from the DataFrame
            return results[0:1]
        except Exception as e:
            log.error('Error while returning first row from DataFrame !!!')
            raise e