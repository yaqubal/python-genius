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