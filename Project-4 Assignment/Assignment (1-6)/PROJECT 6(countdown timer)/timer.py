import time
import sys

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds > 0:
        hrs, rem = divmod(total_seconds, 3600)
        mins, secs = divmod(rem, 60)
        sys.stdout.write(f"\rTime Left: {hrs:02}:{mins:02}:{secs:02}")
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1
    
    print("\nTime's up! ⏰")

def get_time_input():
    while True:
        try:
            user_input = input("Enter time in HH:MM:SS format: ")
            h, m, s = map(int, user_input.split(':'))
            if h >= 0 and m >= 0 and s >= 0:
                return h, m, s
            else:
                print("Please enter non-negative values.")
        except ValueError:
            print("Invalid format. Please enter time in HH:MM:SS format.")

if __name__ == "__main__":
    hours, minutes, seconds = get_time_input()
    countdown_timer(hours, minutes, seconds)
