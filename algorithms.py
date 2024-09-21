# algorithms.py
import time
from draw import draw_bars

# Bubble Sort
def bubble_sort(arr, speed, draw_fn):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            draw_fn(arr, highlight_index=j, compare_index=j + 1, message=f"Comparing arr[{j}] and arr[{j + 1}]")
            time.sleep(speed)
            if arr[j] > arr[j + 1]:
                draw_fn(arr, highlight_index=j, compare_index=j + 1, message=f"Swapping arr[{j}] and arr[{j + 1}]")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                time.sleep(speed)
    draw_fn(arr, message="Done! Array is sorted.")

# Selection Sort
def selection_sort(arr, speed, draw_fn):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            draw_fn(arr, highlight_index=min_index, compare_index=j, message=f"Finding min from arr[{i}] to arr[{n-1}]")
            time.sleep(speed)
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        draw_fn(arr, highlight_index=i, message=f"Swapping arr[{i}] with arr[{min_index}]")
        time.sleep(speed)
    draw_fn(arr, message="Done! Array is sorted.")

# Insertion Sort
def insertion_sort(arr, speed, draw_fn):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            draw_fn(arr, highlight_index=j, compare_index=i, message=f"Shifting arr[{j}]")
            time.sleep(speed)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    draw_fn(arr, message="Done! Array is sorted.")
