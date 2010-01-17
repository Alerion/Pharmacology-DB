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
    
    def w(self):
        return self._w
    
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
    
    def y(self):
        return self._y
    
    @property
    def _gamma(self):
        return sum(self._y)
    
    def gamma(self):
        return self._gamma
    
    @property
    def _IC(self):
        size = len(self)
        return (self._gamma - size)/(size - 1)

    def IC(self):
        return self._IC

    @property
    def _OC(self):
        return self._IC / self._CC[len(self)]
    
    def OC(self):
        return self._OC

class MAI(object):
    
    def __init__(self, cr, items):
        self._criterion = self._get_w(cr)
        self._items = items
        self._alters = []
        self._size = None
        print self._items
        
    def _get_w(self, el):
        if isinstance(el, Matrix):
            return el._w
        else:
            raise Exception('Element must be Matrix instance.')

    def add_alter(self, alter):
        if self._size and not len(alter) == self._size:
            raise Exception('Alternatives must be same size.')
            self._alters.append(self._get_w(alter))
        elif not self._size:
            self._size = len(alter)
        self._alters.append(self._get_w(alter))
        
    def __call__(self, cr=None):
        if not len(self._items) == self._size:
            raise Exception('Not enought items.')
        if cr is None:
            cr = self._criterion
        else:
            cr = self._get_w(cr)
        cr_len = len(cr)
        for i in range(self._size):
            sum = 0
            for j in range(cr_len):
                sum += self._alters[j][i] * cr[j]
            yield sum
            
    def sort(self):
        output = []
        result = [item for item in self()]
        for i in range(len(result)):
            output.append({
                'item': self._items[i],
                'value': round(result[i], 2)
            })
        output.sort(lambda x, y: cmp(y['value'], x['value']))
        return output
        

"""
m = Matrix()
m.append([1, 5, 3, 7, 6, 6, 1/3., 1/4.])
m.append([1/5., 1, 1/3., 5, 3, 3, 1/5., 1/7.])
m.append([1/3., 3, 1, 6, 3, 4, 6, 1/5.])
m.append([1/7., 1/5., 1/6., 1, 1/3., 1/4., 1/7., 1/8.])
m.append([1/6., 1/3., 1/3., 3, 1, 1/2., 1/5., 1/6.])
m.append([1/6., 1/3., 1/4., 4, 2, 1, 1/5., 1/6.])
m.append([3, 5, 1/6., 7, 5, 5, 1, 1/2.])
m.append([4, 7, 5, 8, 6, 6, 2, 1])

mai = MAI(m)

a1 = Matrix()
a1.append([1, 6, 8])
a1.append([1/6., 1, 4])
a1.append([1/8., 1/4., 1])
mai.add_alter(a1)

a2 = Matrix()
a2.append([1, 7, 1/5.])
a2.append([1/7., 1, 1/8.])
a2.append([5, 8, 1])
mai.add_alter(a2)

a3 = Matrix()
a3.append([1, 8, 6])
a3.append([1/8., 1, 1/4.])
a3.append([1/6., 4, 1])
mai.add_alter(a3)

a4 = Matrix()
a4.append([1, 1, 1])
a4.append([1, 1, 1])
a4.append([1, 1, 1])
mai.add_alter(a4)

a5 = Matrix()
a5.append([1, 5, 4])
a5.append([1/5., 1, 1/3.])
a5.append([1/4., 3, 1])
mai.add_alter(a5)

a6 = Matrix()
a6.append([1, 8, 6])
a6.append([1/8., 1, 1/5.])
a6.append([1/6., 5, 1])
mai.add_alter(a6)

a7 = Matrix()
a7.append([1, 1/2., 1/2.])
a7.append([2, 1, 1])
a7.append([2, 1, 1])
mai.add_alter(a7)

a8 = Matrix()
a8.append([1, 1/7., 1/5.])
a8.append([7, 1, 3])
a8.append([5, 1/3., 1])
mai.add_alter(a8)

for item in mai():
    print item
"""