import tensorflow as tf
import numpy as np
import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

epochs = 100
learning_rate = 0.01

input_layer_nodes = 1000
hidden1_layer_nodes = 500
hidden2_layer_nodes = 500
output_layer_nodes = 10

x_data = np.zeros([5000, 1000])
y_data = np.zeros([5000, 10])

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

theta1 = tf.Variable(tf.random_uniform([input_layer_nodes, hidden1_layer_nodes], minval=-1, maxval=1, name='theta1'))
theta2 = tf.Variable(tf.random_uniform([hidden1_layer_nodes, hidden2_layer_nodes], minval=-1, maxval=1, name='theta2'))
theta3 = tf.Variable(tf.random_uniform([hidden2_layer_nodes, output_layer_nodes], minval=-1, maxval=1, name='theta3'))

bias1 = tf.Variable(tf.zeros([hidden1_layer_nodes]))
bias2 = tf.Variable(tf.zeros([hidden2_layer_nodes]))
bias3 = tf.Variable(tf.zeros([output_layer_nodes]))

layer2 = tf.sigmoid(tf.matmul(X, theta1) + bias1)
layer3 = tf.sigmoid(tf.matmul(layer2, theta2) + bias2)
hypothesis = tf.sigmoid(tf.matmul(layer3, theta3) + bias3)

term1 = -(Y * tf.log(hypothesis))
term2 = -((1-Y) * tf.log(1-hypothesis))
cost = tf.reduce_mean(term1 + term2)

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
init_var = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_var)
    for i in range(epochs):
        sess.run(optimizer, feed_dict={X: x_data, Y: y_data})
        if i % 10 == 0:
            print(sess.run(cost, feed_dict={X: x_data, Y: y_data}))
            taklu = sess.run([hypothesis, Y], feed_dict={X: x_data, Y: y_data})
            answer = tf.equal(tf.floor(taklu[0] + 0.5), taklu[1])
            accuracy = tf.reduce_mean(tf.cast(answer, tf.float32))
            print(sess.run(accuracy, feed_dict={X: x_data, Y: y_data})*100)

