# function to create multitouch attribution model - position decay model

def pos_decay_model(dt, conv_col, channel_col, user_id):

    import pandas as pd
    from collections import Counter

    def calc_attribution(click_pos,total_clicks):
        rel_pos = total_clicks - click_pos
        attribution = pow(2, -(rel_pos))       #Assigning weightage to channels in the negative power of 2 depending on their position
        return attribution

    #Keeping data of only those users who are getting converted at the end
    pd.options.mode.chained_assignment = None
    temp=dt.loc[dt[conv_col]==1]
    cookie_index=list(temp[user_id])
    dt['new']=dt[user_id].isin(cookie_index)
    y=dt['new'].isin([True])
    dt_conv=dt[y]

    dt_conv['temp']=1
    count=Counter(dt_conv[user_id])
    dt_conv['clicks']=dt_conv[user_id].map(count)
    dt_conv=dt_conv.assign(click_per=lambda x: round(100/dt_conv['clicks'],2))
    dt_conv['click_pos'] = dt_conv.groupby(user_id).cumcount() + 1              #Giving ranks to channels according to user_id
    dt_conv['PosDecay'] = dt_conv.apply(lambda val: calc_attribution(val.click_pos,val.clicks)*100,axis=1)
    dt_pos_decay=dt_conv

    #Getting the mean weightage of every channels
    res_pos_decay=dt_pos_decay.groupby('channel', as_index=False)['PosDecay'].mean()
    sum=res_pos_decay['PosDecay'].sum()
    res_pos_decay['Weightage(%)']=res_pos_decay.apply(lambda x: round((x['PosDecay']/sum)*100,2),axis=1)
    res_pos_decay.drop(['PosDecay'], axis=1,inplace=True)
    res_pos_decay=res_pos_decay.set_index(channel_col)
    res_pos_decay.index.name=None
    return res_pos_decay   
