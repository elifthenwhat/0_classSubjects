def build_person(first_name, last_name, **feature):
    person = {"First" : first_name, "Last" : last_name}
    if feature:
        person["Additional Info"] = feature
    return person 

