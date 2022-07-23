# RENAN KRZESINSKI
# BCC
# 10549964

from state import State


def validate(problem, solution):
    '''
    Return true if `solution` is a valid plan for `problem`.
    Otherwise, return false.

    OBSERVATION: you should check action applicability,
    next-state generation and if final state is indeed a goal state.
    It should give you some indication of the correctness of your planner,
    mainly for debugging purposes.
    '''
    state = State(problem.init)
    for a in solution:
        precond = a.precond
        if state.intersect(precond) != precond:
            return False
        state = state.union(a.pos_effect).difference(a.neg_effect)
    goal = State(problem.goal)
    if state.intersect(goal) != goal:
        return False
    return True
