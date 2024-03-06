import pandas as pd
from .models import Spot

def submissions_to_dataframe():
    data = Spot.objects.all().values()  # Filter based on your criteria, e.g., status='pending'
    return pd.DataFrame(list(data))
