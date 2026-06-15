Here is the completed Python script for Lab 3: The Deployment Budget Optimizer, fulfilling all the learning objectives and task instructions.



# Lab 3: The Deployment Budget Optimizer

def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    # TODO: Calculate total monthly cost (instances * hourly_rate * 720)
    total_cost = instance_count * hourly_rate * 720
    
    # TODO: Implement if/else conditional check against budget_cap
    if total_cost > budget_cap:
        # Calculate how much it exceeded the budget by
        excess_amount = total_cost - budget_cap
        # TODO: Return the appropriate message string
        return f"REJECTED: Budget Exceeded by ${excess_amount:.2f}!"
    else:
        return f"APPROVED: Total Estimated Cost is ${total_cost:.2f}."

# --- Test Cases to verify your execution ---

# Test Case 1: 5 instances * $0.45/hr * 720 hrs = $1620.00 (Cap: $1500.00) -> Should be REJECTED
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))

# Test Case 2: 12 instances * $0.85/hr * 720 hrs = $7344.00 (Cap: $5000.00) -> Should be REJECTED
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))

# Test Case 3 (Added for completeness): 2 instances * $0.50/hr * 720 hrs = $720.00 (Cap: $1000.00) -> Should be APPROVED
print(estimate_deployment_cost(instance_count=2, hourly_rate=0.50, budget_cap=1000.00))



Key Concepts Demonstrated:
Functions with Parameters and Return Values: The function estimate_deployment_cost accepts three specific arguments and uses the return keyword to pass the evaluated string back to the caller, rather than just printing it inside the function.
Arithmetic Operations: We calculate the total monthly cost by multiplying the number of instances, the hourly rate, and the fixed 720 hours in a 30-day month. We also use subtraction to find the excess_amount.
Comparative Conditions: The if total_cost > budget_cap: statement evaluates the boolean condition to determine which execution path (Rejected vs. Approved) the program should take.
String Interpolation (F-Strings): The :.2f format specifier is used inside the f-strings to ensure all dollar amounts are cleanly formatted to exactly two decimal places, which is standard practice for financial outputs.
(Note: I added a third test case where the cost is under the budget cap so you can see the "APPROVED" logic path trigger successfully!)