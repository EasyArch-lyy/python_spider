import csv
'''
读写csv文件
'''
# 读csv文件
with open('/home/lyy/桌面/kk.csv',encoding='utf-8')as f:
    reader=csv.DictReader(f)
    # for循环有序字典row
    for row in reader:
        print(row)
        # 获取具体参数
        kind=row['kind']
        print(kind)
# 写csv文件
data=[{'name':'kingname','age':24,'salary':99999},
      {'name':'meiji','age':20,'salary':100},
      {'name':'kingname','age':30,'salary':'N/A'}]
with open('../new.csv', 'w', encoding='utf-8')as d:
    writer=csv.DictWriter(d,fieldnames=['name','age','salary'])
    writer.writeheader()
    writer.writerows(data)
    writer.writerow({'name':'超人','age':999,'salary':0})

if __name__ == '__main__':
    data = [{'name': 'kingname', 'age': 24, 'salary': 99999},
            {'name': 'meiji', 'age': 20, 'salary': 100},
            {'name': 'kingname', 'age': 30, 'salary': 'N/A'}]
    with open('../new.csv', 'w', encoding='utf-8')as d:
        writer = csv.DictWriter(d, fieldnames=['name', 'age', 'salary'])
        writer.writeheader()
        writer.writerows(data)
        writer.writerow({'name': '超人', 'age': 999, 'salary': 0})