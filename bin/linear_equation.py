
class LinearEquation:

    def __init__(self, coefs: list[float]) -> None:
        
        assert all(type(i) is float or type(i) is int for i in coefs), 'Equation must be composed of integer or float numbers.'
        
        self._eq: list = coefs
        self.padding: list = []

    def get_coefficients(self) -> list:
        return self._eq[:-1]
    
    def get_padded_coefficients(self) -> list:
        return self.get_coefficients() + self.padding
    
    def get_length(self) -> int:
        return len(self.get_padded_coefficients())
    
    def get_solution(self) -> object:
        return self._eq[-1]
    
    def set_padding(self, n: int) -> None:
        
        padding_number: int = n - len(self.get_coefficients())
        assert padding_number >= 0, 'Cannot pad with a smaller number than coef\'s size.'
        self.padding = [0] * padding_number

    def __sub__(self, other: 'LinearEquation') -> 'LinearEquation':
        
        new_coefs: list = []
        for i, j in zip((self.get_padded_coefficients() + [self.get_solution()]), (other.get_padded_coefficients() + [other.get_solution()])):
            new_coefs.append(i - j)
        return LinearEquation(new_coefs)
    
    def __add__(self, other: 'LinearEquation') -> 'LinearEquation':
        
        new_coefs: list = []
        for i, j in zip((self.get_padded_coefficients() + [self.get_solution()]), (other.get_padded_coefficients() + [other.get_solution()])):
            new_coefs.append(i + j)
        return LinearEquation(new_coefs)
    
    def __mul__(self, k: float) -> 'LinearEquation':

        new_coefs: list = []
        for i in (self.get_padded_coefficients() + [self.get_solution()]):
            new_coefs.append(i * k)
        return LinearEquation(new_coefs)



    def __getitem__(self, idx: int) -> object:
        return self.get_padded_coefficients()[idx]
    
    def __repr__(self) -> str:
        return str(self.get_padded_coefficients())
    