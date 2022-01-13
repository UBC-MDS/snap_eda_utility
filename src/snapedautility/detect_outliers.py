def detect_outliers(s):
    """
    Detects outliers in a pandas series
    Returns a threshold value for the lower bound and upper bound of the outliers and Plot a violin plot of the observations
    Parameters
    ----------
    s : pandas.core.series.Series
        Pandas Series for which the outliers need to be found

    Returns
    -------
    List of integers
        Boolean array with same length as the input,
        indices of outlier marked.
    Examples
    --------
    >>> from snapedautility.detect_outliers import detect_outliers 
    >>> s = pd.Series([1,1,2,3,4,5,6,9,10,13,40])
    >>> detect_outliers(s)
    [-8.0 , 20.0]
    """
    return None
