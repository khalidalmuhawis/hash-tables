students = [
    {
        "name": "Jean-Luc Garza",
        "score": 24
    },
    {
        "name": "Teddy Munoz",
        "score": 79
    },
    {
        "name": "Georgia Ali",
        "score": 17
    },
    {
        "name": "Vicky Calhoun",
        "score": 8
    },
    {
        "name": "Awais Weaver",
        "score": 65
    },
    {
        "name": "Athena Kline",
        "score": 52
    },
    {
        "name": "Zacharia Whitaker",
        "score": 38
    },
        {
        "name": "Clarice Davenport",
        "score": 99
    },
    {
        "name": "Viktoria Flynn",
        "score": 84
    },
    {
        "name": "Ianis Crossley",
        "score": 20
    },
    {
        "name": "Johnnie Owens",
        "score": 74
    },
    {
        "name": "Emily-Rose Erickson",
        "score": 33
    },
    {
        "name": "Adeel Nieves",
        "score": 100
    },
    {
        "name": "Dustin Villegas",
        "score": 98
    },
    {
        "name": "Maxine Hughes",
        "score": 65
    },
    {
        "name": "Bilaal Harding",
        "score": 79
    },
    {
        "name": "Maddie Ventura",
        "score": 71
    },
    {
        "name": "Leroy Rees",
        "score": 44
    },
    {
        "name": "Wanda Frank",
        "score": 73
    },
    {
        "name": "Margaux Herbert",
        "score": 80
    },
    {
        "name": "Ali Rios",
        "score": 70
    },
    {
        "name": "Nigel Santiago",
        "score": 25
    },
    {
        "name": "Markus Greene",
        "score": 78
    },
    {
        "name": "Harlan Parrish",
        "score": 97
    },
    {
        "name": "Baran Davidson",
        "score": 43
    },
    {
        "name": "Seth Rodriguezh",
        "score": 67
    },
    {
        "name": "Diego Mayer",
        "score": 100
    },
]

class HashTable:
    def __init__(self, class_size):
        self.class_size = class_size
        self.dict = {'A': [], 'B': [], 'C': [], 'D': []}

    def hash_class(self, score):
        if score >= 90:
            return "A"
        elif score >=80:
            return "B"
        elif score >=70:
            return "C"
        elif score >=60:
            return "D"
        else:
            return None


    def insert(self, name, score):
        classroom = self.hash_class(score)
        if classroom:
            if len(self.dict[classroom]) < self.class_size:
                self.dict[classroom].append({"name":name, "score": score})
            else:
                print("classroom is full")

size = int(input("whats the size of the classes? "))
school = HashTable(size)
for student in students:
    school.insert(student['name'], student['score'])

    for classroom, students in school.dict.items():
        print(f"CLASSROOM {classroom}")
        for student in students:
            print(f"{student['name']} --> {student['score']}")
        print("-"*40)
