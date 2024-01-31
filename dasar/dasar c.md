Berikut adalah beberapa contoh program dasar dalam bahasa C:

### 1. Tipe Data
```c
#include <stdio.h>

int main() {
    int integerVar = 10;
    float floatVar = 3.14;
    char charVar = 'A';

    printf("Integer: %d\n", integerVar);
    printf("Float: %f\n", floatVar);
    printf("Char: %c\n", charVar);

    return 0;
}
```

### 2. Percabangan
```c
#include <stdio.h>

int main() {
    int number = 5;

    if (number > 0) {
        printf("Positif\n");
    } else if (number < 0) {
        printf("Negatif\n");
    } else {
        printf("Nol\n");
    }

    return 0;
}
```

### 3. Perulangan
```c
#include <stdio.h>

int main() {
    for (int i = 1; i <= 5; i++) {
        printf("%d ", i);
    }

    printf("\n");

    return 0;
}
```

### 4. Fungsi
```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(3, 5);
    printf("Hasil penjumlahan: %d\n", result);

    return 0;
}
```

### 5. Array
```c
#include <stdio.h>

int main() {
    int numbers[] = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }

    printf("\n");

    return 0;
}
```

### 6. Sorting
#### Selection Sort
```c
#include <stdio.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // Tukar elemen minimum [minIndex] dengan elemen i [i]
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

int main() {
    int numbers[] = {64, 25, 12, 22, 11};
    int n = 5;

    selectionSort(numbers, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", numbers[i]);
    }

    return 0;
}
```

#### Insertion Sort
```c
#include <stdio.h>

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        /* Pindahkan elemen-elemen dari arr[0..i-1] yang lebih besar dari kunci ke satu posisi di depan posisi mereka saat ini. */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int numbers[] = {12, 11, 13, 5, 6};
    int n = 5;

    insertionSort(numbers, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", numbers[i]);
    }

    return 0;
}

```

#### Bubble Sort
```c
#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Tukar arr[j] dan arr[j+1] (samping kanan j)
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int numbers[] = {64, 34, 25, 12, 22, 11, 90};
    int n = 7;

    bubbleSort(numbers, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", numbers[i]);
    }

    return 0;
}

```

#### Counting Sort
```c
#include <stdio.h>

void countingSort(int arr[], int n) {
    // Temukan elemen maksimum (angka paling besar) dalam array
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    // Buat array count untuk menyimpan jumlah setiap elemen
    int count[max + 1];
    for (int i = 0; i <= max; i++) {
        count[i] = 0;
    }

    // Hitung berapa kali setiap elemen dalam array muncul, contoh: elemen 4 muncul dua kali, maka count[4] = 2
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // Modifikasi array count untuk menyimpan jumlah kumulatif
    for (int i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    // Bangun array yang sudah diurutkan
    int output[n];
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    // Salin elemen yang sudah diurutkan kembali ke array asli
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

int main() {
    int numbers[] = {4, 2, 1, 4, 3, 1};
    int n = 6;

    countingSort(numbers, n);

    printf("Array yang sudah diurutkan: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", numbers[i]);
    }

    return 0;
}

```

### 7. Searching
#### Sequential Search
```c
#include <stdio.h>

int sequentialSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            return i;
        }
    }
    return -1;  // Elemen tidak ditemukan
}

int main() {
    int numbers[] = {2, 4, 6, 8, 10};
    int n = 5;
    int key = 8;

    int result = sequentialSearch(numbers, n, key);

    if (result != -1) {
        printf("Elemen %d ditemukan pada indeks %d.\n", key, result);
    } else {
        printf("Elemen %d tidak ditemukan dalam array.\n", key);
    }

    return 0;
}

```

#### Binary Search
```c
#include <stdio.h>

int binarySearch(int arr[], int low, int high, int key) {
    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == key) {
            return mid;  // Kembalikan indeks jika elemen ditemukan
        } else if (arr[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return -1;  // Elemen tidak ditemukan
}

int main() {
    int numbers[] = {2, 4, 6, 8, 10};
    int n = 5;
    int key = 6;

    int result = binarySearch(numbers, 0, n - 1, key);

    if (result != -1) {
        printf("Elemen %d ditemukan pada indeks %d.\n", key, result);
    } else {
        printf("Elemen %d tidak ditemukan dalam array.\n", key);
    }

    return 0;
}

```

### 8. Algoritma Rekursif
```c
#include <stdio.h>

int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1); // memanggil diri sendiri
    }
}

int main() {
    int num = 5;
    printf("Faktorial dari %d adalah %d\n", num, factorial(num));

    return 0;
}
```

### 9. File Handling
```c
#include <stdio.h>

int main() {
    FILE *file;
    char data[50] = "Hello, File Handling!";

    file = fopen("example.txt", "w");
    
    fprintf(file, "%s", data);
    fclose(file);

    printf("File berhasil ditulis.\n");
    

    return 0;
}
```
