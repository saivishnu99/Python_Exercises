def print_numbers_occuring_once(numbers):
    # Dictionary to store the count of each number
    count_dict = {}
    
    # Count occurrences of each number in the list
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Print numbers that occur only once
    for num, count in count_dict.items():
        if count == 1:
            print(num)

# Example usage:
if __name__ == "__main__":
    # Input list of numbers
    numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
    
    # Call the function to print numbers occurring only once
    print_numbers_occuring_once(numbers)