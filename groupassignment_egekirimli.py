import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("titanic.csv")

# Columns from the dataset
names_column = titanic["Name"]
class_column = titanic["Pclass"]
survive_column = titanic["Survived"]
sex_column = titanic["Sex"]
age_column = titanic["Age"]

# Variables to store counts
males = 0
females = 0
male_class1 = 0
male_class2 = 0
male_class3 = 0
female_class1 = 0
female_class2 = 0
female_class3 = 0
survived_females = 0
survived_males = 0
dead_females = 0
dead_males = 0

while True:
    print("\nWhat would you like to learn about the titanic dataset? ")
    print("1. Number of passengers")
    print("2. Number of passengers survived and died ")
    print("3. Average age of passengers ")
    print("4. Number of passengers in each class ")
    print("5. Survival Rate by Class ")
    print("6. Exit ")


    choice = input("Enter your choice (1/2/3/4/5/6): ")

# Count the number of males and females
    for each_sex in sex_column:
            if "male" == each_sex:
                males += 1
            if "female" == each_sex:
                females += 1
    if choice == "1":
# Print the total number of passengers
        print(f"\nThere were {females} female and {males} male passengers in the Titanic. ")
        print(f"Total passengers: {females + males}")

# Count the number of survived and dead females and males
        for index, each_row in titanic.iterrows():
            if each_row["Survived"] == 1 and each_row["Sex"] == "female":
             survived_females += 1
            elif each_row["Survived"] == 0 and each_row["Sex"] == "female":
                dead_females += 1

        for index, each_row in titanic.iterrows():
            if each_row["Survived"] == 1 and each_row["Sex"] == "male":
                 survived_males += 1
            elif each_row["Survived"] == 0 and each_row["Sex"] == "male":
                 dead_males += 1

    elif choice == "2":
# Print the number of females and males who survived and died
        print(f"\nNumber of females who survived: {survived_females} ")
        print(f"Number of females who died: {dead_females} ")
        print(f"\nNumber of males who survived: {survived_males} ")
        print(f"Number of males who died: {dead_males} ")
        print(f"\nTotal dead: {dead_females + dead_males}")
        print(f"Total survived: {survived_females + survived_males}")

# Calculate the average age of all passengers, females, and males
        average_age_all = age_column.mean()
        average_age_females = titanic[sex_column == "female" ]["Age"].mean()
        average_age_males = titanic[sex_column == "male" ]["Age"].mean()

    elif choice == "3":
# Print the average age of all passengers, females, and males
        print(f"\nAverage age of all passengers: {average_age_all:.2f}")
        print(f"Average age of female passengers: {average_age_females:.2f}")
        print(f"Average age of male passengers: {average_age_males:.2f}")

# Count the number of males and females in each class
        for index, each_row in titanic.iterrows():
            if each_row["Pclass"] == 1 and each_row["Sex"] == "male":
                male_class1 += 1
            elif each_row["Pclass"] == 2 and each_row["Sex"] == "male":
                male_class2 += 1
            elif each_row["Pclass"] == 3 and each_row["Sex"] == "male":
                male_class3 += 1

        for index, each_row in titanic.iterrows():
            if each_row["Pclass"] == 1 and each_row["Sex"] == "female":
                female_class1 += 1
            elif each_row["Pclass"] == 2 and each_row["Sex"] == "female":
                female_class2 += 1
            elif each_row["Pclass"] == 3 and each_row["Sex"] =="female":
                female_class3 += 1

    elif choice == "4":
# Print the number of females and males in each class
        print(f"\nNumber of females that are Class 1: {female_class1}")
        print(f"Number of males that are Class 1: {male_class1}")
        print(f"Class 1 Total: {female_class1 + male_class1}")
        print(f"\nNumber of females that are Class 2: {female_class2}")
        print(f"Number of males that are Class 2: {male_class2}")
        print(f"Class 2 Total: {female_class2 + male_class2}")
        print(f"\nNumber of females that are Class 3: {female_class3}")
        print(f"Number of males that are Class 3: {male_class3}")
        print(f"Class 3 Total: {female_class3 + male_class3}")

    elif choice == "5":
# Plot the survival rate by class
        plt.figure(figsize=(8, 6))
        class_survival_rate = titanic.groupby("Pclass")["Survived"].mean()
        plt.bar(class_survival_rate.index, class_survival_rate.values, color="darkgreen")
        plt.title("Survival Rate by Class")
        plt.xlabel("Passenger Class")
        plt.ylabel("Survival Rate")
        plt.show()


    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option. ")

    

      
