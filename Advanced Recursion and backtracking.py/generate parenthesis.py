class Solution(object):
    def generateParenthesis(self, n):
        n=2
        brackets = [""] * n * 2
        result = []

        def solve(index, total, brackets, result):
            if index >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return

            if total > len(brackets) // 2:
                return
            elif total < 0:
                return

            brackets[index] = "("
            solve(index + 1, total + 1, brackets, result)

            brackets[index] = ")"
            solve(index + 1, total - 1, brackets, result)

        solve(0, 0, brackets, result)
        return result
