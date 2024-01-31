# function to create multitouch attribution model - position based model / u-shaped model

def u_shaped_model(dt, conv_col, channel_col, user_id):

    import pandas as pd
    from collections import Counter

    def calc_attribution(click_pos,total_clicks):

        #Assigning weightage according to the position of the channel
        default_att = 0.5       #if a user has visited only 2 channels 
        extreme_touch_att_1 = 0.4     #Assigining weightage to first and last channels
        intermed_att_1 = 0.2    #Total weightage for remaining channels

        if  total_clicks == 2:     
            return default_att

        elif total_clicks == 1:
            return 1
        else:
            if click_pos == total_clicks or click_pos ==1:
                return extreme_touch_att_1
            else:
                return intermed_att_1/(total_clicks-2)      #Giving equal weightage to all the mid channels from the remaining 20%

    #Keeping data of only those users who are getting converted at the end
    pd.options.mode.chained_assignment = None     #Ignoring pandas warnings
    temp=dt.loc[dt[conv_col]==1]
    cookie_index=list(temp[user_id])
    dt['new']=dt[user_id].isin(cookie_index)
    y=dt['new'].isin([True])
    dt_conv=dt[y]

    count=Counter(dt_conv[user_id])
    dt_conv['clicks']=dt_conv[user_id].map(count)
    dt_conv['click_pos'] = dt_conv.groupby(user_id).cumcount() + 1      #Giving ranks to the channel for each user_id
    dt_Ushaped=dt_conv
    dt_Ushaped['U_Shape'] = dt_conv.apply(lambda val: round(calc_attribution(val.click_pos,val.clicks)*100,2),axis=1)

    #Getting the mean weightage of every channels
    res_Ushaped=dt_Ushaped.groupby(channel_col, as_index=False)['U_Shape'].mean()
    sum=res_Ushaped['U_Shape'].sum()
    res_Ushaped['Weightage(%)']=res_Ushaped.apply(lambda x: round((x['U_Shape']/sum)*100,2),axis=1)
    res_Ushaped.drop(['U_Shape'],inplace=True,axis=1)
    res_Ushaped=res_Ushaped.set_index(channel_col)
    res_Ushaped.index.name=None
    return res_Ushaped