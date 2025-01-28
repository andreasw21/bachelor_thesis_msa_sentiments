from typing import List

import numpy as np


def calculate_third_quartil(points: List[int]) -> float:
    """
    Calculates the third quartile (Q3) of a list of points.
    """
    if not points:
        return 0.0  # Return 0 for an empty list

    print("Calculating the third quartile (Q3)")
    quartil1 = 0.75
    q1 = np.quantile(points, quartil1)

    return q1
