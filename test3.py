import pandas as pd

entity = ['女装', '男装']

# entity = ['女装', '男装', '运动', '手表眼镜', '鞋包饰品', 
#         '粮油美食', '日化洗护', '母婴玩具', '办公影音', 
#         '家用电器', '手机通信', '家装建材', '家具家私',
#         '种子', '肥料', '饲料', '机具', '农膜', '农药',
#         '新车', '摩托', '电动', '汽车精品', '汽摩配件']

# nrows 控制读取文件的行数
data = pd.read_csv('社团划分.csv', nrows=10)

# 第一种，根据文件里面的查找entity
# entity_in = data[(data['Label'].isin(entity))].drop_duplicates(['modularity_class'])['modularity_class']
# entity_in = entity_in.values.tolist()

# entity_out = data[(data['modularity_class'].isin(entity_in))]

# print (entity_in)
# print (entity_out)

# filter_data = pd.DataFrame(columns = ['Id', 'Label', 'timeset', 'modularity_class'])
filter_data = set()
# 第二种，根据entity查找文件，筛选出Id包含村淘实体的
# modularity_class_set去除重复
for e in entity:
    b = data['Id'].str.contains(e)
    c = data[b]
    # print (c['modularity_class'])
    # print (type(c['modularity_class'].values[0]))

    # filter_data = filter_data.append(data[b], ignore_index=True, sort=False)
    # print (filter_data)
    filter_data.add(c['modularity_class'].values[0])
    # print (modularity_class_set)

print (filter_data)
# print (type(filter_data))

# 根据上述筛选出的modularity_class，从社团划分.csv文件中提取所有和提取的modularity_class的实体
# filter_data = filter_data['modularity_class'].values.tolist()
filter_data2 = data[data['modularity_class'].isin(filter_data)]
print (filter_data2)

# 再根据筛选出的实体，输出通用图谱中的信息
filter_data2 = filter_data2['Id'].values.tolist()
data2 = pd.read_csv('entity4.csv', nrows=1000)
filter_data3 = data2[data2['实体'].isin(filter_data2)]
print (filter_data3)

# 输出
filename = 'output.csv'
filter_data3.to_csv(filename, encoding='utf-8-sig', index=False)



