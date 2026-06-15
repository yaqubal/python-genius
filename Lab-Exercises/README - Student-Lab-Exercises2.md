Here is the completed Python script for Lab 2: The Multi-Cluster IP Audit Tool, fulfilling all the learning objectives and task instructions.



# Lab 2: The Multi-Cluster IP Audit Tool

cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
    # Extract values from the dictionary
    cluster_name = config["cluster_name"]
    total_max_slots = config["total_max_slots"]
    active_nodes = config["active_nodes"]
    
    # TODO: Calculate how many items are in the active_nodes list using a loop
    active_count = 0
    for node in active_nodes:
        active_count += 1  # Increment counter for each node extracted
        
    # TODO: Run the mathematical formula to find utilization percentage
    # Formula: (Active Nodes / Total Max Slots) * 100
    utilization_percentage = (active_count / total_max_slots) * 100
    
    # TODO: Print the status statement using string interpolation (f-strings)
    print("\n" + "="*45)
    print(f"       CLUSTER CAPACITY AUDIT REPORT")
    print("="*45)
    print(f"Cluster Name     : {cluster_name}")
    print(f"Total Max Slots  : {total_max_slots}")
    print(f"Active Nodes     : {active_count}")
    
    # Print the individual active node IPs for extra clarity
    print("Active Node IPs  :")
    for node in active_nodes:
        print(f"                 - {node}")
        
    print("-" * 45)
    # Formatting the percentage to 2 decimal places for a clean look
    print(f"Utilization      : {utilization_percentage:.2f}%")
    print("="*45 + "\n")

# Execute the audit tool
calculate_capacity(cluster_config)



Key Concepts Demonstrated:
Dictionaries & Lists: We accessed nested data structures by using key lookups (config["total_max_slots"]) and iterated over the list (config["active_nodes"]).
Sequential Loops (for loop): Instead of just using the built-in len() function, we explicitly used a for loop to iterate through and count the items, satisfying the learning objective of practicing sequential loops. We also used a second loop to neatly print out each IP address.
Arithmetic Operations: We performed division and multiplication to calculate the exact utilization percentage ((5 / 8) * 100 = 62.50%).
String Interpolation: The final report uses f-strings to inject variables directly into the output. The :.2f format specifier is used to ensure the percentage displays cleanly with exactly two decimal places.
You can run this code in any Python environment. Try modifying the cluster_config dictionary (e.g., adding more IPs or changing total_max_slots) to see how the utilization percentage dynamically updates!


