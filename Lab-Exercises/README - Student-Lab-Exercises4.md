Here is the completed Python script for Lab 4: The Profile Text Normalization Pipeline, fulfilling all the learning objectives and task instructions.


# Lab 4: The Profile Text Normalization Pipeline

raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
sanitized_records = []

# TODO: Write a loop to clean each string element and save it to sanitized_records
for item in raw_survey_inputs:
    # 1. .strip() removes leading and trailing whitespace
    # 2. .lower() converts all uppercase characters to lowercase
    cleaned_item = item.strip().lower()
    
    # 3. Append the dynamically modified string to the new list
    sanitized_records.append(cleaned_item)

# 4. Output both lists to the terminal to visually verify the conversion results
print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {sanitized_records}")



Key Concepts Demonstrated:
String Methods (.strip() and .lower()):
.strip() is chained first to remove all erratic spaces from the beginning and end of the string (e.g., " ALICE SMITH " becomes "ALICE SMITH").
.lower() is then chained to normalize the casing (e.g., "ALICE SMITH" becomes "alice smith"). Chaining them as .strip().lower() is a highly efficient and common Python idiom.
Lists and Loops: A for loop iterates sequentially through every element in the raw_survey_inputs list, processing them one by one.
Appending Dynamic Modifications: The .append() method is used to dynamically add each newly cleaned string to the initially empty sanitized_records list, building the final dataset in memory.
String Interpolation: The final print statements use f-strings to cleanly display both the original messy data and the newly sanitized data side-by-side for easy visual verification.
You can run this script directly in any Python environment to see the before-and-after transformation of the data!