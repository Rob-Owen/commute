from load_data import load_data
from load_pop_data import load_pop_data
from match_places import match_places
from filter_db import filter_db
from dist_calc import dist_calc

# Execute commands in sequence
load_data()
load_pop_data()
match_places()
filter_db()
dist_calc()