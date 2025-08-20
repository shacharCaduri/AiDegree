import pandas as pd
import numpy as np
import datetime
from typing import Union, Optional


class ExPrinter:
    _SYMBOL = "="
    _COUNT = 10
    _TYPES = {'headline'}


    def headline(self, head_text: str) -> str:
        return self._SYMBOL * self._COUNT  + head_text + self._SYMBOL * self._COUNT 

    def print(self, type: str, text: Optional[str] = None) -> None:
        if type in self._TYPES:
            if type == 'headline':
                print(self.headline(f' {'DefaultHeadline' if not text else text} '))


def creating_dataset() -> dict[str, Union[str, int, float, datetime.datetime]]:
    return {
        "Cars": ["BMW", "Volvo", "Mazda"],
        "LicensePlates": [1342455, 4433455, 8455874],
    }


def creating_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        creating_dataset()
    )


def creating_series() -> pd.Series:
    # 'object' stores pandas objects, more flexible but less memory efficient
    # 'string' stores pandas optimized string type, better for string operations and memory usage when using strings
    return pd.Series(["Regular", "Lithium-ion"], dtype='string', name='BatteryType')


def example_series_index() -> pd.Series:
    return pd.Series(['Stam', 'Argument'], index=['Head1', 'Head2'], dtype='string')


def example_index_dict() -> pd.Series:
    return pd.Series(
        {'day1': 200, 'day2': 100, 'day3': 300}, index=['day1', 'day2']
    )

def main():
    printer = ExPrinter()
    printer.print('headline', " DataFrame ")
    print(creating_dataframe())
    printer.print('headline', " Series ")
    print(creating_series())
    print(example_series_index())
    print(example_index_dict())

if __name__ == "__main__":
    main()