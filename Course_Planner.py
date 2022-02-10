#Course Planner

dict_of_courses = {'Gen_Biology 1121' : 3, 'Thermodynamics 2534' : 3, 'TRW 2323' : 2, 'Computer_Programming 7683' : 4, 'Maths1 1111' : 3, 'Maths2 1112' : 3, 
                    'Maths3 1113' : 3, 'Workshop_practice 9889' : 2, 'Engineering_graphics 5482' : 2, 'Gen_chemistry 2231' : 3, 'Electrical_sciences 0584' : 3, 
                    'MeOW 6969' : 3}

user_courses = {}

class User:

    def __init__(self):
        self.courses = user_courses

    def add_course(self, course):
        self.course = course
        user_courses[self.course]=""

    def remove_course(self, course):
        self.course = course
        del user_courses[self.course]


class Courses:

    def __init__(self, notes):
        self.notes = notes
    
    
    def create_notes(self, notes):
        self.notes = notes + " "
        user_courses[c2] = self.notes

    def read_notes(self):
        print(self.notes)


    def update_notes(self, new_notes):
        self.new_notes = new_notes
        self.notes = self.notes + " " + self.new_notes 
        user_courses[c2] = self.notes

    def delete_notes(self):
        self.notes = ""
        user_courses[c2]=self.notes



def allow_edit():
    print("\n")
    for i in user_courses:
        print(i)
    global c, c2, nt
    c2 = c = input("Enter course:")
    print("\n")
    for i in user_courses:
        if(c==i):
            nt = user_courses[c]
            return True
        else:
            p=0

    if(p==0):
        print("\nInvalid course entered!!")






while(True):
    student = User()
    response = int(input("\n\n\n1.Add Course    \n2.Remove Course    \n3.Create notes    \n4.Read notes \n5.Update notes    \n6.Delete notes \n7.Your enrolled courses \n8.Your total Units \n9.Exit \nYour response : "))
    if(response==1):
        while(True):
            print(("\nList of Courses and respective units\n"))
            for key in dict_of_courses:
                print("{}  ---->  {}".format(key, dict_of_courses[key]))
            ans = input("Enter code of the course to be added:")
            for key in dict_of_courses:
                fl = True
                name_code = key.split(" ")
                if(ans==name_code[1]):
                    fl = False
                    if(name_code[0] not in user_courses):
                        student.add_course(name_code[0])
                        print("\n{} has been added to your courses\n\n".format(name_code[0]))
                    else:
                        print("\nAlready in your courses\n")
                    break
            if(fl):
                print("\nEnter valid course code!!\n") 


            k=input("Add more courses [y/n]:")
            if(k=='y'):
                continue
            else:
                break

    elif(response==2):
        k = allow_edit()
        if(k==True):
            student.remove_course(c)
            print(c+" has been removed from your courses")
    
    elif(response==3):
        k = allow_edit()
        if(k==True):
            note = input("Enter note to be added : ")
            c=Courses("")
            c.create_notes(note)
            print("\nNote added successfully\n")
    
    elif(response==4):
        k = allow_edit()
        if(k==True):
            c=Courses(nt)
            if(nt==""):
                print("No notes written!")
            else:
                c.read_notes()
    
    elif(response==5):
        k = allow_edit()
        if(k==True):
            new_note=input("Enter notes:")
            c=Courses(nt)
            c.update_notes(new_note)
    
    elif(response==6):
        k = allow_edit()
        if(k==True):
            c=Courses(nt)
            c.delete_notes()
            print("\n{}'s notes deleted successfully".format(c2))
    
    elif(response==7):
        if(user_courses=={}):
            print("\nNo courses enrolled yet")
        else:
            print("\n")
            for i in user_courses:
                print(i, "--> "+user_courses[i])
    
    elif(response==8):
        units=0
        for i in user_courses:
            for key in dict_of_courses:
                if(i==key.split()[0]):
                    units+=dict_of_courses[key]
        print("\nTotal Units: ", units)

    else:
        print("\nSigning Off!\n")
        break