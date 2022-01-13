def plot_histograms(df, features, width=125, heigh=125):
    """
    Plots histogram given numeric features of the input dataframe, and
    plots bar charts for categorical features of the input dataframe

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        Input dataframe
    features : list
        List of feature names as string
    width: int
        The width of sub-plot for each feature. Default set to 125
    height: int
        The height of sub-plot for each feature Default set to 125

    Returns
    -------
    `altair plot`
        Returns altair plot

    Examples
    --------
    >>> from snapedautility.plot_histograms import plot_histograms
    >>> df = penguins_data
    >>> plot_histograms(df, ["Culmen Length (mm)", "Culmen Depth (mm)", 'Species'], 100, 100)
    """
    return None