class Data:
    @classmethod
    def date_str_to_int(cls, date_str):
        date_dic = dict(zip(['day', 'month', 'year'],
                            map(int, date_str.split('-'))))
        print(date_dic)
        validity = cls.date_validation(date_dic)
        print(validity)
        
    @staticmethod
    def date_validation(date_dic):
        boundaries = {'day': [0, 32], 'month': [0, 13], 'year': [-5000, 5000]}

        invalid_levels = list(i for i in date_dic if not (boundaries[i][0] < date_dic[i] < boundaries[i][1]))
        if invalid_levels:
            return 1, 'invalid levels: ' + ', '.join(invalid_levels)
        return 0, 'all valid'


d1 = '11-40-0'
d2 = '03-05-1980'

for d in [d1, d2]:
    print(d)
    Data.date_str_to_int(d)

