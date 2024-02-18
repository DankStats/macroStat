
import requests
import pandas as pd
import pymysql
import json
from pyjstat import pyjstat


apiDict = {"eurostat":{"gasPrisPrivat":"nrg_pc_202",
                       "gasPrisVerksamhet":"nrg_pc_203",
                       "elPrisPrivat":"nrg_pc_204",
                       "elPrisVerksamhet":"nrg_pc_205",
                       "gasKonsumptionPrivat":"nrg_pc_202_v",
                       "gasKOnsumptionVerksamhet":"nrg_pc_203_v",
                       "elKonsumptionPrivat":"nrg_pc_204_v",
                       "elKonsumptionVerksamhet":"nrg_pc_205_v"}}