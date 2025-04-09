def adjust_temperature(suggested_temp):
    return max(18, min(26, suggested_temp + 1))

if __name__ == "__main__":
    temp = int(input("Suggested temp: "))
    print("Adjusted to:", adjust_temperature(temp))