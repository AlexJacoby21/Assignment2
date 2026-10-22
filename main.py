"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45

MINUTES_PER_CLASS = 50

# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semestercost = annual_cost/SEMESTERS_PER_YEAR
    return semestercost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    monthcost = annual_cost/MONTHS_PER_YEAR
    return monthcost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    daycost = annual_cost/(SEMESTERS_PER_YEAR*CLASS_DAYS_PER_SEMESTER)
    return daycost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    creditcost = annual_cost/(credits*SEMESTERS_PER_YEAR)
    return creditcost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    classcost = (((annual_cost/(credits*SEMESTERS_PER_YEAR))*CS1430_CREDITS)/CS1430_MEETINGS_PER_SEMESTER)
    return classcost


def cost_of_distraction(annual_cost, minutes_focused):
    portion_distracted = ((MINUTES_PER_CLASS-minutes_focused)/MINUTES_PER_CLASS)
    distraction_cost = annual_cost * portion_distracted
    return distraction_cost


# ---- PROGRAM ----

def main():
    cost = float(input("Enter the total yearly cost: "))# Ask for the total cost for one year here.
    credits = float(input("Enter your number of credits per semester: "))# Then ask for the credits this semester.

    while True:
        # Show your menu here.
        print("1 Per semester")
        print("2 Per month")
        print("3 Per class day")
        print("4 Per credit")
        print("5 Per CS 1430 class")
        print("6 Cost of being distracted")
        print("Q. Quit")
        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            print(f"One semester costs ${cost_per_semester(cost):.2f}")
        elif choice == "2":
            print(f"One month costs ${cost_per_month(cost):.2f}")
        elif choice == "3":
            print(f"One class day costs ${cost_per_day(cost):.2f}")
        elif choice == "4":
            print(f"One credit costs ${cost_per_credit(cost,credits):.2f}")
        elif choice == "5":
            print(f"Every CS 1430 class costs ${cost_per_class(cost,credits):.2f}")
        elif choice == "6":
            minutes_focused = float(input("How many minutes do you pay attention in a 50 minute class? "))
            print(f"You pay ${cost_of_distraction(cost,minutes_focused):.2f} per year to gain no knowledge")
        else:
            print("Please select a valid option")    
        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
