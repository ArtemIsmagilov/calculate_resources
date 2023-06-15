from run import create_table
from save_values_to_excel import show_table


def test_0():
    create_table('test0_init_tables.sql')
    assert show_table(save=True) == {'Energy resource': {'Natural gas': {2017: {'Bboe': 1.017186075818, 'Gft3ng': 5739.00988997253, 'Gj': 622451.5715502357, 'Gm3ng': 159.60295419782798, 'Gtce': 0.212385710038, 'Gtoe': 0.14867, 'Gwh': 1729032.0384398673, 'Kboe': 1017186.075818, 'Ktoe': 148670.0, 'MMbtu': 589967.9341463007, 'Mboe': 1017.186075818, 'Mft3ng': 5739009.88997253, 'Mj': 622451571.5502356, 'Mm3ng': 159602.954197828, 'Mtce': 212.38571003799998, 'Mtoe': 148.67, 'Qbtu': 0.0005899679341463007, 'Twh': 1729.032038439867}, 2018: {'Bboe': 1.0217017333820002, 'Gft3ng': 5764.487434382176, 'Gj': 625214.8596192689, 'Gm3ng': 160.31148954302589, 'Gtce': 0.21332856716200002, 'Gtoe': 0.14933000000000002, 'Gwh': 1736707.8381665796, 'Kboe': 1021701.733382, 'Ktoe': 149330.0, 'MMbtu': 592587.0155785773, 'Mboe': 1021.701733382, 'Mft3ng': 5764487.434382176, 'Mj': 625214859.6192689, 'Mm3ng': 160311.48954302588, 'Mtce': 213.328567162, 'Mtoe': 149.33, 'Qbtu': 0.0005925870155785774, 'Twh': 1736.7078381665797}, 2019: {'Bboe': 1.0262858099999999, 'Gft3ng': 5790.3510021919665, 'Gj': 628020.015689348, 'Gm3ng': 161.03076027224188, 'Gtce': 0.21428571, 'Gtoe': 0.15, 'Gwh': 1744499.937889151, 'Kboe': 1026285.8099999999, 'Ktoe': 150000.0, 'MMbtu': 595245.7800628581, 'Mboe': 1026.28581, 'Mft3ng': 5790351.002191966, 'Mj': 628020015.6893479, 'Mm3ng': 161030.76027224187, 'Mtce': 214.28571, 'Mtoe': 150.0, 'Qbtu': 0.0005952457800628582, 'Twh': 1744.4999378891512}, 2020: {'Bboe': 1.030869886618, 'Gft3ng': 5816.214570001757, 'Gj': 630825.1717594271, 'Gm3ng': 161.7500310014579, 'Gtce': 0.21524285283800002, 'Gtoe': 0.15067, 'Gwh': 1752292.0376117225, 'Kboe': 1030869.886618, 'Ktoe': 150670.0, 'MMbtu': 597904.5445471387, 'Mboe': 1030.869886618, 'Mft3ng': 5816214.570001757, 'Mj': 630825171.7594271, 'Mm3ng': 161750.0310014579, 'Mtce': 215.24285283799998, 'Mtoe': 150.67, 'Qbtu': 0.0005979045445471387, 'Twh': 1752.2920376117224}, 2021: {'Bboe': 1.0353855441820001, 'Gft3ng': 5841.692114411402, 'Gj': 633588.4598284604, 'Gm3ng': 162.45856634665577, 'Gtce': 0.21618570996200004, 'Gtoe': 0.15133000000000002, 'Gwh': 1759967.8373384352, 'Kboe': 1035385.544182, 'Ktoe': 151330.0, 'MMbtu': 600523.6259794155, 'Mboe': 1035.385544182, 'Mft3ng': 5841692.114411402, 'Mj': 633588459.8284602, 'Mm3ng': 162458.56634665577, 'Mtce': 216.18570996200003, 'Mtoe': 151.33, 'Qbtu': 0.0006005236259794155, 'Twh': 1759.9678373384347}}}}


def test_1():
    create_table('test1_init_tables.sql')
    assert show_table(save=True) == {'Energy resource': {'Natural gas': {2017: {'Bboe': 1.017186075818, 'Gft3ng': 5739.00988997253, 'Gj': 622451.5715502357, 'Gm3ng': 159.60295419782798, 'Gtce': 0.212385710038, 'Gtoe': 0.14867, 'Gwh': 1729032.0384398673, 'Kboe': 1017186.075818, 'Ktoe': 148670.0, 'MMbtu': 589967.9341463007, 'Mboe': 1017.186075818, 'Mft3ng': 5739009.88997253, 'Mj': 622451571.5502356, 'Mm3ng': 159602.954197828, 'Mtce': 212.38571003799998, 'Mtoe': 148.67, 'Qbtu': 0.0005899679341463007, 'Twh': 1729.032038439867}, 2018: {'Bboe': 1.0217017333820002, 'Gft3ng': 5764.487434382176, 'Gj': 625214.8596192689, 'Gm3ng': 160.31148954302589, 'Gtce': 0.21332856716200002, 'Gtoe': 0.14933000000000002, 'Gwh': 1736707.8381665796, 'Kboe': 1021701.733382, 'Ktoe': 149330.0, 'MMbtu': 592587.0155785773, 'Mboe': 1021.701733382, 'Mft3ng': 5764487.434382176, 'Mj': 625214859.6192689, 'Mm3ng': 160311.48954302588, 'Mtce': 213.328567162, 'Mtoe': 149.33, 'Qbtu': 0.0005925870155785774, 'Twh': 1736.7078381665797}, 2019: {'Bboe': 1.0262858099999999, 'Gft3ng': 5790.3510021919665, 'Gj': 628020.015689348, 'Gm3ng': 161.03076027224188, 'Gtce': 0.21428571, 'Gtoe': 0.15, 'Gwh': 1744499.937889151, 'Kboe': 1026285.8099999999, 'Ktoe': 150000.0, 'MMbtu': 595245.7800628581, 'Mboe': 1026.28581, 'Mft3ng': 5790351.002191966, 'Mj': 628020015.6893479, 'Mm3ng': 161030.76027224187, 'Mtce': 214.28571, 'Mtoe': 150.0, 'Qbtu': 0.0005952457800628582, 'Twh': 1744.4999378891512}, 2020: {'Bboe': 1.030869886618, 'Gft3ng': 5816.214570001757, 'Gj': 630825.1717594271, 'Gm3ng': 161.7500310014579, 'Gtce': 0.21524285283800002, 'Gtoe': 0.15067, 'Gwh': 1752292.0376117225, 'Kboe': 1030869.886618, 'Ktoe': 150670.0, 'MMbtu': 597904.5445471387, 'Mboe': 1030.869886618, 'Mft3ng': 5816214.570001757, 'Mj': 630825171.7594271, 'Mm3ng': 161750.0310014579, 'Mtce': 215.24285283799998, 'Mtoe': 150.67, 'Qbtu': 0.0005979045445471387, 'Twh': 1752.2920376117224}, 2021: {'Bboe': 1.0353855441820001, 'Gft3ng': 5841.692114411402, 'Gj': 633588.4598284604, 'Gm3ng': 162.45856634665577, 'Gtce': 0.21618570996200004, 'Gtoe': 0.15133000000000002, 'Gwh': 1759967.8373384352, 'Kboe': 1035385.544182, 'Ktoe': 151330.0, 'MMbtu': 600523.6259794155, 'Mboe': 1035.385544182, 'Mft3ng': 5841692.114411402, 'Mj': 633588459.8284602, 'Mm3ng': 162458.56634665577, 'Mtce': 216.18570996200003, 'Mtoe': 151.33, 'Qbtu': 0.0006005236259794155, 'Twh': 1759.9678373384347}}}, 'Water': {'Water resource': {2017: {'Bboe': 1.017186075818, 'Gft3ng': 5739.00988997253, 'Gj': 622451.5715502357, 'Gm3ng': 159.60295419782798, 'Gtce': 0.212385710038, 'Gtoe': 0.14867, 'Gwh': 1729032.0384398673, 'Kboe': 1017186.075818, 'Ktoe': 148670.0, 'MMbtu': 589967.9341463007, 'Mboe': 1017.186075818, 'Mft3ng': 5739009.88997253, 'Mj': 622451571.5502356, 'Mm3ng': 159602.954197828, 'Mtce': 212.38571003799998, 'Mtoe': 148.67, 'Qbtu': 0.0005899679341463007, 'Twh': 1729.032038439867}, 2018: {'Bboe': 1.0217017333820002, 'Gft3ng': 5764.487434382176, 'Gj': 625214.8596192689, 'Gm3ng': 160.31148954302589, 'Gtce': 0.21332856716200002, 'Gtoe': 0.14933000000000002, 'Gwh': 1736707.8381665796, 'Kboe': 1021701.733382, 'Ktoe': 149330.0, 'MMbtu': 592587.0155785773, 'Mboe': 1021.701733382, 'Mft3ng': 5764487.434382176, 'Mj': 625214859.6192689, 'Mm3ng': 160311.48954302588, 'Mtce': 213.328567162, 'Mtoe': 149.33, 'Qbtu': 0.0005925870155785774, 'Twh': 1736.7078381665797}, 2019: {'Bboe': 1.0262858099999999, 'Gft3ng': 5790.3510021919665, 'Gj': 628020.015689348, 'Gm3ng': 161.03076027224188, 'Gtce': 0.21428571, 'Gtoe': 0.15, 'Gwh': 1744499.937889151, 'Kboe': 1026285.8099999999, 'Ktoe': 150000.0, 'MMbtu': 595245.7800628581, 'Mboe': 1026.28581, 'Mft3ng': 5790351.002191966, 'Mj': 628020015.6893479, 'Mm3ng': 161030.76027224187, 'Mtce': 214.28571, 'Mtoe': 150.0, 'Qbtu': 0.0005952457800628582, 'Twh': 1744.4999378891512}, 2020: {'Bboe': 1.030869886618, 'Gft3ng': 5816.214570001757, 'Gj': 630825.1717594271, 'Gm3ng': 161.7500310014579, 'Gtce': 0.21524285283800002, 'Gtoe': 0.15067, 'Gwh': 1752292.0376117225, 'Kboe': 1030869.886618, 'Ktoe': 150670.0, 'MMbtu': 597904.5445471387, 'Mboe': 1030.869886618, 'Mft3ng': 5816214.570001757, 'Mj': 630825171.7594271, 'Mm3ng': 161750.0310014579, 'Mtce': 215.24285283799998, 'Mtoe': 150.67, 'Qbtu': 0.0005979045445471387, 'Twh': 1752.2920376117224}, 2021: {'Bboe': 1.0353855441820001, 'Gft3ng': 5841.692114411402, 'Gj': 633588.4598284604, 'Gm3ng': 162.45856634665577, 'Gtce': 0.21618570996200004, 'Gtoe': 0.15133000000000002, 'Gwh': 1759967.8373384352, 'Kboe': 1035385.544182, 'Ktoe': 151330.0, 'MMbtu': 600523.6259794155, 'Mboe': 1035.385544182, 'Mft3ng': 5841692.114411402, 'Mj': 633588459.8284602, 'Mm3ng': 162458.56634665577, 'Mtce': 216.18570996200003, 'Mtoe': 151.33, 'Qbtu': 0.0006005236259794155, 'Twh': 1759.9678373384347}}}}


def test_2():
    create_table('test2_init_tables.sql')
    assert show_table(save=True) == {'Energy resource': {'Natural gas': {2017: {'Bboe': 1.017186075818, 'Gft3ng': 5739.00988997253, 'Gj': 622451.5715502357, 'Gm3ng': 159.60295419782798, 'Gtce': 0.212385710038, 'Gtoe': 0.14867, 'Gwh': 1729032.0384398673, 'Kboe': 1017186.075818, 'Ktoe': 148670.0, 'MMbtu': 589967.9341463007, 'Mboe': 1017.186075818, 'Mft3ng': 5739009.88997253, 'Mj': 622451571.5502356, 'Mm3ng': 159602.954197828, 'Mtce': 212.38571003799998, 'Mtoe': 148.67, 'Qbtu': 0.0005899679341463007, 'Twh': 1729.032038439867}, 2018: {'Bboe': 1.0217017333820002, 'Gft3ng': 5764.487434382176, 'Gj': 625214.8596192689, 'Gm3ng': 160.31148954302589, 'Gtce': 0.21332856716200002, 'Gtoe': 0.14933000000000002, 'Gwh': 1736707.8381665796, 'Kboe': 1021701.733382, 'Ktoe': 149330.0, 'MMbtu': 592587.0155785773, 'Mboe': 1021.701733382, 'Mft3ng': 5764487.434382176, 'Mj': 625214859.6192689, 'Mm3ng': 160311.48954302588, 'Mtce': 213.328567162, 'Mtoe': 149.33, 'Qbtu': 0.0005925870155785774, 'Twh': 1736.7078381665797}, 2019: {'Bboe': 1.0262858099999999, 'Gft3ng': 5790.3510021919665, 'Gj': 628020.015689348, 'Gm3ng': 161.03076027224188, 'Gtce': 0.21428571, 'Gtoe': 0.15, 'Gwh': 1744499.937889151, 'Kboe': 1026285.8099999999, 'Ktoe': 150000.0, 'MMbtu': 595245.7800628581, 'Mboe': 1026.28581, 'Mft3ng': 5790351.002191966, 'Mj': 628020015.6893479, 'Mm3ng': 161030.76027224187, 'Mtce': 214.28571, 'Mtoe': 150.0, 'Qbtu': 0.0005952457800628582, 'Twh': 1744.4999378891512}, 2020: {'Bboe': 1.030869886618, 'Gft3ng': 5816.214570001757, 'Gj': 630825.1717594271, 'Gm3ng': 161.7500310014579, 'Gtce': 0.21524285283800002, 'Gtoe': 0.15067, 'Gwh': 1752292.0376117225, 'Kboe': 1030869.886618, 'Ktoe': 150670.0, 'MMbtu': 597904.5445471387, 'Mboe': 1030.869886618, 'Mft3ng': 5816214.570001757, 'Mj': 630825171.7594271, 'Mm3ng': 161750.0310014579, 'Mtce': 215.24285283799998, 'Mtoe': 150.67, 'Qbtu': 0.0005979045445471387, 'Twh': 1752.2920376117224}, 2021: {'Bboe': 1.0353855441820001, 'Gft3ng': 5841.692114411402, 'Gj': 633588.4598284604, 'Gm3ng': 162.45856634665577, 'Gtce': 0.21618570996200004, 'Gtoe': 0.15133000000000002, 'Gwh': 1759967.8373384352, 'Kboe': 1035385.544182, 'Ktoe': 151330.0, 'MMbtu': 600523.6259794155, 'Mboe': 1035.385544182, 'Mft3ng': 5841692.114411402, 'Mj': 633588459.8284602, 'Mm3ng': 162458.56634665577, 'Mtce': 216.18570996200003, 'Mtoe': 151.33, 'Qbtu': 0.0006005236259794155, 'Twh': 1759.9678373384347}}}, 'Water': {'Hot water': {2017: {'Bboe': 1.017186075818, 'Gft3ng': 5739.00988997253, 'Gj': 622451.5715502357, 'Gm3ng': 159.60295419782798, 'Gtce': 0.212385710038, 'Gtoe': 0.14867, 'Gwh': 1729032.0384398673, 'Kboe': 1017186.075818, 'Ktoe': 148670.0, 'MMbtu': 589967.9341463007, 'Mboe': 1017.186075818, 'Mft3ng': 5739009.88997253, 'Mj': 622451571.5502356, 'Mm3ng': 159602.954197828, 'Mtce': 212.38571003799998, 'Mtoe': 148.67, 'Qbtu': 0.0005899679341463007, 'Twh': 1729.032038439867}, 2018: {'Bboe': 1.0217017333820002, 'Gft3ng': 5764.487434382176, 'Gj': 625214.8596192689, 'Gm3ng': 160.31148954302589, 'Gtce': 0.21332856716200002, 'Gtoe': 0.14933000000000002, 'Gwh': 1736707.8381665796, 'Kboe': 1021701.733382, 'Ktoe': 149330.0, 'MMbtu': 592587.0155785773, 'Mboe': 1021.701733382, 'Mft3ng': 5764487.434382176, 'Mj': 625214859.6192689, 'Mm3ng': 160311.48954302588, 'Mtce': 213.328567162, 'Mtoe': 149.33, 'Qbtu': 0.0005925870155785774, 'Twh': 1736.7078381665797}, 2019: {'Bboe': 1.0262858099999999, 'Gft3ng': 5790.3510021919665, 'Gj': 628020.015689348, 'Gm3ng': 161.03076027224188, 'Gtce': 0.21428571, 'Gtoe': 0.15, 'Gwh': 1744499.937889151, 'Kboe': 1026285.8099999999, 'Ktoe': 150000.0, 'MMbtu': 595245.7800628581, 'Mboe': 1026.28581, 'Mft3ng': 5790351.002191966, 'Mj': 628020015.6893479, 'Mm3ng': 161030.76027224187, 'Mtce': 214.28571, 'Mtoe': 150.0, 'Qbtu': 0.0005952457800628582, 'Twh': 1744.4999378891512}, 2020: {'Bboe': 1.030869886618, 'Gft3ng': 5816.214570001757, 'Gj': 630825.1717594271, 'Gm3ng': 161.7500310014579, 'Gtce': 0.21524285283800002, 'Gtoe': 0.15067, 'Gwh': 1752292.0376117225, 'Kboe': 1030869.886618, 'Ktoe': 150670.0, 'MMbtu': 597904.5445471387, 'Mboe': 1030.869886618, 'Mft3ng': 5816214.570001757, 'Mj': 630825171.7594271, 'Mm3ng': 161750.0310014579, 'Mtce': 215.24285283799998, 'Mtoe': 150.67, 'Qbtu': 0.0005979045445471387, 'Twh': 1752.2920376117224}, 2021: {'Bboe': 1.0353855441820001, 'Gft3ng': 5841.692114411402, 'Gj': 633588.4598284604, 'Gm3ng': 162.45856634665577, 'Gtce': 0.21618570996200004, 'Gtoe': 0.15133000000000002, 'Gwh': 1759967.8373384352, 'Kboe': 1035385.544182, 'Ktoe': 151330.0, 'MMbtu': 600523.6259794155, 'Mboe': 1035.385544182, 'Mft3ng': 5841692.114411402, 'Mj': 633588459.8284602, 'Mm3ng': 162458.56634665577, 'Mtce': 216.18570996200003, 'Mtoe': 151.33, 'Qbtu': 0.0006005236259794155, 'Twh': 1759.9678373384347}}, 'Water resource': {2017: {'Bboe': 1.017186075818, 'Gft3ng': 5739.00988997253, 'Gj': 622451.5715502357, 'Gm3ng': 159.60295419782798, 'Gtce': 0.212385710038, 'Gtoe': 0.14867, 'Gwh': 1729032.0384398673, 'Kboe': 1017186.075818, 'Ktoe': 148670.0, 'MMbtu': 589967.9341463007, 'Mboe': 1017.186075818, 'Mft3ng': 5739009.88997253, 'Mj': 622451571.5502356, 'Mm3ng': 159602.954197828, 'Mtce': 212.38571003799998, 'Mtoe': 148.67, 'Qbtu': 0.0005899679341463007, 'Twh': 1729.032038439867}, 2018: {'Bboe': 1.0217017333820002, 'Gft3ng': 5764.487434382176, 'Gj': 625214.8596192689, 'Gm3ng': 160.31148954302589, 'Gtce': 0.21332856716200002, 'Gtoe': 0.14933000000000002, 'Gwh': 1736707.8381665796, 'Kboe': 1021701.733382, 'Ktoe': 149330.0, 'MMbtu': 592587.0155785773, 'Mboe': 1021.701733382, 'Mft3ng': 5764487.434382176, 'Mj': 625214859.6192689, 'Mm3ng': 160311.48954302588, 'Mtce': 213.328567162, 'Mtoe': 149.33, 'Qbtu': 0.0005925870155785774, 'Twh': 1736.7078381665797}, 2019: {'Bboe': 1.0262858099999999, 'Gft3ng': 5790.3510021919665, 'Gj': 628020.015689348, 'Gm3ng': 161.03076027224188, 'Gtce': 0.21428571, 'Gtoe': 0.15, 'Gwh': 1744499.937889151, 'Kboe': 1026285.8099999999, 'Ktoe': 150000.0, 'MMbtu': 595245.7800628581, 'Mboe': 1026.28581, 'Mft3ng': 5790351.002191966, 'Mj': 628020015.6893479, 'Mm3ng': 161030.76027224187, 'Mtce': 214.28571, 'Mtoe': 150.0, 'Qbtu': 0.0005952457800628582, 'Twh': 1744.4999378891512}, 2020: {'Bboe': 1.030869886618, 'Gft3ng': 5816.214570001757, 'Gj': 630825.1717594271, 'Gm3ng': 161.7500310014579, 'Gtce': 0.21524285283800002, 'Gtoe': 0.15067, 'Gwh': 1752292.0376117225, 'Kboe': 1030869.886618, 'Ktoe': 150670.0, 'MMbtu': 597904.5445471387, 'Mboe': 1030.869886618, 'Mft3ng': 5816214.570001757, 'Mj': 630825171.7594271, 'Mm3ng': 161750.0310014579, 'Mtce': 215.24285283799998, 'Mtoe': 150.67, 'Qbtu': 0.0005979045445471387, 'Twh': 1752.2920376117224}, 2021: {'Bboe': 1.0353855441820001, 'Gft3ng': 5841.692114411402, 'Gj': 633588.4598284604, 'Gm3ng': 162.45856634665577, 'Gtce': 0.21618570996200004, 'Gtoe': 0.15133000000000002, 'Gwh': 1759967.8373384352, 'Kboe': 1035385.544182, 'Ktoe': 151330.0, 'MMbtu': 600523.6259794155, 'Mboe': 1035.385544182, 'Mft3ng': 5841692.114411402, 'Mj': 633588459.8284602, 'Mm3ng': 162458.56634665577, 'Mtce': 216.18570996200003, 'Mtoe': 151.33, 'Qbtu': 0.0006005236259794155, 'Twh': 1759.9678373384347}}}}

