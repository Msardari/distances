from itertools import combinations
from typing import Tuple, Any

import numpy as np
import pandas as pd
from geopy.distance import great_circle
from pandas import DataFrame


class Engine:

    def __init__(self, options):
        self.__data_frame = None
        self.__distances = None
        self.options = options

        self.initial_data()
        self.fill_distances()

    def initial_data(self):
        if self.options.known.number > 1:
            number = self.options.known.number
            lat, lon = np.random.randn(2, number)
            data = {
                'Name': [f'RandPlace{i}' for i in range(number)],
                'Latitude': lat,
                'Longitude': lon,
            }
            data_frame = pd.DataFrame(data)
        else:
            data_frame = pd.read_csv('data/places.csv')

        self.__data_frame = data_frame

    def fill_distances(self):
        distances = pd.DataFrame(columns=['place1', 'place2', 'distance'])
        for index in list(combinations(self.__data_frame.index, 2)):
            comb = self.__data_frame.loc[index, :]
            same, distance = self.calculate_distance(comb)
            if not same:
                data = {
                    'place1': comb.Name.iloc[0],
                    'place2': comb.Name.iloc[1],
                    'distance': distance,
                }
                distances = pd.concat([distances, pd.DataFrame(data, index=[0])], ignore_index=True)
        self.__distances = distances

    @staticmethod
    def calculate_distance(data: DataFrame) -> tuple[bool, float]:
        start = (data.Latitude.iloc[0], data.Longitude.iloc[0])
        end = (data.Latitude.iloc[1], data.Longitude.iloc[1])
        if start == end:
            return True, 0
        return False, great_circle(start, end).km

    def get_distances(self) -> DataFrame:
        return self.__distances.sort_values('distance')

    def avg(self) -> float:
        return self.__distances['distance'].mean()

    def closest_pair(self, distance: float) -> DataFrame:
        return self.__distances.iloc[(self.__distances['distance']-distance).abs().argsort()[:1]]
