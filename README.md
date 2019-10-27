# git_qing
（按领域划分）计划：
  第一步：提取通用图谱的一部分，利用networkx将其转化为gephi可读文件(gexf)，利用gephi的社团划分，导出数据文件（csv）
  第二步：将村淘中的部分实体提取出来，在 社团分割.csv 中查找相关的实体，再利用modularity_class导出与上述有关的实体
  
该部分实现了第二步
