"""
Nose tests for mypymongo.py

Write your tests HERE AND ONLY HERE.
"""

from mypymongo import brevet_insert, brevet_find
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_brevet1():
    brevet_dist_km =  "200"
    begin_date = "2021-01-01T00:00"
    items = [
        {"close": "2021-01-01T03:30", "km": "50", "location": "a", "miles": "31.068550", "open": "2021-01-01T01:28"},
        {"close": "2021-01-01T06:40", "km": "100", "location": "b", "miles": "62.137100", "open": "2021-01-01T02:56"},
        {"close": "2021-01-01T10:00", "km": "150", "location": "c", "miles": "93.205650", "open": "2021-01-01T04:25"},
        {"close": "2021-01-01T13:30", "km": "200", "location": "d", "miles": "124.274200", "open": "2021-01-01T05:53"},
        ]
    brevet_insert(brevet_dist_km, begin_date, items)
    rtn_brevet_dist_km, rtn_begin_date, rtn_items = brevet_find()
    assert rtn_brevet_dist_km == brevet_dist_km
    assert rtn_begin_date == rtn_begin_date
    assert rtn_items == items

def test_brevet2():
    #test empty location brevets
    brevet_dist_km =  "300"
    begin_date = "2021-01-01T00:00"
    items = [
        {"close": "2021-01-01T06:40", "km": "100", "location": "", "miles": "62.137100", "open": "2021-01-01T02:56"},
        {"close": "2021-01-01T13:20", "km": "200", "location": "", "miles": "124.274200", "open": "2021-01-01T05:53"},
        {"close": "2021-01-01T20:00", "km": "300", "location": "", "miles": "186.411300", "open": "2021-01-01T09:00"},
        ]
    brevet_insert(brevet_dist_km, begin_date, items)
    rtn_brevet_dist_km, rtn_begin_date, rtn_items = brevet_find()
    assert rtn_brevet_dist_km == brevet_dist_km
    assert rtn_begin_date == rtn_begin_date
    assert rtn_items == items


