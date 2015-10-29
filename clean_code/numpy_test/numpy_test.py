from numpy import *

# array
print "random array:"
print random.rand(4, 4)

# matrix
randMat = mat(random.rand(4, 4))
print "random matrix:"
print randMat
# matrix inversion
invRanMat = randMat.I

print randMat * invRanMat

# eye matrix
myEye = randMat * invRanMat
print myEye - eye(4)

