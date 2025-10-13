import random

from bubblesort import sort as bubble
from insertionsort import sort as insertion
from mergesort import sort as merge
from quicksort import sort as quick
from utils import measure_time


if __name__ == "__main__":
    data = [random.randint(0, 5000) for _ in range(5000)]

    @measure_time
    def sort_bubble(arr):
        bubble(arr)
    sort_bubble(data)

    @measure_time
    def sort_insertion(arr):
        insertion(arr)
    sort_insertion(data)

    @measure_time
    def sort_merge(arr):
        merge(arr)
    sort_merge(data)


    @measure_time
    def sort_quick(arr):
        quick(arr)
    sort_quick(data)