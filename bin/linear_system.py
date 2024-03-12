
from linear_equation import LinearEquation


class LinearSystem:

    def __init__(self, *args: LinearEquation) -> None:
        
        assert all(type(exp) is LinearEquation for exp in args), 'LinearSystem args must be LinearEquations'

        self.coef_number: int = len(max([eq.get_padded_coefficients() for eq in args], key=len))
        self.system_matrix: list[LinearEquation] = [eq for eq in args]
        self.pad_system()

    def get_system_matrix(self) -> list[LinearEquation]:
        return self.system_matrix
    
    def pad_system(self) -> None:
        for i in self.get_system_matrix():
            i.set_padding(self.coef_number)





    
e1 = LinearEquation([4, 8, 12, 4])
e2 = LinearEquation([3, 8, 13, 8, 5])
e3 = LinearEquation([2, 9, 18, 11])
A  = LinearSystem(e1, e2, e3)

print(A.get_system_matrix())