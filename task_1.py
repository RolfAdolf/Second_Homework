def psp(n: int) -> str:

        result = []
        s = ''

        # Вспомогательная рекурсивная функция.
        def generate(left, right, s):
            if (left == 0) and (right == 0):
                result.append(s)
            if left > 0:
                generate(left-1, right, s + '(')
            if right > left:
                generate(left, right-1, s + ')')

        generate(n, n, s)

        return '\n'.join(result)