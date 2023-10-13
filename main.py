import math
nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

# Linear Search Funtion
def linearSearch(a_list, item):
    for i in range(len(a_list)):
        if a_list[i] == item:
            return i
    return -1

# Binary search function
def binarySearch(a_list, item):
    lower_index = 0
    higher_index = len(a_list) - 1
    done = False
    while not done:
        middle_index = math.floor((lower_index + higher_index) / 2)
        if item == a_list[middle_index]:
            done = True
            return middle_index
        elif item < a_list[middle_index]:
            higher_index = middle_index - 1
        elif item > a_list[middle_index]:
            lower_index = middle_index + 1
        else:
            return -1
    

def main():
    print(binarySearch(nums, 100))
    print(binarySearch(nums, 75))
    print(binarySearch(words, "fish"))
    print(binarySearch(words, "at"))
    print(binarySearch(unsorted, 70))
    
main()
