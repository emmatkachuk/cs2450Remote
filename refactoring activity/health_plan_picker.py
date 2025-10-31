# Return (recommended_plan, alternate_plan, label) using grouped, readable rules.
# No extra features added; this only flattens the nested decision logic.
def choose_plans(marital_status: str, has_children: str, income: float, health_level: str):
    is_single = (marital_status == "single")
    has_kids = (has_children == "yes")
    is_healthy = (health_level == "no")  # "no" means doesn't visit the doctor a lot

    if is_single:
        label = "Individual"
        if income < 35000:
            if is_healthy:
                return ("Low Income Plan", "High-Deductible B", label)
            else:
                return ("Low Income Plan", "Regular Plan A", label)
        # income >= 35000
        if is_healthy:
            if income > 50000:
                return ("High-Deductible B", "High-Deductible A", label)
            else:
                return ("High-Deductible A", "Regular Plan A", label)
        else:
            if income > 50000:
                return ("Regular Plan A", "Regular Plan B", label)
            else:
                return ("Regular Plan B", "High-Deductible A", label)

    # Married
    if has_kids:
        label = "Family"
        if income < 65000:
            if is_healthy:
                return ("Low Income Plan", "High-Deductible A", label)
            else:
                return ("Low Income Plan", "Regular Plan A", label)
        # income >= 65000
        if is_healthy:
            return ("High-Deductible A", "High-Deductible B", label)
        else:
            return ("Regular Plan A", "Regular Plan B", label)
    else:
        # married, no children -> Individual label in original logic
        label = "Individual"
        if income > 50000:
            if is_healthy:
                return ("High-Deductible A", "High-Deductible B", label)
            else:
                return ("Regular Plan B", "Regular Plan A", label)
        else:
            if is_healthy:
                return ("High-Deductible B", "High-Deductible A", label)
            else:
                return ("Regular Plan A", "Regular Plan B", label)


def determine_insurance_plan():
    print("Welcome to the Insurance Plan Selector!")
    
    # Get user inputs
    age = int(input("Enter your age: "))
    income = float(input("Enter your annual income: "))
    marital_status = input("Are you single or married? (Enter 'single' or 'married'): ").lower()
    has_children = input("Do you have children? (yes/no): ").lower()
    health_level = input("Do you visit the doctor a lot or have any chronic illness? (yes/no): ").lower()

    # Plan details
    plans = {
        "High-Deductible A": {"deductible": "3500/person, 7500/family", "coverage": "80% after deductible", "cost": "1100/month individual, 2300/month family"},
        "High-Deductible B": {"deductible": "4500/person, 9500/family", "coverage": "80% after deductible", "cost": "800/month individual, 1800/month family"},
        "Regular Plan A": {"deductible": "1500/person, 3500/family", "coverage": "80% after deductible", "cost": "2800/month individual, 3800/month family"},
        "Regular Plan B": {"deductible": "1500/person, 3500/family", "coverage": "90% after deductible", "cost": "3500/month individual, 4800/month family"},
        "Low Income Plan": {"deductible": "No deductible", "coverage": "90% coverage", "cost": "1000/month individual, 2000/month family"}
    }

    # Grouped logic (refactor of the old deeply nested ifs)
    if age <= 18:
        print("Sorry, you do not qualify for any plans.")
        return

    recommended, alternate, label = choose_plans(marital_status, has_children, income, health_level)

    print(f"\nRecommended Plan: {recommended} ({label})")
    print_plan_details(recommended, plans)

    print(f"\nAlternate Plan: {alternate} ({label})")
    print_plan_details(alternate, plans)


def print_plan_details(plan_name, plans):
    """Print details of a given insurance plan."""
    print(f"\nPlan: {plan_name}")
    print(f"  Deductible: {plans[plan_name]['deductible']}")
    print(f"  Coverage: {plans[plan_name]['coverage']}")
    print(f"  Cost: {plans[plan_name]['cost']}")


# Run the program
determine_insurance_plan()