import pandas as pd
import numpy as np

# координаты начала заказов
a_x = np.array([3, 3])
a_y = np.array([4, 2])

# координаты конца заказов
b_x = np.array([8, 8])
b_y = np.array([4, 2])

# координаты маршрута водителя
B_x = np.array([11,11])
B_y = np.array([0,0])

# англ. населённый пункт
orders = ['order #1',
          'order #2']

data = pd.DataFrame({'a_x': a_x,
                     'a_y': a_y,
                     'b_x': b_x,
                     'b_y': b_y,
                     'B_x': B_x,
                     'B_y': B_y}, index=orders)

vector_a = data[['a_x', 'a_y']].values
vector_b = data[['b_x', 'b_y']].values
vector_B = data[['B_x', 'B_y']].values
def distance(vector):
  return np.dot(vector,vector)**0.5

d= []
for i in range(len(orders)):
  d.append((distance(vector_a[i])+distance(vector_b[i]-vector_a[i])+distance(vector_B[i]-vector_b[i])).round())
print(d)
print(pd.DataFrame({'distance': d}, index=orders).sort_values('distance'))
