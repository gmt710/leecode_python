class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        List = []
        for i in range(1,n+1):
            if (i % 3 != 0) and (i % 5 != 0):
                List.append(str(i))
            elif (i % 3 == 0) and (i % 5 != 0):
                List.append("Fizz")
            elif (i % 5 == 0) and (i % 3 != 0):
                List.append("Buzz")
            else:
                List.append("FizzBuzz")
        return List
