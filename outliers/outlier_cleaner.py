#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    num_outliers = int(len(ages) * 1.0 / 100 * 10)

    residual_errors = [(predictions[i][0] - net_worths[i][0]) for i in range(len(ages))]

    outliers_errors = sorted(residual_errors, reverse=True)[:num_outliers]

    cleaned_data = [(ages[i][0], net_worths[i][0], residual_errors[i]) for i in range(len(ages)) if residual_errors[i] not in outliers_errors]

    return cleaned_data

