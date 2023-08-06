# Machine Learning Topics

This repository is my Python and machine learning playground, I use it to save some results of my experiments with
machine learning algorithms.

I hope you find something useful here.. 🙂

## Notes: Getting started

First, get an understanding of the data, [pandas](https://pandas.pydata.org/) is a great tool for this.

**Example**

```python
import pandas as pd

# Import dataset
data_set = pd.read_csv('my_dataset.csv')

# Have a look at the raw entries
print(data_set.values)

# Statistical information about the dataset
data_set.describe()
```

A next step would be to clean the data. This involves removing duplicates and removing entries with missing values,
because these can cause problems when training the model.
