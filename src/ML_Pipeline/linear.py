# function to create multitouch attribution model - linear model

def linear_model(dt, conv_col, channel_col, user_id):
    
    import pandas as pd
    from collections import Counter
    #Keeping data of only those users who are getting converted at the end
    pd.options.mode.chained_assignment = None 
    temp=dt.loc[dt[conv_col]==1]
    cookie_index=list(temp[user_id])
    dt['new']=dt[user_id].isin(cookie_index)      
    y=dt['new'].isin([True])
    dt_conv=dt[y]

    temp=pd.DataFrame(dt_conv.groupby(user_id).tail(1))
    x=Counter(dt_conv[user_id])
    temp['click_count']=x.values()      #Click count is total number of channels visited by an user
    temp.set_index(user_id,inplace=True)
    count=Counter(dt_conv[user_id])
    dt_conv['clicks']=dt_conv[user_id].map(count)     #Adding click count to the filtered the data
    dt_conv=dt_conv.assign(click_per=lambda x: round(100/dt_conv['clicks'],2))      #Assigning the weightages in a linear fashion

    #Getting the mean weightage of every channels    
    res_linear=dt_conv.groupby(channel_col, as_index=False)['click_per'].mean()
    sum=res_linear['click_per'].sum()
    res_linear['Weightage(%)']=res_linear.apply(lambda x: round((x['click_per']/sum)*100,2),axis=1)
    res_linear.drop(['click_per'],inplace=True,axis=1)
    res_linear=res_linear.set_index(channel_col)
    res_linear.index.name=None
    return res_linear