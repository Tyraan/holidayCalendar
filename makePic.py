import os
if os.path.exists('dota2.db'):
    import numpy as np
    import matplotlib.pyplot as plt
    import sqlite3
    conn= sqlite3.connect('dota2.db')
    cur = conn.cursor()
    cur