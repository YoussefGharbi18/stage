import re
def validation_nom(name):
    return bool(re.match(r'^[a-zA-Z]+$', str(name)))

def validation_prenom(name):
    return bool(re.match(r'^[a-zA-Z]+$', str(name)))

def validation_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}$', str(email)))

def validation_date_de_naissance(birth_date):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', str(birth_date)))

def validate_schema(data, schema):
    for key, pattern in schema.items():
        if key not in data:
            return False

        value = data[key]
        if not re.match(pattern, str(value)):
            return False

    return True
