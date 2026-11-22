import random
import time


def create_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]


def partition(arr, low, high, ascending):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if (ascending and arr[j] <= pivot) or (not ascending and arr[j] >= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort_rec(arr, low, high, ascending):
    if low < high:
        p = partition(arr, low, high, ascending)
        _quick_sort_rec(arr, low, p - 1, ascending)
        _quick_sort_rec(arr, p + 1, high, ascending)


def quick_sort(arr, ascending=True):
    _quick_sort_rec(arr, 0, len(arr) - 1, ascending)
    return arr


def check_sorted(arr, ascending=True):
    for i in range(len(arr) - 1):
        if ascending and arr[i] > arr[i + 1]:
            return False
        if not ascending and arr[i] < arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    sample = create_array(10, -20, 50)
    print("Початковий масив:", sample)
    print("За зростанням:   ", quick_sort(sample.copy(), True))
    print("За спаданням:    ", quick_sort(sample.copy(), False))

    for size in (1_000, 10_000, 100_000):
        source = create_array(size, -10**6, 10**6)
        print(f"\nРозмір масиву: {size}")

        for ascending in (True, False):
            data = source.copy()

            t0 = time.perf_counter()
            quick_sort(data, ascending)
            dt = time.perf_counter() - t0

            order = "за зростанням" if ascending else "за спаданням"
            ok = check_sorted(data, ascending)
            print(f"  {order}: {dt:.4f} с | відсортовано: {ok}")