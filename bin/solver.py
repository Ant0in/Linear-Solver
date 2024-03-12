
from linear_equation import LinearEquation
from linear_system import LinearSystem



class LinearSystemSolver:

    def __init__(self) -> None:
        pass

    @staticmethod
    def solve_linear_system(system: LinearSystem) -> list:
        
        # En premier lieu on va trianguler le système.
        LinearSystemSolver.triangulate_system(system)

        # Puis on va calculer le vecteur solution en propageant le résultat vers le haut.
        system_solutions: list = system.get_solution_vector()
        system_eq: list[LinearEquation] = system.get_system()[::-1]
        solutions: list = [0] * len(system_eq)

        # Pour chacune des équations, avec i l'élément de la diagonale TR-BL
        for i, eq in zip(range(len(system_eq)-1, -1, -1), system_eq):

            term_by_term_sum: float = 0
            divider: float = eq[i]

            # On ajoute chacun des coefs 
            for w in range(i+1, len(system_eq)):
                term_by_term_sum += solutions[w] * eq[w]

            if divider == 0: pass  # Si le coef est 0, alors la solution est 0.
            else: solutions[i] = (system_solutions[i] - term_by_term_sum) / divider

        return solutions


    @staticmethod
    def triangulate_system(system: LinearSystem) -> None:

        system_eq = system.get_system()

        for i in range(0, len(system_eq)):
            
            # Pour l'équation i, on va récupérer son élément i (diagonale)
            a_i = system_eq[i][i]

            for j in range(i + 1, len(system_eq)):
                
                # Puis pour chacune des équations 'en dessous' de l'équation i, on va lui soustraire eq1 * (a_j/a_i)
                a_j = system_eq[j][i]
                system_eq[j] -= system_eq[i] * (a_j / a_i)





if __name__ == '__main__':
    
    e1 = LinearEquation([1, 2, -1, 1, 6])
    e2 = LinearEquation([-1, 1, 2, -1, 3])
    e3 = LinearEquation([2, -1, 2, 2, 14])
    e4 = LinearEquation([1, 1, -1, 2, 8])
    
    SystemeLineaire = LinearSystem(e1, e2, e3, e4)
    sol = LinearSystemSolver.solve_linear_system(SystemeLineaire)
    print(sol)
