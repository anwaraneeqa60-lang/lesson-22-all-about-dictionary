test_dict = {'codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}
print("Test Dictionary:", test_dict)
check_value = int(input("Enter the value you want to check the frequency for: "))
frequency = list(test_dict.values()).count(check_value)
print(f"The frequency of value {check_value} is: {frequency}")