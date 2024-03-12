
class LinearEquation:

    def __init__(self, coefs: list[float]) -> None:
        
        assert all(type(i) is float or type(i) is int for i in coefs), 'Equation must be composed of integer or float numbers.'
        
        self._coefs: list = coefs[:-1]
        self.padding: list = []
        self._solution = coefs[-1]

    def get_coefficients(self) -> list:
        return self._coefs
    
    def get_padded_coefficients(self) -> list:
        return self._coefs + self.padding
    
    def get_length(self) -> int:
        return len(self.get_padded_coefficients())
    
    def get_solution(self) -> object:
        return self._solution
    
    def set_padding(self, n: int) -> None:
        
        padding_number: int = n - len(self.get_coefficients())
        assert padding_number >= 0, 'Cannot pad with a smaller number than coef\'s size.'
        self.padding = [0] * padding_number

    def __getitem__(self, idx: int) -> object:
        return self.get_padded_coefficients()[idx]
    
    def __repr__(self) -> str:
        return str(self.get_padded_coefficients())