
# Problem:
# You have a list of job offers, each with a deadline and a payment amount.
# Each day in a week can only accommodate one job.
# Your goal is to select jobs in such a way that you maximize your total payment (profit) while respecting the deadlines.

# Approach to Solve the Problem:
# 1. Sort Jobs by Payment:
#    - Order the jobs from highest payment to lowest payment. This ensures that higher-paying jobs are considered first.

# 2. Initialize Timeline:
#    - Create a list with 7 elements (for each day of the week), initialized to False indicating that all days are free initially.

# 3. Schedule Jobs:
#    - For each job, determine the latest possible day it can be scheduled, based on its deadline.
#    - Attempt to schedule the job on the latest available day before or on its deadline.
#    - If a free day is found, mark it as occupied and add the job’s payment to the total profit.

# 4. Return Total Profit:
#    - After all jobs have been processed, return the total accumulated profit.

def optimalFreelancing(jobs): 
    LENGTH_OF_WEEK = 7  # Define the number of days in a week
    profit = 0  # Initialize the total profit to 0
    
    # Sort the jobs in descending order by payment to prioritize higher paying jobs first
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    print("Sorted Jobs by Payment:", jobs)  # Print the sorted jobs

    # Create a list representing each day of the week, initialized to False (indicating each day is free)
    timeline = [False] * LENGTH_OF_WEEK 
    print("Initial Timeline:", timeline)  # Print the initial timeline

    # Iterate through each job in the sorted list
    for job in jobs: 
        # Determine the latest day the job can be scheduled by taking the minimum of the job's deadline and the week's length
        maxTime = min(job["deadline"], LENGTH_OF_WEEK)
        print(f"Processing Job: {job} (Deadline: {job['deadline']}, Payment: {job['payment']})")

        # Iterate from the latest possible day (maxTime - 1) to the earliest day (0)
        for time in reversed(range(maxTime)): 
            if timeline[time] == False:  # Check if the current day is free
                timeline[time] = True  # Mark this day as occupied
                profit += job["payment"]  # Add the job's payment to the total profit
                print(f"Scheduled Job on Day {time}: {job}")  # Print which day the job is scheduled on
                print("Updated Timeline:", timeline)  # Print the updated timeline
                print("Current Profit:", profit)  # Print the current profit
                break  # Exit the loop once the job is scheduled
    
    return profit  # Return the total profit after scheduling all possible jobs

# Dummy data to test the function
jobs = [
    {"deadline": 2, "payment": 50},  # Job 1: Can be completed within 2 days, pays 50
    {"deadline": 1, "payment": 20},  # Job 2: Can be completed within 1 day, pays 20
    {"deadline": 2, "payment": 100}, # Job 3: Can be completed within 2 days, pays 100
    {"deadline": 3, "payment": 30},  # Job 4: Can be completed within 3 days, pays 30
    {"deadline": 5, "payment": 60},  # Job 5: Can be completed within 5 days, pays 60
]

# Call the function with the dummy data and print the result
print("Total Profit:", optimalFreelancing(jobs))  # Output should be 210 (100 + 50 + 60)
