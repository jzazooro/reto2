import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


model = Sequential()

model.add(Dense(5, input_dim=input_dim, activation='soft_plus_te'))
model.add(Dense(10, activation='soft_plus_te'))
model.add(Dense(20, activation='tanh'))
model.add(Dense(15, activation='relu'))
model.add(Dense(25, activation='tanh'))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(25, activation='relu'))
model.add(Dense(output_dim, activation='soft_plus_te'))
model.add(Dropout(0.2))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(train_x,train_y,epochs=number_epo,verbose=0,batch_size=10,
validation_data=(test_x, test_y))
model.summary()