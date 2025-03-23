age = int(input("Enter your age: "))

# Check if the user is a minor
if age < 18:
    print("You are a minor and not eligible to vote.")
else:
    # Get user's country
    country = input("Enter your country name: ").strip().lower()
    # Check if the user is a citizen of the required country
    if country == "your_country_name":  
        print("Great! You have the right to vote.")
    else:
        print("You're not a citizen, so you cannot vote.")
