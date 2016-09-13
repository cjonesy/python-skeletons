"""Skeleton for 'pyspark.functions' module."""

def abs(col):
    """Computes the absolute value.
    
    New in version 1.3.

    :type col: T
    """
    pass

def acos(col):
    """Computes the cosine inverse of the given value; the returned angle is in the range0.0 through pi.
    
    New in version 1.4.
    
    :type col: T
    :rtype: pyspark.sql.Column
    """
    pass

def add_months(start, months):
    """Returns the date that is `months` months after `start`
    
    >>> df = sqlContext.createDataFrame([('2015-04-08',)], ['d'])
    >>> df.select(add_months(df.d, 1).alias('d')).collect()
    [Row(d=datetime.date(2015, 5, 8))]

    New in version 1.5.

    :type start: T
    :type months: T
    :rtype: pyspark.sql.Column
    """
    pass

def approxCountDistinct(col, rsd=None):
    """Returns a new :class:`Column` for approximate distinct count of ``col``.

    >>> df.agg(approxCountDistinct(df.age).alias('c')).collect()
    [Row(c=2)]

    New in version 1.3.

    :type col: pyspark.sql.Column
    :type rsd: float
    :rtype: pyspark.sql.Column
    """
    pass

def lit(col):
    """Creates a Column of literal value.
    
    :type col: T
    :rtype: pyspark.sql.Column
    """
    pass
