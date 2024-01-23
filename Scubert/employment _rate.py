import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")

file_JPN_total_employee = 'DATA/일본 총 취업자수.xlsx'
file_KOR_to_JPN_employee_part1 = 'DATA/한국산업인력공단_해외취업 통계정보_20231231.csv'
file_KOR_to_JPN_employee_part2 = 'DATA/해외취업통계_2008-2012.csv'
file_impression_response = 'DATA/상대국 인상 응답 추이 2013-2023.csv'

impression_response = pd.read_csv(file_impression_response, index_col=0)
JPN_total_employee = pd.read_excel(file_JPN_total_employee, index_col=0, header=[0, 1])
JPN_total_employee = JPN_total_employee.xs('전체', level=1, axis='columns')
JPN_total_employee.index = ['일본']
JPN_total_employee.columns.name = None
KOR_to_JPN_employee_part1 = pd.read_csv(file_KOR_to_JPN_employee_part1, index_col=0, encoding='EUC-KR')

print(JPN_total_employee)
print(JPN_total_employee.index)
print(JPN_total_employee.columns)

print((JPN_total_employee.loc['일본'] * 1000).astype(int))
print(KOR_to_JPN_employee_part1)
print(impression_response)

