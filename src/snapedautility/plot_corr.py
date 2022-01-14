def plot_corr(df, features=None, width=250, heigh=250):
    """
    Generates the correlation plot for a list of numeric features in a given dataframe

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The input dataframe
    features : list
        List of feature names as string
        len(features) >=2
        None returns plot of all numeric features
    width: int, default = 250
        The width of the plot. Default set to 250
    height: int, default = 250
        The height of the plot. Default set to 250

    Returns
    -------
    `altair plot`
        An interactive altair correlation plot
    Examples
    --------
    >>> from snapedautility.plot_corr import plot_corr
    >>> df = penguins_data
    >>> plot_corr(df, ["Culmen Length (mm)", "Culmen Depth (mm)", 'Species'])
    """
    return None
