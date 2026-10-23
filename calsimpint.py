
# Function to calculate simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

# Main program
if __name__ == "__main__":
    principal = 80000
    rate = 2
    time = 4

    interest = simple_interest(principal, rate, time)

    print("Principal Amount:", principal)
    print("Rate of Interest:", rate, "%")
    print("Time:", time, "years")
    print("Simple Interest:", interest)
