#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class LoginManager():
    def __init__(self, username, password, isVerified):
        self.username = username
        self.password = password
        self.isVerified = isVerified
    
    def setVerifiedValue(self, data):
        print("Value to Update is: ", data)
        if type(data) == bool:
            self.isVerified = data
        else:
            print("Plz Enter Value in True/False")
        print("Updated value: ",self.isVerified)
        
    def checkVerified(self):
        if self.isVerified:
            print("User is Verified")
            return True
        else:
            print("User is Not Verified")
            return False
            
    def loginUser(self):
        if self.username == "faizan" and self.password == "123456":
            if self.checkVerified():
                return "User Logged in"
            else:
                print("Not Verified")
        else:
            return "Incorrect details"

