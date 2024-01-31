# function to create single touch attribution model - first touch model

def first_touch_model(dt, conv_col,channel_col,user_id):
    import pandas as pd
    temp=dt.loc[dt[conv_col]==1]          #Saving the dataframe where all the conversions are 1 into temp variable
    first_touch=pd.DataFrame(dt.groupby(user_id).first(),index=dt[user_id])       #Grouping with respect to cookie and then keeping only the first instance of every cookie
    cookie_index=list(temp[user_id])      #making a list of cookie column of temp
    mid_first_touch=first_touch.loc[cookie_index]     #locating cookie index in the first touch dataframe
    res_first_touch=pd.DataFrame(round(mid_first_touch[channel_col].value_counts(normalize=True)*100,2))    #Calculating weightage
    res_first_touch.columns=['Weightage(%)']
    return res_first_touch