from dataValidator import validator

user_schema = {
    "nom": r'^[a-zA-Z]+$',
    "prenom": r'^[a-zA-Z]+$',
    "email": r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}$',
    "birth_date": r'^\d{4}-\d{2}-\d{2}$',
}

user_data = {
    "nom": "youssef",
    "prenom": "gharbi",
    "email": "gharbiyoussef884@gmail.com",
    "dn": "2004-05-18",
}


if validator.validatiton_nom(user_data["nom"]):
    print("Nom valide")
else:
    print("Nom est invalide.")

if validator.validation_prenom(user_data["prenom"]):
    print("Last name is valid!")
else:
    print("Invalid last name.")

if validator.validate_email(user_data["email"]):
    print("Email est valide!")
else:
    print("email est invalide")

if validator.validation_date_de_naissance(user_data["dn"]):
    print("date de naissance est valide")
else:
    print("date de naissance est invalide.")


if validator.validate_schema(user_data, user_schema):
    print("Data est valide!")
else:
    print("Data est invalide.")
