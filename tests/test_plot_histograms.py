import pandas as pd
import altair as alt
from snapedautility.plot_histograms import plot_histograms
from palmerpenguins import load_penguins
from pytest import raises, fixture


@fixture
def df():
    df = load_penguins()
    return df

@fixture
def histograms():
    df = load_penguins()
    features = df.columns.to_list()
    histograms = plot_histograms(df=df, features=features, facet_columns=2)
    print(histograms)
    return histograms

def test_invalid_input_df(df):
    # None type
    with raises(ValueError):
        plot_histograms(
            None,
            ["species", "bill_length_mm"],
            facet_columns=2,
            width=100,
            height=100
        )
    
    # Pandas DataFrame with unmatching columns
    df = {'col1': [1, 2], 'col2': [3, 4]}
    invalid_df = pd.DataFrame(data=df)
    with raises(ValueError):
        plot_histograms(
            invalid_df,
            ["species", "bill_length_mm"],
            facet_columns=2,
            width=100,
            height=100
        )

def test_invalid_features(df):
    # Empty list of features
    with raises(ValueError):
        plot_histograms(
            df,
            [],
            facet_columns=2,
            width=100,
            height=100
        )

    # Invalid list of features
    with raises(ValueError):
        plot_histograms(
            df,
            ["SADJASDASDAS", "DASCZXCXVCHWERFW4!@#$!@$"],
            facet_columns=2,
            width=100,
            height=100
        )

def test_invalid_plot_size(df):
    # Pass width of negative integer as a parameter
    with raises(ValueError):
        plot_histograms(
            df,
            ["species", "bill_length_mm"],
            facet_columns=2,
            width=-5,
            height=100
        )
    
    # Pass height of 0 as a parameter
    with raises(ValueError):
        plot_histograms(
            df,
            ["species", "bill_length_mm"],
            facet_columns=2,
            width=100,
            height=0
        )

    # Pass width of string type
    with raises(ValueError):
        plot_histograms(
            df,
            ["species", "bill_length_mm"],
            facet_columns=2,
            width="100",
            height=100
        )

    # Pass width and height of type list
    with raises(ValueError):
        plot_histograms(
            df,
            ["species", "bill_length_mm"],
            facet_columns=2,
            width=[100],
            height=[100]
        )

def test_data_used_for_histograms(histograms, df):
    """
    Check the data used for histograms are matching
    """
    data = list(histograms.to_dict()["datasets"].values())
    assert df.equals(pd.DataFrame(data[0]))
