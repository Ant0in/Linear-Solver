
from linear_equation import LinearEquation


class LinearSystem:

    def __init__(self, *args: LinearEquation) -> None:
        
        assert all(type(expression) is LinearEquation for expression in args), 'LinearSystem args must be LinearEquations'

        self._greatest_coef_number: int = max([eq.get_length() for eq in args])
        self._system: list[LinearEquation] = [eq for eq in args]
        self.pad_system()

    def get_system(self) -> list[LinearEquation]:
        return self._system
    
    def get_solution_vector(self) -> list[object]:
        return [eq.get_solution() for eq in self.get_system()]
    
    def get_greatest_coef_number(self) -> int:
        return self._greatest_coef_number
    
    def set_greatest_coef_number(self, new_number: int) -> None:
        self._greatest_coef_number = new_number

    def pad_system(self) -> None:
        for eq in self.get_system(): eq.set_padding(self.get_greatest_coef_number())

    def add_linear_equation(self, *new_eqs: LinearEquation) -> None:
        
        assert all(type(i) is LinearEquation for i in new_eqs), 'Can\'t add something that isn\'t a linearEquation to a linear system.'
        
        for eq in new_eqs:

            self.get_system().append(eq)
            new_eq_length: int = eq.get_length()

            if self.get_greatest_coef_number() < new_eq_length:
                self.set_greatest_coef_number(new_eq_length)
                self.pad_system()

    def triangulate_system(self) -> None:

        system: list[LinearEquation] = self.get_system()

        for i in range(0, len(system)):
            
            # Pour l'équation i, on va récupérer son élément i (diagonale)
            a_i = system[i][i]

            for j in range(i + 1, len(system)):
                
                # Puis pour chacune des équations 'en dessous' de l'équation i, on va lui soustraire eq1 * (a_j/a_i)
                a_j = system[j][i]
                system[j] -= system[i] * (a_j / a_i)

