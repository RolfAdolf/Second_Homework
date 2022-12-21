# Вспомогательный  класс с переопределённой
# функцией сравнения
class newString(str):
    def __lt__(self, other):
        return self+other < other+self


def largest_number(n: int, nums: str) -> str:
    nums = [newString(i) for i in nums.split()]
    nums.sort(reverse = True)
    return '0' if (nums[0][0] == '0') else ''.join(nums)