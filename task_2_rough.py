
# Функция сравнения
def comp_func(str_1: str, str_2: str):
    return str_1+str_2 > str_2+str_1

# Основная функция
def largest_number(n: int, numbers: str) -> str:

    nums = [str(i) for i in numbers.split()]
    n = int(n)

    # Сортировка вставкой. 
    for i in range(1, n):
        key = nums[i]
        w = i
        for j in range(i-1, -1, -1):
            if (comp_func(key, nums[j])):
                nums[j+1] = nums[j]
                w = j
            else:
                break
        nums[w] = key

    if n:
        return '0' if (nums[0][0] == '0') else ''.join(nums)
    else:
        return ' '