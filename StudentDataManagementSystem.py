class StudentNode:
    def __init__(self, roll_no, data):
        self.roll_no = roll_no
        self.stdata = data
        self.prev = None
        self.next = None

class StudentData:
    def __init__(self, name, course):
        self.name = name
        self.course = course

class CourseNode:
    def __init__(self, course_num, grade):
        self.course_num = course_num
        self.grade = grade
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None
        self.std_list = []
    
    def __del__(self):
        pass
    
    def isEmpty(self):
        return self.head is None

    # add new student
    def add_student(self, roll_no, name, course):
        std_data = StudentData(name, course)
        new_student = StudentNode(roll_no, std_data)
        if self.head is None:
            self.head = new_student
            return
        # if the roll no of new student is greater than head student roll no
        if new_student.roll_no < self.head.roll_no:
            new_student.next = self.head
            self.head.prev = new_student
            self.head = new_student
            return
        # traversing through the list to find correct position to insert new student
        curr = self.head
        while curr:
            if new_student.roll_no < curr.roll_no:
                previous = curr.prev
                previous.next = new_student
                new_student.prev = previous
                new_student.next = curr
                curr.prev = new_student
                return
            else:
                if curr.next is None:
                    curr.next = new_student
                    new_student.prev = curr
                    return
            curr = curr.next
       
    # remove an existing record of a student
    def remove(self, roll_no):
        curr = self.head
        # if the head student is to removed
        if curr.roll_no == roll_no:
            temp = curr.next
            # if the list has only one student
            if temp is None:
                self.head  = None
                return
            else:
                self.head = temp
                temp.prev = None
                return
        
        # traversing through the list to find the required student
        while curr:
            if curr.roll_no == roll_no:
                previous = curr.prev
                next_std = curr.next
                # if the student to be removed is the last student
                if next_std is None:
                    previous.next = None
                    return
                # if the student to be removed is in the middle
                previous.next = next_std
                next_std.prev = previous             
                return
            else:
                curr = curr.next

    def update_student(self, roll_no, course, grade):
        # if the list is empty
        if self.head is None:
            print('List is empty')
            return
        curr = self.head
        # traversing through the list to find the required student
        while curr:
            if curr.roll_no ==  roll_no:
                st = curr.stdata
                st.course = CourseNode(course, grade)
                return
            else:
                curr = curr.next
                
    # display the list of students
    def display(self):
        if self.isEmpty():
            print('List is Empty')
            return
        curr = self.head
        while curr:
            print('Roll No: ', curr.roll_no)
            print('Name: ', curr.stdata.name)
            CourseNode = curr.stdata.course
            while CourseNode:
                print('Course Number: ', CourseNode.course_num,'\nGrade: ', CourseNode.grade)
                CourseNode = CourseNode.next
                print()
            curr = curr.next

    # display students in ascending order
    # -- as we have added student is ascending order, a normal display function 
    # will give the student in ascending order 
    def display_ascending(self, start_roll, end_roll):
        if self.isEmpty():
            print('List is Empty')
            return
        curr = self.head
        # Move to the student with roll_no equals to start_roll
        while curr and curr.roll_no != start_roll:
            curr = curr.next
        # If curr is None, start_roll is not found
        if curr is None:
            print("Student with start_roll not found")
            return
        # Traverse the list from start_roll to end_roll and print student information
        while  curr and curr.roll_no <= end_roll:
            print('Roll No: ', curr.roll_no)
            print('Name: ', curr.stdata.name)
            CourseNode = curr.stdata.course
            while CourseNode:
                print('Course Number: ', CourseNode.course_num,   'Grade: ', CourseNode.grade)
                CourseNode = CourseNode.next
                print()
            curr = curr.next
            
    def display_descending(self, end_roll, start_roll):
        if self.isEmpty():
            print('List is Empty')
            return
        curr = self.head
        # Move to the student with roll_no equals to end_roll
        while curr and curr.roll_no != end_roll:
            curr = curr.next

        # If curr is None, end_roll is not found
        if curr is None:
            print("Student with end_roll not found")
            return

        # Traverse the list from end_roll to start_roll and print student information
        while curr and curr.roll_no >= start_roll:
            print('Roll No: ', curr.roll_no)
            print('Name: ', curr.stdata.name)
            # Print course information for the student
            course_node = curr.stdata.course
            while course_node:
                print('Course Number: ', course_node.course_num, 'Grade: ', course_node.grade)
                course_node = course_node.next
            print()
            # Move to the previous student
            curr = curr.prev

def main():
    # create a student list
    print()
    std = StudentList()
    while True:
        # display the menu
        print()
        print ('1. Add Student\n2. Remove Student\n3. Update Student\n4. Display All Students')
        print ('5. Display Students in Ascending Order')
        print ('6. Display Students in Descending Order')
        print ('7. Exit')
        # take input from the user
        print()
        choice = int(input('Enter your choice: '))
        print()

        # perform action based on the user choice
        if choice == 1:
            print('Add New Student')
            # add a student
            # take input from the user
            roll_no = int(input('Enter Roll No: '))
            name = input('Enter Name: ')
            course_num = int(input('Enter Course Number: '))
            grade = input('Enter Student Grade: ')
            course_node = CourseNode(course_num, grade)
            std.add_student(roll_no, name, course_node)
            print()
        
        elif choice == 2:
            print('Remove Student')
            # remove a student
            roll_no = int(input('Enter Roll No: '))
            std.remove(roll_no)
            print()
        
        elif choice == 3:
            print('Update Student')
            # update a student
            roll_no = int(input('Enter Roll No: '))
            course_num = int(input('Enter New Course No: '))
            grade = input('Enter New Grade: ')
            std.update_student(roll_no, course_num, grade)
            print()
        
        elif choice == 4:
            print('Displaying All Students')
            # display the students
            std.display()
            print()
            
        elif choice == 5:
            print('Displaying Students in Ascending order')
            # display the students in ascending order
            start_roll = int(input('Enter Starting Roll No: '))
            end_roll = int(input('Enter Ending Roll No: '))
            std.display_ascending(start_roll, end_roll)
            print()
        
        elif choice == 6:
            print('Displaying Students in Descending order')
            # display the students in descending order
            start_roll = int(input('Enter Starting Roll No: '))
            end_roll = int(input('Enter Ending Roll No: '))
            std.display_descending(start_roll, end_roll)
            print()
        
        elif choice == 7:
            # exit the program
            break
        else:
            print('Invalid choice')
if __name__ == '__main__':
    main()