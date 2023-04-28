#create a function that print data from array of object input:

def print_data(data):
    for i, item in enumerate(data):
        print(f"{i+1}. nama: {item['name']}, usia: {item['age']}")


data = [
    {
        "name": "udin",
        "age": 10
    },
    {
        "name": "ujang",
        "age": 11
    },
    {
        "name": "asep",
        "age": 12
    }
]

print_data(data)