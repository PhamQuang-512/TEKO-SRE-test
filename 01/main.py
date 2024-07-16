from datetime import datetime, timedelta
from collections import deque

# Function to check the rate limit for each request and return a list of boolean values
def rate_limit_checker(R: int, timestamps: []):
    # Initialize a deque to keep track of the timestamps of the requests within the last hour
    requests = deque()

    for timestamp in timestamps:
        # Convert the timestamp string to a datetime object
        current_time = datetime.fromisoformat(timestamp)
        # Remove requests that are older than 1 hour
        while requests and (current_time - requests[0]) > timedelta(hours=1):
            requests.popleft()

        # Check if the rate limit is not exceeded for the current request   
        if len(requests) < R:
            print("true")
            requests.append(current_time)
        else:
            print("false")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_line = input("Enter N (number of requests) and R (rate limit):\n").strip().split()

    N = int(first_line[0]) 
    R = int(first_line[1])
    timestamps = []

    for n in range(N):
        timestamps.append(input())

    rate_limit_checker(R, timestamps)
