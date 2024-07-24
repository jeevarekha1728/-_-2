# BMI Calculator

# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return None

# Function to classify BMI
def classify_bmi(bmi):
    if bmi is None:
        return "Invalid input for height."
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main function
def main():
    print("Welcome to the BMI Calculator")
    
    try:
        # Prompt user for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Classify BMI
        category = classify_bmi(bmi)
        
        if bmi is not None:
            # Display the result
            print(f"Your BMI is: {bmi:.2f}")
        print(f"Based on your BMI, you are classified as: {category}")
    
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
