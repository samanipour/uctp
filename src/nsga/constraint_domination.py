import constraint.constraints as constraints
import helper.inputs as inputs
def constraint_dominates(ind1, ind2):
    """
    Determine if ind1 dominates ind2 considering constraints.
    
    Args:
    - ind1: first individual
    - ind2: second individual
    
    Returns:
    - True if ind1 constraint-dominates ind2, False otherwise
    """
    uni_program_list = inputs.get_uni_programs()
    instructors_list  = inputs.get_instructors()
    students_list = inputs.get_students()
    violation1 = constraints.total_violation(ind1,uni_program_list=uni_program_list,student_list=students_list)
    violation2 = constraints.total_violation(ind1,uni_program_list=uni_program_list,student_list=students_list)
    
    if violation1 == 0 and violation2 == 0:
        return dominates(ind1, ind2)
    elif violation1 == 0:
        return True
    elif violation2 == 0:
        return False
    else:
        return violation1 < violation2

def dominates(fitness1, fitness2):
    """
    Determine if ind1 dominates ind2 based on fitness values.
    
    Args:
    - ind1: first individual
    - ind2: second individual
    
    Returns:
    - True if ind1 dominates ind2, False otherwise
    """
    better_in_any = False
    for f1, f2 in zip(fitness1, fitness2):
        if f1 > f2:
            return False
        elif f1 < f2:
            better_in_any = True
    return better_in_any
