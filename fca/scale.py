# -*- coding: utf-8 -*-
"""
Holds scale class for conceptual scaling
"""

from context import Context

class Scale(Context):
    """
    Scale inherited from the Context used for conceptual scaling.
    
    Examples
    ========
    
    >>> ct = [[True, False],\
              [False, True]]
    >>> objs = ['value>7', 'value<2']
    >>> attrs = ['>7', '<2']
    >>> c = Context(ct, objs, attrs)
    >>> s = Scale(c)
    
    """

    def __init__(self, context):
        """Constructor"""
        super(Scale, self).__init__(context._table,
                                    context._objects,
                                    context._attributes)


class NominalScale(Scale):
    def __init__(self, attribute, mvcontext):
        """Generate a nominal scale for an attribute based on its values in the
        input many-valued context.
        
        """
        if type(attribute) == str:
            attribute = mvcontext.attributes.index(attribute)
        values = list(set([mvcontext[i][attribute]
                           for i in range(len(mvcontext))]))
        objects = ["value==%s" % v for v in values]
        table = []
        for i in range(len(objects)):
            row = [False] * len(values)
            row[i] = True
            table.append(row)
        super(NominalScale, self).__init__(Context(table, objects, values))

        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
        