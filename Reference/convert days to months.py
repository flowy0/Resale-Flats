#convert days to months
#credit to https://stackoverflow.com/questions/42822768/pandas-number-of-months-between-two-dates/42822819

 df['nb_months'] = ((df.date2 - df.date1)/np.timedelta64(1, 'M'))
 df['nb_months'] = df['nb_months'].astype(int)

