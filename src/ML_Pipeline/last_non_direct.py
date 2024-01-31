# function to create single touch attribution model - last non direct touch model

def last_non_direct_model(dt, conv_col, channel_col, user_id):
    import pandas as pd
    slp=pd.DataFrame(dt.groupby(user_id).tail(2))     #Grouping by cookie and keeping the last two observation for each cookie
    temp=slp.loc[slp[conv_col]==1]
    last_non_direct=pd.DataFrame(slp.groupby(user_id).first(),index=slp[user_id])
    cookie_index=list(temp[user_id])
    mid_last_non_direct=last_non_direct.loc[cookie_index]
    res_last_non_direct=pd.DataFrame(round(mid_last_non_direct[channel_col].value_counts(normalize=True)*100,2))
    res_last_non_direct.columns=['Weightage(%)']
    return res_last_non_direct