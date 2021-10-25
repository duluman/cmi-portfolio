"""
Vreau un sistem pentru managementul utilizatorilor. 

Un utilizator are urmatoarele detalii: 
- nume 
--> cum arata numele? first si last, first last in acelasi camp?
= first name si last name 

- adresa de email

- parola
--> lungime minima?
= 10 caractere
--> caractere obligatorii?
= nu 

- token
- fingerprint 
- image 
- ... 

- tier 
- parent 

- companie
--> doar numele companiei sau si alte detalii?
= doar numele 

- tip 
--> ce tipuri de utilizatori exista?
= super admin, admin, employee
= super admin (per aplicatie), admin (per subscriptie), manager (per admin), employee (per admin)
= admin e unic per subscriptie 

Sistemul de management al utilizatorilor vreau sa imi ofere urmatoarele functionalitati:

- creez un utilizator nou
--> ce detalii sunt obligatorii?
= nume, email, parola, tip, secret

--> creez utilizatori de orice tip?
= nu, doar manager si employee

--> cui ofera functionalitatea de a creea utilizatori noi? 
= admin sau manager
= admin -> manager -> employee
= super admin -> admin 

--> orice tip de utilizator poate create orice alt tip de utilizator?
= nu (vezi intrebarea anterioara)

--> am un numar limitat de noi utilizatori pe care ii pot crea?
= da, depinde de subscriptie  
= tier 1: 2 managers si 10 employee per manager 
= tier 2: 5 managers si 100 employee per manager 

--> simultaneous login + sync?
= nu 

- editez un utilizator existent 
--> ce anume editez?
= tot

--> cine are voie sa editeze?
= user curent + admin + manager 
= super admin -> admin

--> poate oricine sa editeze? 
= da
= employee -> self 
= manager -> self + employee care ii apartin lui 
= admin -> self + manager care ii apartin lui 
= super admin -> admin 

--> vreau sa am o verificare inainte de a permite editarea?
= da

--> vreau sa trimit notificari despre ultima editare?
= da 

--> putem sa schimbam tipul de user? (tip3 --> tip1) 
= da 
= doar admin poate schimba tipul
= pot trece din manager in employee sau din employee in manager 
= super admin poate face alti admin

- schimb parola unui utilizator
--> poti refolosi o parola?
= nu 

--> ce informatii sunt necesare pt schimbarea parolei?
= confirmarea parolei vechi 

--> vrem sa avem 2 factor auth pt schimbarea parolei?
= nu 

--> poate si alt user sa schimbe parola userului curent (exceptand userul curent)? 
= super admin -> admin 
= admin -> manager sau employee

--> doresc schimbarea parolei periodic?
= nu 

- recuperez parola unui utilizator
--> se doreste folosirea unei informatii personale pentru recuperare?
= da, numele mamei 

--> de cate ori?
= nu exista limita

--> cat de des?
= de 3 ori la 1h

--> cum fac asta? 
= temporary password --> needs changing in 10m
= change password 

- stergerea utilizatorilor (dezactivarea)
--> cine are voie sa ii stearga?
= manager sau admin

--> permanent sau temporar?
= temporar 

--> pot reactiva un user?
= da 

--> stergem / dezactivam utlizatori dupa X zile de inactivitate?
= nu 
"""
from enum import Enum 

class User:
    def __init__(self, firstname, lastname, email, password, secret, user_type, company=None, tier=None, parent=None):
        self.firstname = firstname
        self.lastname = lastname 
        self.email = email 
        self.password = password
        self.user_type = user_type
        self.company = company 
        self.tier = tier 
        self.parent = parent 
        self.secret = secret

    def edit_user(self):
        pass 

    def change_password(self):
        pass 

    def remind_password(self):
        pass 

    def delete(self):
        pass 

    def change_tier(self):
        pass

    @staticmethod
    def validate_password(password):
        if len(password) >= 10:
            return password
        else:
            raise Exception("Invalid password provided")

    @staticmethod
    def validate_user_creation_by_tier(user_type, tier, parent):
        if user_type is None or tier is None or parent is None:
            raise Exception("Invalid user type, tier, or parent provided.")
        # get user tree --> based on parent --> get all managers + employees 
        # get from database! 
        admins_num = 1
        managers_num = 1
        employees_num = 2
        if user_type == UserTypeEnum.ADMIN and admins_num + 1 > 1:
            raise Exception("Too many admins.")
        if user_type == UserTypeEnum.MANAGER and managers_num + 1 > tier.max_number_of_managers:
            raise Exception("Too many managers.")
        if user_type == UserTypeEnum.EMPLOYEE and employees_num + 1 > tier.max_number_of_employees:
            raise Exception("Too many employees.")
        return True

    @classmethod
    def create_user(cls, firstname, lastname, email, password, secret, user_type, company=None, tier=None, parent=None):
        password = cls.validate_password(password)
        if cls.validate_user_creation_by_tier(user_type, tier, parent):
            return cls(firstname, lastname, email, password, secret, user_type, company, tier, parent)


class Tier:
    def __init__(self, max_number_of_managers, max_number_of_employees, name=None):
        self.max_number_of_managers = max_number_of_managers
        self.max_number_of_employees = max_number_of_employees
        self.name = name 


class UserTypeEnum(Enum):
    SUPERADMIN = 1
    ADMIN = 2
    MANAGER = 3
    EMPLOYEE = 4


if __name__ == "__main__":
    tier1 = Tier(2, 10)
    user = User.create_user('andrei', 'luchici', 'a@c.com', 'password1234456', '23423423', UserTypeEnum.ADMIN, tier=tier1)
    manager = user.create_user('bogdan', 'vaduva', 'b@c.com', 'pasasrereqwqwq', '2daslfj', UserTypeEnum.MANAGER, tier=tier1)