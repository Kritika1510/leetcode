class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return reduce(lambda x ,y: x+ (1 if y[1] == '+' else -1),operations ,0)
        