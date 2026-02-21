# Name: Priyadharshini T.
# Roll Number: IITP_AIMLTN_2602813
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")

def find_min_max(numbers):
    minimum=numbers[0]
    maximum=numbers[0]
    
    for number in numbers[1:]:
        if number<minimum:
            minimum=number
        if number>maximum:
            maximum=number
        
        
    print(f"Highest Temperature: {maximum}°C")
        
    print(f"Lowest Temperature: {minimum}°C")

temperatures = [28, 32, 35, 29, 31, 27, 30]
find_min_max(temperatures)

print("\n===== Task 2: Count Hot Days =====")
def find_hot_days(numbers):
    count=0
    for num in numbers:
        if num > 30:
            count+=1
        if num <= 30:
            continue
    print(f"Hot Days (>30°C): {count}")
    
temperatures = [28, 32, 35, 29, 31, 27, 30]
find_hot_days(temperatures)


print("\n===== Task 3: Alert System =====")

def hot_day_alert(numbers):
    count = 0
    
    for day, num in enumerate(numbers, start=1):
        if num >= 40:
            print(f"Alert! Extreme temperature {num}°C detected on Day {day}")
            break
        if num > 30:
            count += 1
        
    print(f"Hot Days before alert: {count}")

temperatures = [28, 32, 35, 40, 31, 33, 30]
hot_day_alert(temperatures)

