def generate_profile(age):
    # Return life stage based on age
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    return "Adult"

user_name = input("Hello user! Enter your name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)  # Convert input to integer

current_age = 2025 - birth_year  # Simple age calculation
hobbies = []

# Collect hobbies until 'stop'
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ").strip()
    if hobby.lower() == "stop":
        break
    if hobby:
        hobbies.append(hobby)

life_stage = generate_profile(current_age)

# Build user profile dictionary
user_profile = { 'name': user_name,
                'age': current_age,
                 'stage': life_stage,
                 'hobby': hobbies
                 }


print(f"Profile Summary:")
print(f"Name: {user_profile['name']} \nAge: {user_profile['age']} \nStage: {user_profile['stage']}")

# Print hobbies if provided
if hobbies:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")
else:
    print("You didn't mention any hobby.")