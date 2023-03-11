import requests,io
from PIL import Image

class User:

    def __init__(self):
        response = requests.get("https://randomuser.me/api/")
        self.data = response.json()["results"][0]
        self.setDataUser()

    def setDataUser(self):
        """
        set the global data

        return nothing
        """
        self.gender = self.data['gender']
        self.name = self.data['name']
        self.location = self.data['location']
        self.email = self.data['email']
        self.login = self.data['login']
        self.dob = self.data['dob']
        self.registered = self.data['registered']
        self.phone = self.data['phone']
        self.cell = self.data['cell']
        self.id = self.data['id']
        self.picture = self.data['picture']['large']
        self.nat = self.data['nat']

    def getUserFirstName(self) -> str:
        return self.name['first']

    def getUserLastName(self) -> str:
        return self.name['last']

    def getUserStreetNumber(self):
        return self.location['street']['number']

    def getUserStreetName(self):
        return self.location['street']['name']

    def getUserCity(self):
        return self.location['city']

    def getUserState(self):
        return self.location['state']

    def getUserCountry(self):
        return self.location['country']

    def getUserAge(self):
        return self.dob['age']

    def getUserBirthDate(self):
        res = self.dob['date']
        return res[:10]

    def getUserPhone(self):
        return self.phone

    def getUserEmail(self):
        return self.email

    def getUserGender(self):
        return self.gender

    def getUserUsername(self):
        return self.login['username']

    def getUserUUID(self):
        return self.login['uuid']

    def getUserPassword(self):
        return self.login['password']

    def getUserPicture(self):
        r = requests.get(self.picture)
        return Image.open(io.StringIO(r.content))

    def getUserNat(self):
        return self.nat



u = User()
for el in u.data:
    print(el, end=" : ")
    print(u.data[el])