import json

data_file = "PN.json"

class PhoneNumber:
    def enter(self, phone, fname):
        self.phone = phone
        self.fname = fname
        data =  {
                fname:{
                    phone
                },
            }
        with open(".\\" + data_file, "a", encoding="utf-8") as file:
            json.dump(data, file)
        

amir1 = PhoneNumber()
# amir1.phone = 9917266234
# amir1.fname = "Amirhossein Arabpour"
amir1.enter(9917266234, "Amirhossein Arabpour")