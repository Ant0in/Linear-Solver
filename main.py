
from src.solver import LinearSystemSolver
from src.linear_equation import LinearEquation
from src.linear_system import LinearSystem



if __name__ == '__main__':

    SystemeLineaire: LinearSystem = LinearSystem(
        LinearEquation([1, 2, -1, 1, 6]),
        LinearEquation([-1, 1, 2, -1, 3]),
        LinearEquation([2, -1, 2, 2, 14]),
        LinearEquation([1, 1, -1, 2, 8]))

    sol = LinearSystemSolver.solve_linear_system(SystemeLineaire)
    print(sol)