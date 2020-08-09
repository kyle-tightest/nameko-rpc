from nameko.rpc import rpc
from nameko.testing.services import worker_factory

class SquareOddIntegers:
    name = "square_odd_service"

    @rpc
    def square(self, integers):
        if not isinstance(integers, list):
            return "input is not list"
        answer = list()
        for x in list(integers):
            if isinstance(x, int) and x % 2 != 0:
                x = x * x
            answer.append(x)
        return answer