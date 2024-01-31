Berikut adalah beberapa contoh program dasar dalam bahasa Python:

### 1. Tipe Data
```python
integerVar = 10
floatVar = 3.14
charVar = 'A'

print("Integer:", integerVar)
print("Float:", floatVar)
print("Char:", charVar)
```

### 2. Percabangan
```python
number = 5

if number > 0:
    print("Positif")
elif number < 0:
    print("Negatif")
else:
    print("Nol")
```

### 3. Perulangan
```python
for i in range(1, 6):
    print(i, end=' ')

print()
```

### 4. Fungsi
```python
def add(a, b):
    return a + b

result = add(3, 5)
print("Hasil penjumlahan:", result)
```

### 5. Array
```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=' ')

print()
```

### 6. Sorting
#### Selection Sort
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print("Sorted array:", numbers)
```

#### Insertion Sort
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers = [12, 11, 13, 5, 6]
insertion_sort(numbers)
print("Sorted array:", numbers)
```

#### Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted array:", numbers)
```

#### Counting Sort
```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    index = 0
    for i in range(max_val + 1):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

numbers = [4, 2, 1, 4, 3, 1]
counting_sort(numbers)
print("Sorted array:", numbers)
```

### 7. Searching
#### Sequential Search
```python
def sequential_search(arr, key):
    for i, element in enumerate(arr):
        if element == key:
            return i
    return -1

numbers = [2, 4, 6, 8, 10]
key = 8
result = sequential_search(numbers, key)

if result != -1:
    print(f"Elemen {key} ditemukan pada indeks {result}.")
else:
    print(f"Elemen {key} tidak ditemukan dalam array.")
```

#### Binary Search
```python
def binary_search(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [2, 4, 6, 8, 10]
key = 6
result = binary_search(numbers, 0, len(numbers) - 1, key)

if result != -1:
    print(f"Elemen {key} ditemukan pada indeks {result}.")
else:
    print(f"Elemen {key} tidak ditemukan dalam array.")
```

### 8. Algoritma Rekursif
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"Faktorial dari {num} adalah {factorial(num)}")
```

### 9. File Handling
```python
data = "Hello, File Handling!"

with open("example.txt", "w") as file:
    file.write(data)

print("File berhasil ditulis.")
```