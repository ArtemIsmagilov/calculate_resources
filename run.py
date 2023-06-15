import sqlite3
import numpy as np


def multiplication(u, value):
    id, name, u, e, base_u = T_multiplication[m_multiplication_calc_units == u][0]
    # calc_unit -> base_unit
    value = value * 10 ** (6 + int(e))
    return base_u, value


def convertation(res, value):
    if res == 'toe':
        return res, value
    else:
        id, name, b_u, k, res_u = T_convertation[m_convertation_res_units == res][0]
        value = float(value) * float(k)
        return convertation(b_u, value)


def get_result(u, values):
    base_u, v = multiplication(u, float(values[5]))
    b, v = convertation(base_u, v)
    return v


def transaction(u, res):
    id, i, r, y, *_ = row
    cur.execute('INSERT INTO T_values (indicator, resource, year, unit, value) VALUES (?, ?, ?, ?, ?);',
                [i, r, int(y), u, float(res)])


def create_table(path_to_sql='init_tables.sql'):
    global conn, cur, row, T_convertation, T_multiplication, m_convertation_res_units, m_multiplication_calc_units
    conn = sqlite3.connect('artem.sqlite3')
    cur = conn.cursor()
    with conn:
        cur.executescript(open(path_to_sql).read())
    # conn.row_factory = sqlite3.Row
    T_values = np.array(cur.execute('SELECT * FROM T_values;').fetchall())
    T_multiplication = np.array(cur.execute('SELECT * FROM T_multiplication;').fetchall())
    T_convertation = np.array(cur.execute('SELECT * FROM T_convertation;').fetchall())

    m_multiplication_calc_units = T_multiplication[:, 2]
    m_convertation_res_units = T_convertation[:, 4]

    with conn:
        for row in T_values:
            for unit in m_multiplication_calc_units:
                res = get_result(unit, row)
                transaction(unit, res)


if __name__ == '__main__':
    create_table()
