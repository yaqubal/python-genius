# Lab 1: The Smart Survey Onboarding Engine

# 1. TODO: Capture inputs from user (Name, Age, Developer Status)
name = input("Enter your name: ")
# Type casting the age input to an integer
age = int(input("Enter your age: "))
# Capturing developer status and normalizing the string (lowercase, no extra spaces)
developer_input = input("Are you a developer? (yes/no): ").strip().lower()

# Convert the string input into a boolean for easier conditional logic
is_developer = (developer_input == "yes")

# 2. TODO: Evaluate conditional logic to determine the clearance tier
if age < 18:
    tier = "Tier 3: Guest"
elif age >= 18 and is_developer:
    tier = "Tier 1: Admin Infrastructure Access"
else:
    # This covers age >= 18 and not a developer
    tier = "Tier 2: Standard Executive Access"

# 3. TODO: Print out the final profile card using an f-string
print("\n" + "="*40)
print("       PROFILE CONFIGURATION SUMMARY")
print("="*40)
print(f"Name             : {name}")
print(f"Age              : {age}")
print(f"Developer Status : {'Yes' if is_developer else 'No'}")
print(f"Clearance Tier   : {tier}")
print("="*40 + "\n")