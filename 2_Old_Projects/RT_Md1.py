from func1 import *
from query1 import *

df = data1()
df.index = df['timestamp']
df.index = df.index.astype('datetime64[ns]')
df.sort_index(inplace=True)
df.dropna(inplace=True)
df['timestamp'] = pd.to_datetime(df['timestamp'])
# print(df)

dtat0 = df.iloc[-1:,0:1].values[0][0]
dti = pd.date_range(dtat0, periods=2, freq='0.5H').shift(1,freq='0.5H')
dfdt = dti.to_frame(index=False, name='datims')

df.drop(('timestamp'), axis=1, inplace=True)

from sklearn.preprocessing import MinMaxScaler
y_scaler = MinMaxScaler()
y_scaler.fit(df[['Q']])
X_scaler = MinMaxScaler()

df[['fore24', 'tail24', 'tail24_avg', 'evap', 'infl', 'losses',
       'rel1', 'rel2', 'rel3', 'rel_tol', 'engr1', 'engr2', 'engr3', 'cond1',
       'cond2', 'cond3', 'str1', 'str2', 'str3', 'run_g1', 'run_g2', 'run_g3',
       'run_c1', 'run_c2', 'run_c3', 'spillway', 'irr', 'camp', 'demand',
       'derate', 'outage', 'stor']] = X_scaler.fit_transform(df)

dfval = df.values

n_steps_in, n_steps_out = 3, 2
X, y = split_sequences(dfval, n_steps_in, n_steps_out)
n_features = X.shape[2]
print(X.shape) # (5973, 3, 31) = (samples, n_steps_in, n_features)
print(y.shape) # (5973, 2) = (samples, n_steps_out)

model_2 = ShallowConvNet(n_steps_in=n_steps_in, n_steps_out=n_steps_out, n_features=n_features)
model_2.load_weights("models/model1.hdf5")
model_2.compile(optimizer='adam', loss='mse')
Y_pred = model_2.predict(X)

yp = y_scaler.inverse_transform(Y_pred)
# print(yp)
# print('Y_pred', type(yp), yp.shape)

from sqlalchemy import create_engine
user='root'
pwd='opt#565784'
dbname='predictive'
host='10.211.1.25'
port=3306
con = create_engine(f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}')

df = pd.DataFrame(yp).T
df.columns = ['stor']
print(df)
print(dfdt)

com = pd.concat([dfdt, df], axis=1, join='inner')
print(com)
com.to_sql('waterpred', con, if_exists='append', index=False)