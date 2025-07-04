import pandas as pd

def remove_outliers(df, cols):
    """
    Removes outliers from specified columns using the IQR method.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame.
        cols (list): List of column names to check for outliers.
        
    Returns:
        df_no_outliers (pd.DataFrame): Cleaned DataFrame with outliers removed.
        outliers (list of dict): List of outlier records.
    """
    df_no_outliers = df.copy()
    outliers = []

    for col in cols:
        Q1 = df_no_outliers[col].quantile(0.25)
        Q3 = df_no_outliers[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        col_outliers = df_no_outliers[
            (df_no_outliers[col] < lower_bound) | (df_no_outliers[col] > upper_bound)
        ]
        outliers.extend(col_outliers.to_dict('records'))

        # Keep only non-outlier rows
        df_no_outliers = df_no_outliers[
            (df_no_outliers[col] >= lower_bound) & (df_no_outliers[col] <= upper_bound)
        ]

    return df_no_outliers, outliers


# Example usage
if __name__ == "__main__":
    # Load your data here
    # Example: df = pd.read_csv("your_file.csv")
    df = pd.DataFrame()  # Replace with your DataFrame
    numeric_columns = []  # Replace with your list of numeric columns

    clean_df, outliers = remove_outliers(df, numeric_columns)

    print("Outliers detected:")
    print(pd.DataFrame(outliers))
