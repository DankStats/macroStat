import pandas as pd

from Dir01_EuroStat.Py00_configEuroStat import *

api="demo_pjan"

def runApi(api):

    print("Running EurorStat API script")

    response = requests.get(url=f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{api}",
                            params={"format":"JSON",
                                    "time":"2022",
                                    "lang":"EN",
                                    "geoLevel":"country"},
                                    )
    jsonStr=response.json()

    dataset = pyjstat.from_json_stat(jsonStr)
    df = pd.DataFrame(dataset[0])