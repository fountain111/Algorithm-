
import numpy as np

def _linprog_simplex(c,A_ub=None,b_ub=None,A_eq=None,b_eq=None,
                     bounds=None,maxiter=1000,disp=False,callback=None,
                     tol=1.0E-12,bland=False,**unknow_options):

        '''
        Solve the follwoing linear programming problem via a tow-phase
        simplex algorithm.::

            minimize c^T * x

            subject to:   A_ub * x <= b_ub
                          B_ub * x <= b_eq

        Parameters
        -----------
        :param c: array_like
                Coefficients of the linear objective function to minimized
        :param A_ub: array_like
                2-D array ,when matrix-multiplied by 'x' ,gives the values of
                the upper-bound inequality constraints at 'x'
        :param b_ub: array_like
                1-D array f values representing the upper-bound of each inequality
                constraint (row) in 'A_ub'
        :param A_eq:array_like
                2-D array when matrix-multiplied by 'x',gives the values of
                the equality constraints at 'x'
        :param b_eq:
                1-D

        :param bounds:
        :param maxiter:
        :param disp:
        :param callback:
        :param tol:
        :param bland:
        :param unknow_options:
        :return:
        '''

        cc = np.asarray(c)

        # The number ofvariables as given by c
        n = len(c)

        # Convert the input arguments to arrays(sized to zero if not provided)
        Aub = np.asarray(A_ub) if A_ub is not None else np.empty([0,len(cc)])
        bub = np.ravel(np.asarray(b_ub)) if b_ub is not None else np.empty([0])

        # Analyze the bouns and determine what modifications to be made to
        # the constraints in order to accommodate them

