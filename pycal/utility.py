# pycal/utility.py
import sys
import json
import csv


class FileUtility:
    utility_name:str = 'B-cal file management utility'

    def __init__(self, *args, **kwargs):
        if args:
            if len(args)>1:
                self.name = args[0]
                self.file = args[1]
                print(self.__dict__)
            elif len(args) == 1:
                self.name = args[0] 
                print(self.name, 'Initiliazsed...')    

    def _json_to_csv(self, file:str, data:list):
        keys = [*data[0]]
        items =[[obj[key] for key in keys] for obj in data]
        print(keys)
        print(items)
        with open(file, 'w') as outfile:
            writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(keys)
            for item in data:
                writer.writerow(data)
        return f"{file} Saved."  


    def save_csv(self, file:str=None, data:dict=None):
        ''' This Utility creates and saves a .csv file in the application base directory.
            parameters are:
                file = a String of the name of the file with .csv ending,
                path = a String id of where to save the file defaults to the application base directory,
                data = a dictionary object of the data be saved in the file,
            If a filename is not provided the data payload is scanned for an id key which is used 
            as the file identifier if an id key is not present the first item key is used.
            USAGE

                util = FileUtility() or 
                util = FileUtility('CSV file Handler') # for utility logs
                util.save_csv(data=payload) # without file and path parameter
                util.save_csv(file='todo.json', data=payload) # without path parameter
                util.save_csv(file='todo.json', path='Documents/projects', data=payload) 
        '''

        if file and data:
            try:
                if len(data) > 0:
                    self._json_to_csv(file=file, data=data)
            except Exception as e:
                return e
        
        try:
            # if user did'nt supply a filename and data does not have an id key use the first item key of data
            if len(data) > 0:
                file = f"{data[0]['id']}.csv"
                self._json_to_csv(file=file, data=data)               
        except Exception as e:
            return e
        return
    

    def save_json(self, file:str=None, path:str=None, data:dict=None):
        ''' This Utility creates and saves a .json file in the application base directory.
            parameters are:
                file = a String of the name of the file with .json ending,
                path = a String id of where to save the file defaults to the application base directory,
                data = a dictionary object of the data be saved in the file,
            If a filename is not provided the data payload is scanned for an id key which is used 
            as the file identifier if an id key is not present the first item key is used.
            USAGE

                util = FileUtility() or 
                util = FileUtility('Json file Handler') # for utility logs
                util.save_json(data=payload) # without file and path parameter
                util.save_json(file='todo.json', data=payload) # without path parameter
                util.save_json(file='todo.json', path='Documents/projects', data=payload) 
        '''

        if file and data:
            try:
                if len(data) > 0:
                    with open(file, 'w') as outfile:
                        json.dump(data, outfile)
                    return f"{file} Saved."                
            except Exception as e:
                return e
        try:
            # if user did'nt supply a filename use the id key of the data
            if len(data) > 0 and 'id' in data:
                file = f"{data['id']}.json"
                with open(file, 'w') as outfile:
                    json.dump(data, outfile)
                return f"{file} Saved."                
        except Exception as e:
            return e
        try:
            # if user did'nt supply a filename and data does not have an id key use the first item key of data
            if len(data) > 0:
                keys = [*data]
                file = f"{keys[0]}.json"
                with open(file, 'w') as outfile:
                    json.dump(data, outfile)
                return f"{file} Saved."                
        except Exception as e:
            return e

        
        return
        


#----------------------------- Data Security Service ----------------------------------

"""
class EncryptMessage():
    ciphers:list = []
    #key_dir:str = '.key_dir'
    key_file_name:str = 'test_key.key'

    def generate_hash_key(self, key_name:str=None):
        hash_key = fn.generate_key()
        #print(hash_key)  
        
        #mkdir(key_dir)
        file = open(self.key_file_name, 'wb')
        file.write(hash_key)
        file.close()

    def generate_password_hash_key(self, plain_text_password:str):

        import base64
        import os
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

        password_provided = plain_text_password # This is input in the form of a string
        password = password_provided.encode() # Convert to type bytes
        salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
        return key 

    def encrypt_message(self, message):
        file = open(self.key_file_name, 'rb')
        key = file.read()
        f = fn(key)
        encrypted = f.encrypt(message.encode())
        print(encrypted)
        return encrypted

    def decrypt_message(self, encrypted_message):
        file = open(self.key_file_name, 'rb')
        key = file.read()
        f = fn(key)
        decrypted = f.decrypt(encrypted_message)
        
        file.close()
        return decrypted 


class EncryptFile:

    def encrypt_file():

        from cryptography.fernet import Fernet
        key = b'' # Use one of the methods to get a key (it must be the same when decrypting)
        input_file = 'test.txt'
        output_file = 'test.encrypted'

        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted)

        # You can delete input_file if you want

    def decrypt_file():
        from cryptography.fernet import Fernet
        key = b'' # Use one of the methods to get a key (it must be the same as used in encrypting)
        input_file = 'test.encrypted'
        output_file = 'test.txt'

        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted)

        # You can delete input_file if you want
"""
#----------------------------- ID Generation Service ----------------------------------
from strgen import StringGenerator

class GenerateId:
    tags:dict = dict(
            doc='[h-z5-9]{8:16}',
            app='[a-z0-9]{16:32}',
            key='[a-z0-9]{32:32}',
            job='[a-j0-7]{8:8}',
            user='[0-9]{4:6}',
            item='[a-n1-9]{8:8}',
            code='[a-x2-8]{24:32}'
        )
        
    def genid(self, doc_tag:str=None):
        """Doc Tags: String( doc, app, key, job, user, item, code,task,name)
            UseCase:    >>> import genny
                        >>> from genny import genid
                        >>> from genny import genid as gi                        
                        >>> id = genny.genid('user')
                        >>> id = genid('user')
                        >>> id = gi('user')
                Yeilds ... U474390
                        ... U77301642
                        ... U1593055"""
        
        if doc_tag == 'user':
           return f"U{StringGenerator(str(self.tags[doc_tag])).render(unique=True)}"
        return StringGenerator(str(self.tags[doc_tag])).render(unique=True)
            

    def nameid(self, fn:str='Jane',ln:str='Dear',sec:int=5):
        """Name Identification by initials fn='Jane', ln='Dear' and given number sequence sec=5.            
            UseCase:    >>> import genny
                        >>> from genny import nameid
                        >>> from genny import nameid as nid
                        
                        >>> id = genny.nameid('Peter','Built',6)
                        >>> id = nameid('Peter','Built',5)
                        >>> id = nid('Peter','Built',4)
                        >>> id = nid() # default false id 
                        
                Yeilds ... PB474390
                        ... PB77301
                        ... PB1593
                        ... JD1951"""
        code = '[0-9]{4:%s}'% int(sec)
        return f"{fn[0].capitalize()}{ln[0].capitalize()}{StringGenerator(str(code)).render(unique=True)}"               

    def short_nameid(self, fn:str='Jane', ln:str='Dear', sec:int=2):
        """ 
            Name Identification by initials fn='Jane', ln='Dear' and given number sequence sec=5.
            
            UseCase: 
                        >>> import genny
                        >>> from genny import short_nameid
                        >>> from genny import short_nameid as id
                        
                        >>> id = genny.short_nameid('Peter','Built',2)
                        >>> id = short_nameid('Peter','Built')
                        >>> id = id(p','b',3)
                        >>> id = id() # default false id 
                        
                Yeilds ... PB47
                        ... PB54
                        ... PB69
                        ... JD19
        
        """
        code = '[0-9]{2:%s}'% int(sec)
        return f"{fn[0].capitalize()}{ln[0].capitalize()}{StringGenerator(str(code)).render(unique=True)}"
        

    def eventid(self, event,event_code,sec=8):
        """EventId 
            Event Identification by initials fn='Jane', ln='Dear' and given number sequence sec=5.
            
            UseCase: 
                        >>> import genny
                        >>> from genny import eventid
                        >>> from genny import eventid as id
                        
                        >>> id = genny.eventid('Product','LAUNCH',6)
                        >>> id = eventid('Product','LAUNCH',5)
                        >>> id = id('Product', 'LAUNCH',4)                       
                Yeilds ... PROLAUNCH-884730
                        ... PROLAUNCH-18973
                        ... PROLAUNCH-4631                       
        
        """
        code = '[0-9]{4:%s}'% int(sec)
        return f"{event[:3].upper()}{event_code}-{StringGenerator(str(code)).render(unique=True)}"
        

    
 
genny = GenerateId()
#encrypt_message_file = EncryptMessage()
