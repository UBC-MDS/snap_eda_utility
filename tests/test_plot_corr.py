from snapedautility.plot_corr import plot_corr
import pandas as pd
import numpy as np
from pytest import raises
import altair


def df():
    
    df = pd.DataFrame({"a":np.random.normal(100, 30, 5),
                  "b":np.random.normal(8, 5, size=5),
                  "c":np.random.randint(100, size=5),
                 "char":["A","B", "C", "D", "E"]})

    return df

def test_corr_plot():
    
    """
    Test function to check the output of corr_plot function.
    """

    # Make a plot with features=None
    plot = plot_corr(df(), features=None)

    # Make a plot with input features
    plot_f = plot_corr(df(), features=["a","b"])

    # Tests whether output is of Altair object
    assert isinstance(
        plot, altair.vegalite.v4.api.Chart
    ), "Altair Chart object should be returned."

    # Tests whether plot mark is rect
    assert (
        plot.to_dict()["mark"] == "rect"
    ), "Mark should be of type 'rect'."

    # Tests whether a not dataframe input raises TypeError
    with raises(TypeError):
        plot_corr(np.array([1, 2, 3, 4, 5]), ["a","b","c"])

    # Tests whether a not list features raises TypeError
    with raises(TypeError):
        plot_corr(df(), "a")

    # Tests whether a list of a single feature raises ValueError
    with raises(ValueError):
        plot_corr(df(), ["a"])

def test_corr_plot_subsetting_errors():
    with raises(ValueError):
        plot_corr(df().loc[:, ["a"]])

    with raises(ValueError):
        plot_corr(
            df().loc[:, ["a", "char"]],
            features=["a", "char"],
        )
