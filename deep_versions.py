#!c:\Programming\Anaconda2\envs\tensorflow\python

# c:\Programming\Anaconda2\envs\tensorflow\python  # python 3.5
# c:\Programming\Anaconda2\envs\py36\python   # python 3.6
# c:\Programming\Anaconda2\python


import sys
print(sys.version)

import scipy
print('scipy: %s' % scipy.__version__)
# numpy
import numpy
print('numpy: %s' % numpy.__version__)
# matplotlib
import matplotlib
print('matplotlib: %s' % matplotlib.__version__)
# pandas
import pandas
print('pandas: %s' % pandas.__version__)
# statsmodels
import statsmodels
print('statsmodels: %s' % statsmodels.__version__)
# scikit-learn
import sklearn
print('sklearn: %s' % sklearn.__version__)


# theano
import theano
print('theano: %s' % theano.__version__)
# tensorflow
import tensorflow
print('tensorflow: %s' % tensorflow.__version__)
# keras
import keras
print('keras: %s' % keras.__version__)



import tensorflow as tf




hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
