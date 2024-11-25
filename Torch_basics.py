import torch
import numpy as np
x = torch.ones(2)
# print(x)

y = torch.tensor([2.5,3])
print(y)

# z = x+y
z = torch.add(x,y)
print(z)

y.add_(x)
print(y)

subtraction = torch.sub(x,y)
print(subtraction)

multiplication = torch.mul(x,y)
print(multiplication)

q= torch.rand(4,4)
print(q)
print(q[:,2])
print(q[2,3])

w = q.view(-1,8)
print(w)

# Torch to numpy
a= torch.ones(5)
b = a.numpy()
print(type(b))


#Numpy to Torch
d = np.ones(2)
g = torch.from_numpy(d)
print(type(g))


