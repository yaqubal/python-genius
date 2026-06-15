Here is the completed Python script for Lab 5: System Alert Flag Evaluator, fulfilling all the learning objectives and task instructions.


# Lab 5: System Alert Flag Evaluator

# Change these values to verify different execution paths!
is_active = True
cpu_percent = 94.5
is_production = True

# TODO: Build your compound logical matching condition statement
# Rule 1: Server is not active -> (not is_active)
# Rule 2: CPU is critically high AND it is production -> (cpu_percent > 90.0 and is_production)
# Alert triggers if ANY of these rules are met -> (Rule 1 or Rule 2)

should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

# Control execution states based on the boolean evaluation
if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")
	
	
	
Key Concepts Demonstrated:
Complex Boolean Evaluations:
The not operator is used to invert the is_active flag (triggering an alert if it is False).
The and operator groups the CPU and environment checks together, ensuring both must be true for that specific rule to trigger.
The or operator sits at the top level, meaning if either the server is down OR the high-CPU/production condition is met, the overall should_alert variable becomes True.
Logical Comparisons: We use the greater-than operator (>) to evaluate the float value of cpu_percent against the 90.0 threshold.
Control Execution States: The final if/else block cleanly routes the program's execution path based on the single, pre-evaluated should_alert boolean, keeping the control flow readable and maintainable.
Try modifying the variables to test the logic:
Test Case 1 (Current): is_active=True, cpu=94.5, prod=True ➔ ALERT (High CPU in production)
Test Case 2: is_active=False, cpu=50.0, prod=False ➔ ALERT (Server is not active)
Test Case 3: is_active=True, cpu=95.0, prod=False ➔ OK (High CPU, but not in production, so no alert)
Test Case 4: is_active=True, cpu=85.0, prod=True ➔ OK (Safe margins)	