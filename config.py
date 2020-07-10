mapping = {'VACATION-REQUEST': 0 , 'SALARY-REQUEST': 1, 'SICK-LEAVE-REPORT': 2, 'OTHER': 3}
inv_mapping = {0: 'VACATION-REQUEST', 1: 'SALARY-REQUEST', 2: 'SICK-LEAVE-REPORT', 3: 'OTHER'}
path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
keywords = [['отпуск', 'отдых', 'улетать'], ['зарплата','зарабатывать', 'расчетный', 'лист', 'деньга', 'заплатить'], ['болезнь', 'заболеть', 'больничный', 'врач', 'доктор']]
normalized = True