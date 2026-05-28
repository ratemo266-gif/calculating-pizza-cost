def calculate_pizza_cost():
    
    print("\n" + "=" * 50)
    print("PYTHON PIZZA ORDER COST CALCULATOR")
    print("=" * 50)
    
    while True:
        print("\nPizza Sizes:")
        print("  1. Small - $8")
        print("  2. Large - $12")
        size_choice = input("Enter pizza size (small/large): ").lower().strip()
        
        if size_choice == "small":
            base_cost = 8
            size_display = "Small"
            break
        elif size_choice == "large":
            base_cost = 12
            size_display = "Large"
            break
        else:
            print("Invalid choice! Please enter 'small' or 'large'.")
    
    while True:
        try:
            toppings = int(input("\nEnter number of additional toppings: "))
            if toppings >= 0:
                toppings_cost = toppings * 1
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            distance = float(input("Enter delivery distance in miles: "))
            if distance >= 0:
                break
            else:
                print("Please enter a non-negative distance.")
        except ValueError:
            print("Please enter a valid number.")
    
    if distance == 0:
        delivery_fee = 0
        delivery_note = "Pickup (no delivery fee)"
    elif distance <= 5:
        delivery_fee = 2
        delivery_note = "First 5 miles: $2"
    else:
        extra_miles = distance - 5
        delivery_fee = 2 + extra_miles
        delivery_note = f"First 5 miles: $2 + {extra_miles:.1f} extra miles: ${extra_miles:.2f}"
    
    total_cost = base_cost + toppings_cost + delivery_fee
    
    print("\n" + "=" * 50)
    print("ORDER SUMMARY")
    print("=" * 50)
    print(f"Pizza size: {size_display} Pizza")
    print(f"   Base price: ${base_cost:.2f}")
    print(f"\nToppings: {toppings}")
    print(f"   Toppings cost: ${toppings_cost:.2f} ($1 each)")
    print(f"\nDelivery: {distance:.1f} miles")
    print(f"   Delivery fee: ${delivery_fee:.2f}")
    print(f"   ({delivery_note})")
    print("-" * 50)
    print(f"TOTAL COST: ${total_cost:.2f}")
    print("=" * 50)
    print("Thank you for ordering with Python Pizza!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    calculate_pizza_cost()