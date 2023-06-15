import sqlite3, pprint
import pandas as pd
import numpy as np


def show_table(save=True):
    conn = sqlite3.connect('artem.sqlite3')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    table = {}

    for I in cur.execute('SELECT indicator FROM T_values GROUP BY indicator;').fetchall():
        indicator = I['indicator']
        table[indicator] = {}
        for R in cur.execute('SELECT resource FROM T_values WHERE indicator=? GROUP BY resource;',
                             [indicator]).fetchall():
            resource = R['resource']
            table[indicator][resource] = {}
            for Y in cur.execute('SELECT year FROM T_values WHERE resource=? GROUP BY year ;', [resource]):
                year = Y['year']
                table[indicator][resource][year] = {}

    for row in cur.execute('SELECT * FROM T_values ORDER BY indicator, resource, year, unit;').fetchall():
        id, indicator, resource, year, unit, value = row
        table[indicator][resource][year][unit] = value

    if save:
        df = pd.DataFrame(
            {(i, r, y): table[i][r][y] for i in table.keys() for r in table[i].keys() for y in table[i][r].keys()},
        )
        df.to_excel('data.xlsx')

    return table


if __name__ == '__main__':
    show_table()




