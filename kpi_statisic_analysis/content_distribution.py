
import numpy as np
import matplotlib.pyplot as plt

def radar_map(df):
    '''
    内容类型分布——雷达图 http_flow.contenttype
    '''
    # =======自己设置开始============
    # 标签
    # labels = np.array(['艺术A', '调研I', '实际R', '常规C', '企业E', '社会S'])
    labels=list(df['name'])

    # 数据个数
    max_num=2000
    step=200
    dataLenth = len(labels)
    # 数据
    # data = np.array([1, 4, 3, 6, 4, 8])
    data=list(df['count'])
    # ========自己设置结束============

    angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)
    data = np.concatenate((data, [data[0]]))  # 闭合
    # print(data)
    angles = np.concatenate((angles, [angles[0]]))  # 闭合
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)  # polar参数！！
    ax.plot(angles, data, 'bo-', linewidth=2)  # 画线
    ax.fill(angles, data, facecolor='r', alpha=0.25)  # 填充
    # ax.set_rgrids(np.arange(0, max_num, step))
    ax.set_rlabel_position(180)
    ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
    ax.set_title("content_type radar_map", va='bottom', fontproperties="SimHei")
    # 极径范围
    ax.set_rlim(0, max_num)
    ax.grid(True)
    plt.show()
import pandas as pd
def content_type(file_path):
    '''
    根据查询文件，获取内容类型分布
    :param file_path:
    :return:df
    '''
    rt_df=pd.DataFrame()
    df=pd.read_csv(file_path,usecols=['http_flow.contenttype'])
    df['http_flow.contenttype']=df['http_flow.contenttype'].apply(lambda a:str(a).split('/')[0])
    for name,group in df.groupby(['http_flow.contenttype']):
        # print(int(group.count()))
        rt_df=rt_df.append({'name':name,'count':int(group.count())},ignore_index=True)
        # print(rt_df)
    rt_df[['count']]=rt_df[['count']].astype(int)
    print(rt_df)
    return rt_df
    # print(df.describe())
rt_df=content_type('../data/query_result.csv')
radar_map(rt_df)