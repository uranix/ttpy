# Here we import all necessary staff from external files

# tools
from .tools import matvec, col, kron, dot, mkron, concatenate, sum, reshape
from .tools import eye, diag, Toeplitz, qshift, qlaplace_dd, IpaS
from .tools import ones, rand, linspace, sin, cos, delta, stepfun, unit, xfun

# main classes
from .matrix import matrix
from .vector import vector, tensor

# utility
from . import utils
