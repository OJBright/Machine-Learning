# Outlier Removal Utility

This script provides a reusable Python function to detect and remove outliers from a dataset using the **Interquartile Range (IQR)** method. It is especially useful for preprocessing clinical or biological datasets prior to downstream analysis or modeling.

## Features
- Removes outliers from one or more numeric columns
- Returns a cleaned DataFrame and a list of detected outliers
- Built with reusability and flexibility in mind

## How to Use

### 1. Import the function
```python
from remove_outliers import remove_outliers
