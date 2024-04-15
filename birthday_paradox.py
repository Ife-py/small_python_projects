import datetime, random

# Set up a tuple of month names in order:
MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)


def get_birthday(number_of_birthdays:int):
    """enter an integer for the amount of birthdays to be simulated"""
    
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)

        # get a random number of day into the year:
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthdat that occurs more than once in the birthday list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # all birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthday_A in enumerate(birthdays):
        for b, birthday_B in enumerate(birthdays[a + 1 :]):
            if birthday_A == birthday_B:
                return birthday_A  # to return the matching birthday.


# intro to be displayed
print("""'Birthday Paradox, by Al Sweigart al@inventwithpython.com
  The Birthday Paradox shows us that in a group of N people, the odds
 that two of them have matching birthdays is surprisingly large.
 This program does a Monte Carlo simulation (that is, repeated random
 simulations) to explore this concept.
 (It's not actually a paradox, it's just a surprising result.)""")

while True:
    print("How many birthdays shall i generate?(Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_of_days = int(response)
        break
print()

# Generate and display the birthdays:
print("Here are", num_of_days, "birthdays:")
birthdays = get_birthday(num_of_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # To display a comma for each birthday after the first birthday
        print(",", end="")
        month_name = MONTHS[birthday.month - 1]
        date_text = f"{month_name} {birthday.day}"
        print(date_text, end="")
print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the resuts:
print("In this simulation,", end="")

if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f"{month_name} {match.day}"
    print("multiple people have a birthday on", date_text)
else:
    print("there are no matching birthdays.")
print()

# Run through 100,000 simulations:
print(f"generating {num_of_days} random birthdays 100,000 times.....")
input("Press Enter to begin....")

print("Let's run another 100,000 simulations.")
sim_match = 0
for i in range(100_000):
    # report on the progress every 10,000 simulations:
    if 1 % 10_000 == 0:
        print(i, "simulation run....")
    birthdays = get_birthday(num_of_days)
    if get_match(birthdays) != None:
        sim_match = sim_match + 1
print("100,000 simulations run.")

# display simulation results:
probability = round(sim_match / 100_000 * 100, 2)
print(
    f"Out of 100,000 simulations of {num_of_days} people there was a \n"
    f"matching birthday in that group {sim_match} times. This means \n"
    f"that {num_of_days} people have a {probability} % chance of having a matching birthday in their group. \n"
    f"That's probably more than you would think!")
