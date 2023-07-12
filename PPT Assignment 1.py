# 1. Reverse a string without using any built-in string reversal functions
def reverse_string(string):
    reversed_string = ''
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)


# 2. Check if a given string is a palindrome
def is_palindrome(string):
    string = string.lower()
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

input_string = "level"
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# 3. Find the largest element in a given list
def find_largest_element(lst):
    largest = lst[0]
    for element in lst:
        if element > largest:
            largest = element
    return largest

input_list = [10, 5, 8, 15, 3]
largest_element = find_largest_element(input_list)
print("The largest element in the list is:", largest_element)


# 4. Count the occurrence of each element in a list
def count_occurrences(lst):
    occurrences = {}
    for element in lst:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1
    return occurrences

input_list = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 4]
occurrences = count_occurrences(input_list)
print("Occurrences:", occurrences)


# 5. Find the second largest number in a list
def find_second_largest(lst):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

input_list = [10, 5, 8, 15, 3]
second_largest = find_second_largest(input_list)
print("The second largest number in the list is:", second_largest)


# 6. Remove duplicate elements from a list
def remove_duplicates(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_list = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 4]
result = remove_duplicates(input_list)
print("List with duplicates removed:", result)


# 7. Calculate the factorial of a given number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
factorial_result = factorial(number)
print("Factorial of", number, "is:", factorial_result)


# 8. Check if a given number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 17
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


# 9. Sort a list of integers in ascending order
def sort_list(lst):
    return sorted(lst)

input_list = [5, 2, 8, 1, 10]
sorted_list = sort_list(input_list)
print("Sorted list:", sorted_list)


# 10. Find the sum of all numbers in a list
def sum_of_numbers(lst):
    total = 0
    for num in lst:
        total += num
    return total

input_list = [1, 2, 3, 4, 5]
sum_result = sum_of_numbers(input_list)
print("Sum of numbers in the list:", sum_result)


# 11. Find the common elements between two lists
def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print("Common elements:", common_elements)


# 12. Check if a given string is an anagram of another string
def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    return sorted(string1) == sorted(string2)

string1 = "listen"
string2 = "silent"
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# 13. Generate all permutations of a given string
def permute_string(string):
    if len(string) == 1:
        return [string]

    permutations = []
    for i in range(len(string)):
        char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for perm in permute_string(remaining_chars):
            permutations.append(char + perm)
    return permutations

input_string = "abc"
permutations = permute_string(input_string)
print("Permutations:", permutations)


# 14. Calculate the Fibonacci sequence up to a given number of terms
def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

num_terms = 10
fibonacci_seq = fibonacci_sequence(num_terms)
print("Fibonacci sequence:", fibonacci_seq)


# 15. Find the median of a list of numbers
def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        median = sorted_numbers[n // 2]
    return median

number_list = [10, 5, 8, 15, 3]
median = find_median(number_list)
print("Median of the list:", median)


# 16. Check if a given list is sorted in non-decreasing order
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

input_list = [1, 2, 3, 4, 5]
if is_sorted(input_list):
    print("The list is sorted.")
else:
    print("The list is not sorted.")


# 17. Find the intersection of two lists
def find_intersection(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = find_intersection(list1, list2)
print("Intersection:", intersection)


# 18. Find the maximum subarray sum in a given list
def find_maximum_subarray_sum(lst):
    max_sum = current_sum = lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

input_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray_sum = find_maximum_subarray_sum(input_list)
print("Maximum subarray sum:", max_subarray_sum)


# 19. Remove all vowels from a given string
def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)

input_string = "Hello, World!"
string_without_vowels = remove_vowels(input_string)
print("String without vowels:", string_without_vowels)


# 20. Reverse the order of words in a given sentence
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(words[::-1])
    return reversed_words

input_sentence = "Hello, World!"
reversed_sentence = reverse_words(input_sentence)
print("Reversed sentence:", reversed_sentence)

# 21. Check if two strings are anagrams of each other
def are_anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    return sorted(string1) == sorted(string2)

string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# 22. Find the first non-repeating character in a string
def find_first_non_repeating_character(string):
    character_counts = {}
    for char in string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    for char in string:
        if character_counts[char] == 1:
            return char

    return None

input_string = "abacabad"
first_non_repeating_char = find_first_non_repeating_character(input_string)
if first_non_repeating_char:
    print("The first non-repeating character is:", first_non_repeating_char)
else:
    print("There are no non-repeating characters.")


# 23. Find the prime factors of a given number
def find_prime_factors(number):
    prime_factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return prime_factors

input_number = 24
prime_factors = find_prime_factors(input_number)
print("Prime factors of", input_number, "are:", prime_factors)


# 24. Check if a given number is a power of two
def is_power_of_two(number):
    if number <= 0:
        return False
    return number & (number - 1) == 0

input_number = 16
if is_power_of_two(input_number):
    print(input_number, "is a power of two.")
else:
    print(input_number, "is not a power of two.")


# 25. Merge two sorted lists into a single sorted list
def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
print("Merged list:", merged_list)


# 26. Find the mode of a list of numbers
def find_mode(numbers):
    num_counts = {}
    for num in numbers:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    max_count = max(num_counts.values())
    mode = [num for num, count in num_counts.items() if count == max_count]
    return mode

number_list = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 4]
mode = find_mode(number_list)
print("Mode:", mode)


# 27. Find the greatest common divisor (GCD) of two numbers
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 36
num2 = 48
gcd = find_gcd(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)


# 28. Calculate the square root of a given number
def square_root(number):
    if number < 0:
        return None

    guess = number
    while abs(guess * guess - number) > 1e-6:
        guess = (guess + number / guess) / 2

    return guess

input_number = 16
sqrt = square_root(input_number)
if sqrt is not None:
    print("Square root of", input_number, "is:", sqrt)
else:
    print("Invalid input. Cannot calculate square root.")


# 29. Check if a given string is a valid palindrome ignoring non-alphanumeric characters
import re

def is_valid_palindrome(string):
    cleaned_string = re.sub(r'\W+', '', string.lower())
    return cleaned_string == cleaned_string[::-1]

input_string = "A man, a plan, a canal: Panama"
if is_valid_palindrome(input_string):
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")


# 30. Find the minimum element in a rotated sorted list
def find_minimum_in_rotated_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        mid = (left + right) // 2
        if lst[mid] > lst[right]:
            left = mid + 1
        else:
            right = mid

    return lst[left]

rotated_list = [4, 5, 6, 7, 0, 1, 2]
minimum = find_minimum_in_rotated_list(rotated_list)
print("Minimum element in the rotated list:", minimum)


# 31. Find the sum of all even numbers in a list
def sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_evens = sum_of_even_numbers(input_list)
print("Sum of even numbers:", sum_of_evens)


# 32. Calculate the power of a number using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

base = 2
exponent = 3
result = power(base, exponent)
print(base, "raised to the power of", exponent, "is:", result)


# 33. Remove duplicates from a list while preserving the order
def remove_duplicates_preserve_order(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_list = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 4]
result = remove_duplicates_preserve_order(input_list)
print("List with duplicates removed while preserving order:", result)


# 34. Find the longest common prefix among a list of strings
def find_longest_common_prefix(strings):
    if not strings:
        return ""

    shortest_string = min(strings, key=len)
    for i, char in enumerate(shortest_string):
        if any(string[i] != char for string in strings):
            return shortest_string[:i]

    return shortest_string

input_strings = ["flower", "flow", "flight"]
longest_common_prefix = find_longest_common_prefix(input_strings)
print("Longest common prefix:", longest_common_prefix)


# 35. Check if a given number is a perfect square
def is_perfect_square(number):
    sqrt = number ** 0.5
    return int(sqrt) ** 2 == number

input_number = 25
if is_perfect_square(input_number):
    print(input_number, "is a perfect square.")
else:
    print(input_number, "is not a perfect square.")


# 36. Calculate the product of all elements in a list
def product_of_elements(lst):
    product = 1
    for num in lst:
        product *= num
    return product

input_list = [1, 2, 3, 4, 5]
product = product_of_elements(input_list)
print("Product of elements:", product)


# 37. Reverse the order of words in a sentence while preserving the word order
def reverse_words_preserve_order(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

input_sentence = "Hello, World!"
reversed_sentence = reverse_words_preserve_order(input_sentence)
print("Reversed sentence while preserving word order:", reversed_sentence)


# 38. Find the missing number in a given list of consecutive numbers
def find_missing_number(lst):
    n = len(lst) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

input_list = [1, 2, 4, 5, 6]
missing_number = find_missing_number(input_list)
print("Missing number:", missing_number)


# 39. Find the sum of digits of a given number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number) if digit.isdigit())

input_number = 12345
digit_sum = sum_of_digits(input_number)
print("Sum of digits of", input_number, "is:", digit_sum)


# 40. Check if a given string is a valid palindrome considering case sensitivity
def is_valid_palindrome_case_sensitive(string):
    return string == string[::-1]

input_string = "Racecar"
if is_valid_palindrome_case_sensitive(input_string):
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")


# 41. Find the smallest missing positive integer in a list
def find_smallest_missing_positive_integer(lst):
    n = len(lst)
    contains_one = False

    # Step 1: Mark numbers out of range [1, n] as 1
    for i in range(n):
        if lst[i] == 1:
            contains_one = True
        elif lst[i] <= 0 or lst[i] > n:
            lst[i] = 1

    if not contains_one:
        return 1

    # Step 2: Mark present elements as negative
    for i in range(n):
        index = abs(lst[i]) - 1
        if lst[index] > 0:
            lst[index] = -lst[index]

    # Step 3: Find the first positive index
    for i in range(n):
        if lst[i] > 0:
            return i + 1

    # Step 4: All indices are marked, so the smallest missing positive is n + 1
    return n + 1

input_list = [3, 4, -1, 1]
smallest_missing_positive = find_smallest_missing_positive_integer(input_list)
print("Smallest missing positive integer:", smallest_missing_positive)


# 42. Find the longest palindrome substring in a given string
def find_longest_palindrome_substring(string):
    def expand_around_center(left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1:right]

    longest_palindrome = ""
    for i in range(len(string)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)

        if len(odd_palindrome) > len(longest_palindrome):
            longest_palindrome = odd_palindrome
        if len(even_palindrome) > len(longest_palindrome):
            longest_palindrome = even_palindrome

    return longest_palindrome

input_string = "babad"
longest_palindrome = find_longest_palindrome_substring(input_string)
print("Longest palindrome substring:", longest_palindrome)


# 43. Find the number of occurrences of a given element in a list
def count_occurrences(lst, element):
    return lst.count(element)

input_list = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4, 4]
element = 2
occurrences = count_occurrences(input_list, element)
print("Occurrences of", element, "in the list:", occurrences)


# 44. Check if a given number is a perfect number
def is_perfect_number(number):
    if number <= 0:
        return False

    divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != 1 and i * i != number:
                divisors.append(number // i)

    return sum(divisors) == number

input_number = 28
if is_perfect_number(input_number):
    print(input_number, "is a perfect number.")
else:
    print(input_number, "is not a perfect number.")


# 45. Remove all duplicates from a string
def remove_duplicates_from_string(string):
    return ''.join(set(string))

input_string = "Hello, World!"
string_without_duplicates = remove_duplicates_from_string(input_string)
print("String without duplicates:", string_without_duplicates)


# 46. Find the first missing positive number in a given list
def find_first_missing_positive(lst):
    n = len(lst)

    # Step 1: Move positive numbers to their correct positions
    for i in range(n):
        while 1 <= lst[i] <= n and lst[lst[i] - 1] != lst[i]:
            lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]

    # Step 2: Find the first missing positive number
    for i in range(n):
        if lst[i] != i + 1:
            return i + 1

    # Step 3: All positive numbers from 1 to n are present, so the first missing positive is n + 1
    return n + 1

input_list = [3, 4, -1, 1]
first_missing_positive = find_first_missing_positive(input_list)
print("First missing positive number:", first_missing_positive)

