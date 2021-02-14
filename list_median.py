def median(lst):
    sorted_list = sorted(lst)
    print(sorted_list)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[int(index_1)] + sorted_list[int(index_2)]) / 2.0
        return mean
   
num1 = [2, 1]
num2 = [3, 5, 2, 1, 4]

print(median(num1))
print(median(num2))