from snapedautility.detect_outliers import detect_outliers
import pandas as pd
import pytest

@pytest.fixture
def simple_series():
    return pd.Series([1, 2, 1, 2, 1, 1000])

@pytest.fixture
def empty_series():
    return (
        pd.Series([], dtype="float64")
    )

def test_detect_outliers_simple(simple_series):
    """Test detect outliers drawn by detect_outliers function."""
    s = simple_series
    [lower_bound, upper_bound], plt = detect_outliers(s)

    # Test the threshold values
    assert lower_bound == -0.5, "Lower bound of simple series should equal to -0.5"
    assert upper_bound == 3.5, "Upper bound of simple series should equal to 3.5"
    # Test the plot
    assert "altair" in str(type(plt)), "Plot should be an altair chart"
    assert plt.to_dict()["mark"] == "boxplot", "Plot should be a boxplot"
    assert plt.to_dict()["height"] == 250, "Plot height should be 250"
    assert plt.to_dict()["width"] == 250, "Plot width should be 250"

def test_incorrect_simple_input():
    """Test detect outliers with incorrect input."""
    with pytest.raises(TypeError):
        detect_outliers(1)
    with pytest.raises(TypeError):
        detect_outliers(False)
    with pytest.raises(TypeError):
        detect_outliers("abcdfefg")
    with pytest.raises(TypeError):
        detect_outliers(4.5)
    with pytest.raises(TypeError):
        detect_outliers(None)

def test_incorrect_input_plt(simple_series):
    s = simple_series
    """Test detect outliers with incorrect input."""
    with pytest.raises(TypeError):
        detect_outliers(s, height=[])
    with pytest.raises(TypeError):
        detect_outliers(s, height=365, width= "abc")
    with pytest.raises(TypeError):
        detect_outliers(s, height=250, width= None)

def test_incorrect_empty_input(empty_series):
    """Test detect outliers with incorrect input."""
    with pytest.raises(ValueError):
        detect_outliers(empty_series)
    with pytest.raises(ValueError):
        detect_outliers(empty_series, "abc", False)
    with pytest.raises(ValueError):
        detect_outliers(empty_series, 250, 250)
