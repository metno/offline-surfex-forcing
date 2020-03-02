import unittest
import surfex
from datetime import datetime
import numpy as np
import json


class ConverterTest(unittest.TestCase):

    domain = surfex.geo.set_domain(json.load(open("tests/settings/domains.json", "r")), "CONF_PROJ_TEST")
    my_geo = surfex.geo.get_geo_object(domain)

    fileformat = "surfex"
    var = "TG1P1"
    converter = "none"
    config = {
        "surfex": {
            "fcint": 10800,
            "file_inc": 3600,
            "offset": 0
        },
        "TG1P1": {
            "surfex": {
                "converter": {
                    "none": {
                        "varname": "TG1P1",
                        "filepattern": "testdata/PREP_CONF_PROJ.nc"
                    }
                }
            }
        }
    }

    print(var, fileformat)

    defs = config[fileformat]
    converter_conf = config[var][fileformat]["converter"]
    debug = False

    validtime = datetime(year=2020, month=2, day=1, hour=6)
    cache = surfex.Cache(debug, 7200)
    converter = surfex.read.Converter(converter, validtime, defs, converter_conf, fileformat, validtime)
    field = surfex.read.ConvertedInput(my_geo, var, converter).read_time_step(validtime, cache)
    field = np.reshape(field, [my_geo.nlons, my_geo.nlats])

    domain = surfex.geo.set_domain(json.load(open("tests/settings/domains.json", "r")), "CONF_PROJ_TEST")
    my_geo = surfex.geo.get_geo_object(domain)

    fileformat = "surfex"
    var = "FRAC_NATURE"
    converter = "none"
    config = {
        "surfex": {
            "fcint": 10800,
            "file_inc": 3600,
            "offset": 0
        },
        "FRAC_NATURE": {
            "surfex": {
                "converter": {
                    "none": {
                        "varname": "FRAC_NATURE",
                        "filepattern": "testdata/PGD_CONF_PROJ.txt"
                    }
                }
            }
        }
    }

    print(var, fileformat)

    defs = config[fileformat]
    converter_conf = config[var][fileformat]["converter"]
    debug = False

    validtime = datetime(year=2020, month=2, day=1, hour=6)
    cache = surfex.Cache(debug, 7200)
    converter = surfex.read.Converter(converter, validtime, defs, converter_conf, fileformat, validtime)
    field = surfex.read.ConvertedInput(my_geo, var, converter).read_time_step(validtime, cache)
    field = np.reshape(field, [my_geo.nlons, my_geo.nlats])
