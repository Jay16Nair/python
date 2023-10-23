  sum_of_even_numbers = 0
  sum_of_odd_numbers = 0
  for number in arr:
    if number % 2 == 0:
      sum_of_even_numbers += number
    else:
      sum_of_odd_numbers += number
  return sum_of_even_numbers, sum_of_odd_numbers


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even_numbers, sum_of_odd_numbers = calculate_sum_of_even_and_odd_numbers(arr)

print("Sum of even numbers:", sum_of_even_numbers)
print("Sum of odd numbers:", sum_of_odd_numbers)
