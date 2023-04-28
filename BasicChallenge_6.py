#reate a function that return object that contain gruop of people based on sex, age, marital-status, job-status input

def group_people(people):
    groups = {"sex": {"male": [], "female": []},
              "age": {"under20": [], "20-40": [], "over40": []},
              "marriage": {"single": [], "double": []},
              "status": {"student": [], "employee": []}
             }
    
    for person in people:
        # Group berdasarkan jenis kelamin
        if person["sex"] == "male":
            groups["sex"]["male"].append(person["name"])
        elif person["sex"] == "female":
            groups["sex"]["female"].append(person["name"])
        
        # Group berdasarkan umur
        if person["age"] < 20:
            groups["age"]["under20"].append(person["name"])
        elif person["age"] < 40:
            groups["age"]["20-40"].append(person["name"])
        else:
            groups["age"]["over40"].append(person["name"])
        
        # Group berdasarkan status pernikahan
        if person["marital_status"] == "single":
            groups["marriage"]["single"].append(person["name"])
        elif person["marital_status"] == "married":
            groups["marriage"]["double"].append(person["name"])
        
        # Group berdasarkan status pekerjaan
        if person["job_status"] == "student":
            groups["status"]["student"].append(person["name"])
        elif person["job_status"] == "employed":
            groups["status"]["employee"].append(person["name"])
    
    return groups

people = [
    {"name": "udin", "sex": "male", "age": 18, "marital_status": "single", "job_status": "student"},
    {"name": "ujang", "sex": "male", "age": 35, "marital_status": "married", "job_status": "employed"},
    {"name": "asep", "sex": "male", "age": 45, "marital_status": "single", "job_status": "employed"},
    {"name": "icih", "sex": "female", "age": 19, "marital_status": "single", "job_status": "student"},
    {"name": "eneng", "sex": "female", "age": 55, "marital_status": "married", "job_status": "employed"}
]

groups = group_people(people)
print(groups)
