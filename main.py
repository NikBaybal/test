import pandas as pd
import numpy as np

def distance(vector):
  return np.dot(vector,vector)**0.5
def best(driver_route,orders):
    orders_num=[]
    a_x = []
    a_y = []
    b_x = []
    b_y = []
    B_x = []
    B_y = []
    for i in range(len(orders)):
        orders_num.append(f'order #{i}')
        a_x.append(orders[i][0])
        a_y.append(orders[i][1])
        b_x.append(orders[i][2])
        b_y.append(orders[i][3])
        B_x.append(driver_route[0])
        B_y.append(driver_route[1])

    data = pd.DataFrame({'a_x': a_x,
                         'a_y': a_y,
                         'b_x': b_x,
                         'b_y': b_y,
                         'B_x': B_x,
                         'B_y': B_y}, index=orders_num)

    vector_a = data[['a_x', 'a_y']].values
    vector_b = data[['b_x', 'b_y']].values
    vector_B = data[['B_x', 'B_y']].values

    d= []
    for i in range(len(orders)):
      d.append((distance(vector_a[i])+distance(vector_b[i]-vector_a[i])+distance(vector_B[i]-vector_b[i])).round())
    print(pd.DataFrame({'distance': d}, index=orders).sort_values('distance'))



"""
# координаты начала заказов
a_x = np.array([3, 3])
a_y = np.array([4, 2])

b_x = np.array([8, 8])
b_y = np.array([4, 2])

# координаты маршрута водителя
B_x = np.array([11, 11])
B_y = np.array([0, 0])
driver_route=[11,0]
orders=[[3,4,8,4],[3,2,8,2]]
orders_num=[]
columns_name=['a_x','a_y','b_x','b_y']
for i in range(len(orders)):
    orders_num.append(f'order #{i}')
data = pd.DataFrame(orders, columns=columns_name,index=orders_num)
print(data)
"""
driver_route=[11,0]
orders=[[3,4,8,4],[3,2,8,2]]
best(driver_route,orders)