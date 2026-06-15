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