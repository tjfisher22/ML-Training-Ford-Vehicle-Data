import pandas as pd
from bagpy import bagreader

def load_data(bag_file):
    b = bagreader(bag_file)
    df = b.message_by_topic('/vehicle_data')
    return df

