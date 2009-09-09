# -*- coding: utf-8 -*-

class DimensionError(Exception):
    def __init__(self, message):
        self.messages = message
        
    def __str__(self):
        return repr(self.messages)

class Matrix(list):

    _CC = (0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49)

    def _validate(self):
        size = len(self)
        v = reduce(lambda r, el: (len(el) == size) and r, self)
        if not v:
            raise DimensionError('Wrong dimension!')

    @property
    def _z(self):
        self._validate()
        result = []
        size = len(self)
        for row in self:
            zk = reduce(lambda r, el: r*el, row)
            result.append(pow(zk, 1./size))
        return result

    @property
    def _w(self):
        result = []
        z = self._z
        sumz = sum(z)
        #result = [item/sumz for item in z]
        for item in z:
            result.append(item/sumz)
        return result

    @property
    def _y(self):
        result = []
        size = len(self)
        w = self._w
        for i in range(size):
            s = 0
            for j in range(size):
                s = s + self[i][j] * w[j]
            result.append(s)
        return result

    @property
    def _gamma(self):
        return sum(self._y)

    @property
    def _IC(self):
        size = len(self)
        return (self._gamma - size)/(size - 1)

    @property
    def _OC(self):
        return self._IC / self._CC[len(self)]

class MAI(object):
    '''

    '''
    _criterion = None
    _alters = []

    def __init__(self, cr, alters=[]):
        self._criterion = cr
        self._alters = alters

    def add_alter(self, alter):
        self._alters.append(alter)

m = Matrix()
m.append([1, 5, 3, 7, 6, 6, 1/3., 1/4.])
m.append([1/5., 1, 1/3., 5, 3, 3, 1/5., 1/7.])
m.append([1/3., 3, 1, 6, 3, 4, 6, 1/5.])
m.append([1/7., 1/5., 1/6., 1, 1/3., 1/4., 1/7., 1/8.])
m.append([1/6., 1/3., 1/3., 3, 1, 1/2., 1/5., 1/6.])
m.append([1/6., 1/3., 1/4., 4, 2, 1, 1/5., 1/6.])
m.append([3, 5, 1/6., 7, 5, 5, 1, 1/2.])
m.append([4, 7, 5, 8, 6, 6, 2, 1])

