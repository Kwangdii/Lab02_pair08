
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
# Quiz for the students
# Loop through each student
for key, name in students.items():  
    # Print quiz heading
    print(f"\n--- Quiz for {name} ---")  
    score = 0   # Start score at 0
   
    # Question 1: 2 + 2
    ans1 = int(input("Q1: 2 + 2 = "))
    if ans1 == 4:
        print("Correct Answer!")   # Feedback
        score += 1
    else:
        print("Wrong Answer! The correct answer is 4.")

    # Question 2: 3 * 3
    ans2 = int(input("Q2: 3 * 3 = "))
    if ans2 == 9:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer! The correct answer is 9.")

    # Question 3: 5 - 5
    ans3 = int(input("Q3: 5 - 5 = "))
    if ans3 == 0:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer! The correct answer is 0.")

# show score
    print()
    print("Score:", score) #

    # performance
    if score == 3: #if the score is 3, then the performance is excellent
        print("Performance: Excellent")
    elif score == 2: #if the score is 2, then the performance is good
        print("Performance: Good")
    elif score == 1: #if the score is 1, then the performance is average
        print("Performance: Average")
    else: #if the score is 0, then the performance is poor
        print("Performance: Poor")

    # certificate
    if score >= 2: # if the score is 2 or more, then the student gets a certificate
        print("Certificate: Yes")
    else:
        print("Certificate: No")

    # warning
    if score == 0: # if the score is 0, it willprint a warning message
        print("Warning: Score is 0")

    # stars
    print("Stars:") # if the score is 0, it will not print any stars, or it will print stars according to the score
    if score == 0:
        print("")
    else:
        i = 1
        while i <= score:
            print("*" * i)
            i = i + 1



