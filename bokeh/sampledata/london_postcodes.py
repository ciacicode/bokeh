'''
This modules exposes geometry data for London Postcodes. It exposes a dictionary 'data' which is
indexed by the two-tuple containing (parent postcode, specific postcode) and has the following dictionary as the
associated value:
    data[(1,1)]['parent']
    data[(1,1)]['postcode']
    data[(1,1)]['lats']
    data[(1,1)]['lons']

Data is powered by MapIt
'''
from __future__ import absolute_import
from os.path import dirname, join
import csv
import pdb


data = {}

with open(join(dirname(__file__),'london_postcodes.csv')) as f:
    reader = csv.DictReader(f)
    for row in reader:
        parent = row['parent']
        postcode = row['name']
        lons = row['lons']
        lats = row['lats']
        pdb.set_trace()
        data[(int(parent_id), int(area_id))] = {'parent': parent,'postcode':name, 'lons': lons, 'lats': lats, }