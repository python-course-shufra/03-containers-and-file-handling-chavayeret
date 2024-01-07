classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def add_student(name , email='{name}@example.com'.lower(),**grade):
    student={'name':name,'email':email,'grades':[]}
    classroom.append(student)
    return
    


def delete_student(name):
    index=get_index(name)
    classroom.remove(classroom[index])
    return

    


def set_email(name, email):
    index=get_index(name)
    #classroom[index].update({"email": email})
    classroom[index]['email']=email      
    return 


def add_grade(name, profession, grade):
    index=get_index(name)
    classroom[index].update({"grades": (profession,grade)})
    return


def avg_grade(name, profession):
    index=get_index(name)
    grades=classroom[index].get('grades')
    count=0
    sum=0
    for i in grades:
        if i[0]==profession:
            sum=sum+i[1]  
            count=count+1
    return sum/count


def get_professions(name):
    index=get_index(name)
    grades=classroom[index].get('grades')
    prof=set()
    for i in grades:
        prof.add(i[0])
    return prof

    
def get_index(name):
    count=0
    for i in classroom:
        
        if i.get('name')==name:
            index=count
        count=count+1   
    return index
