# function to create single touch attribution model - last touch model

def last_touch_model(dt, conv_col,channel_col):         #Defining function for last touch model
    import pandas as pd
    last_touch=dt.loc[dt[conv_col]==1]          #Extracting rows where conversion is 1 
    res_last_touch=pd.DataFrame(round(last_touch[channel_col].value_counts(normalize=True)*100,2))      #Calculating the weightage
    res_last_touch.columns=['Weightage(%)']   
    return res_last_touch