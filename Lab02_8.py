
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

print("-----------------------------------------------------------------------------")
print("QUIZ")
# For each student,they have three questions based on the unique value and calculate their score
for name in students.values():

    print("Student:", name)

    # check if empty name
    if name == "": # Blank name entered
        print("Empty name. Skipping...") 
    else:
        score = 0 # Initialize score for each student

        # Q1 
        a = int(input("Q1: " + str(last_two_id) + " + 2 = "))
        if a == last_two_id + 2:
            score = score + 1

        # Q2
        b = int(input("Q2: " + str(last_two_id) + " * 3 = "))
        if b == last_two_id * 3:
            score = score + 1

        # Q3
        c = int(input("Q3: " + str(last_two_id) + " + 5 = "))
        if c == last_two_id + 5:
            score = score + 1
        print("-----------------------------------------------------------------------------")
        print()
        print("You have Scored:", score) # performance, certificate, warning, stars

        # performance
        if score == 3:
            print("Your Performance: Excellent") 
        elif score == 2:
            print("Your Performance: Good")
        elif score == 1:
            print("Your Performance: Average")
        else:
            print("YourPerformance: Poor")

        # certificate
        if score >= 2:
            print("Eligible for Certificate: Yes")
            print()
        else:
            print("Eligible for Certificate: No")
            print()

        # warning
        if score == 0: # Warning for score 0
            print("Warning: Score is 0")
            print()

        # stars
        print("Stars:")
        if score == 0:
            print(" ") # No stars for score 0
        else: # Print stars in a pattern based on the score
            i = 1
            while i <= score: 
                print("*" * i)
                i = i + 1 # Increment i to print the next line of stars



