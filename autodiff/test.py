import autodiff as ad
import numpy as np


x2 = ad.Variable(name = "x2")
x3 = ad.Variable(name = "x3")
y = ad.matmul_op(x2, x3)

grad_x2, grad_x3 = ad.gradients(y, [x2, x3])

executor = ad.Executor([y, grad_x2, grad_x3])
x2_val = np.array([[1, 2], [3, 4], [5, 6]]) # 3x2
x3_val = np.array([[7, 8, 9], [10, 11, 12]]) # 2x3

y_val, grad_x2_val, grad_x3_val = executor.run(feed_dict = {x2: x2_val, x3: x3_val})

expected_yval = np.matmul(x2_val, x3_val)
expected_grad_x2_val = np.matmul(np.ones_like(expected_yval), np.transpose(x3_val))
expected_grad_x3_val = np.matmul(np.transpose(x2_val), np.ones_like(expected_yval))