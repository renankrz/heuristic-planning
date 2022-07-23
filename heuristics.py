# RENAN KRZESINSKI
# BCC
# 10549964

from math import inf
from state import State
import util


def h_naive(state, planning):
    return 0


def h_delete_relaxation(state, planning, f):
    '''
    Return a heuristic value for `state` based on the
    delete-relaxation and the function f given.
    '''
    estimates = {}
    X = State(state)

    # Initialize each proposition in state with 0.
    # Other propositions will be defaulted to inf.
    for p in X:
        estimates[p] = 0

    has_updated = True

    while has_updated:
        has_updated = False
        applicable = planning.applicable(X)
        for a in applicable:
            extended_X = X.union(a.pos_effect)
            if X != extended_X:
                has_updated = True
            X = State(extended_X)
            for p in a.pos_effect:
                sum_precond = 0
                for q in a.precond:
                    if q in estimates:
                        sum_precond += estimates[q]
                    else:
                        estimates[q] = inf
                        sum_precond = inf
                        break
                estimates[p] = min(
                    estimates.get(p, inf),
                    1 + sum_precond)

    return f([estimates.get(p, inf) for p in planning.problem.goal])


def h_add(state, planning):
    '''
    Return heuristic h_add value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    return h_delete_relaxation(state, planning, sum)


def h_max(state, planning):
    '''
    Return heuristic h_max value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    return h_delete_relaxation(state, planning, max)


def h_ff(state, planning):
    '''
    Return heuristic h_ff value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    util.raiseNotDefined()
    ' YOUR CODE HERE '
