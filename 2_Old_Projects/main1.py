# multivariate multi-step 1d cnn example

from numpy import hstack
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from func1 import *
from query1 import *
from keras.callbacks import ModelCheckpoint

df = data1()
df.index = df['timestamp']
df.sort_index(inplace=True)

df.dropna(inplace=True)
print(df.shape)

# print last row
dta = df.iloc[-1:,0:1].values[0][0]
print('last row',type(dta),dta)
#
df.drop(('timestamp'), axis=1, inplace=True)
dfval = df.values
print(type(dfval), dfval.shape) # (2400, 27) = (sample, features)
#
n_steps_in, n_steps_out = 3, 2
#
# # convert into input/output
X, y = split_sequences(dfval, n_steps_in, n_steps_out)
#
print(X.shape) # (2397, 3, 25) = (samples, n_steps_in, n_features)
print(y.shape) # (2397, 2) = (samples, n_steps_out)
#
# # the dataset knows the number of features, e.g. 2
n_features = X.shape[2]
#
# # define model
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=(n_steps_in, n_features)))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(n_steps_out))
model.compile(optimizer='adam', loss='mse')
#
# # fit model
save_path = 'models/'
filepath=save_path+"weights-v-{epoch:02d}.hdf5"
checkpointer = ModelCheckpoint(monitor='val_loss', filepath=filepath, verbose=1, save_best_only=True)
model.fit(X, y, validation_split=0.2, batch_size=64, epochs=2000, verbose=1, callbacks=[checkpointer])