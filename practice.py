def max_num(a, b, c):
    return max(a, b, c)
print(max_num(10, 20, 30))  # Output: 30


def mult_list(numbers):
    product = 1
    for num in numbers:
        product *= num

    return product

print(mult_list([1, 2, 3, 4]))


def rev_string(s):
    return s[::-1]

print(rev_string("hello"))    # Output: "olleh"

def num_within(num, start, end):
    return start <= num <= end

print(num_within(5, 1, 10))  # Output: True
print(num_within(0, 1, 10))  # Output: False


def pascal(n):
    if n <= 0:
        return

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    for row in triangle:
        print(' '.join(map(str, row)))


pascal(5)
