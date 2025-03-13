import time

# Securely store the correct PIN (hardcoded for now)
correct_pin = "2005"

# Initialize the number of attempts and counters for success and failure
count = 3
total_attempts = 0
successful_attempts = 0
failed_attempts = 0

# Loop to allow up to 3 attempts
while True:
    if count > 0:
        # Prompt the user to enter their 4-digit ATM PIN (PIN is visible while typing)
        atm_pin = input("Please enter your 4-digit ATM PIN: ")

        # Check if the input is exactly 4 digits long and consists only of digits
        if len(atm_pin) == 4 and atm_pin.isdigit():
            total_attempts += 1  # Increase total attempts counter
            if atm_pin == correct_pin:
                print("PIN entered successfully.")
                successful_attempts += 1  # Increase successful attempts counter
                break  # Exit the loop if the PIN is correct
            else:
                print("Incorrect PIN. Please try again.")
                failed_attempts += 1  # Increase failed attempts counter
                count -= 1  # Decrease attempts after a failed attempt
        else:
            print("Error: The PIN must be exactly 4 digits long.")
            failed_attempts += 1  # Increase failed attempts counter
            count -= 1  # Decrease attempts for invalid input

    # If the user has reached the maximum number of failed attempts, lock them out
    if count == 0:
        print("You have exceeded the maximum number of attempts. Your account is now locked.")
        print("Please wait for 10 seconds before trying again.")
        time.sleep(10)  # Pause for 10 seconds
        count = 3  # Reset attempts after the 10-second lockout

# Calculate failure rate and availability after the session
if total_attempts > 0:
    failure_rate = (failed_attempts / total_attempts) * 100
    availability = (successful_attempts / total_attempts) * 100
else:
    failure_rate = 0
    availability = 0

# Display the reliability metrics
print("\nSession Reliability Metrics:")
print(f"Total Attempts: {total_attempts}")
print(f"Successful Attempts: {successful_attempts}")
print(f"Failed Attempts: {failed_attempts}")
print(f"Failure Rate: {failure_rate:.2f}%")
print(f"Availability: {availability:.2f}%")