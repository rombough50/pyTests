#This is where the python code would be 
# So this code was committed local and then published. The repository had not been previously published.
# I changed this file up here
# That worked with a combination of Code and GitHUB desktop
# Ok this is the last test to see if stuff can be pushed up there
# Ok one last time with CODE before VS2019
# that didnt work


import tensorflow as tf #we import tensorflow
import numpy as np #we import numpy
sess = tf.Session() #start a new Session Object
x_data = np.array([[1.,2.,3.],[3.,2.,6.]]) # 2x3 matrix
x = tf.convert_to_tensor(x_data, dtype=tf.float32)
print (x)