
# Ask the user to enter the first student's ID and store it as an integer
Sonam_Choki=int(input("Enter student id:"))
Karma_Wangdi=int(input("Enter student id:"))


# Extract the last two digits of the first student's ID using modulus operator
student_id_1= Sonam_Choki%100
student_id_2= Karma_Wangdi%100


# Add the last two digits of both IDs, then take modulus 10 to get a single-digit unique value
last_two_id = (student_id_1 + student_id_2) % 10

# Display the unique value
print(f"Unique Value: {last_two_id}")

# Smart Classroom: Collect student names until "exit" is entered
# Create an empty dictionary to store student names
students = {}

#Start a loop to repeatedly ask for names
while True:
    #let the student input their name
    name= input("Enter the name of Student(or type 'exit' to stop):")

    if name.upper() == "EXIT":
       break
     # Add the name to the dictionary with a number key (1, 2, 3...)
    students[len(students) + 1] = name

# After exiting the loop, display all the names entered
print("\nList of Students:")
for key, value in students.items():
    print(f"{key}. {value}")    





