import random

from bubblesort import sort as bubble
from insertionsort import sort as insertion
from mergesort import sort as merge
from utils import measure_time


if __name__ == "__main__":
    data = [random.randint(0, 100_000) for _ in range(100_000)]

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
