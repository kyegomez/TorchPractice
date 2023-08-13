import torch 
import numpy 

#prexisting arrays
w = torch.tensor([1, 2, 3])

#tuple
w = torch.tensor((1, 2, 3))

# numpy array
w = torch.tensor(numpy.array([1, 2, 3]))

#init by sized
w = torch.empty(100, 200) #not initialized
w = torch.zeros(100, 200) # elements with 0.0
w = torch.ones(100, 200) # elements with 1.0

#random tensor inits 
w = torch.randn(100, 200) #creates 100 x 200 tensor with elements from a uniform distribution on the interval [0, 1]
w = torch.randn(100, 200) # elements are random numbers from a normal distribution, with a mean of 0 and a veriance of 1
w = torch.randint(5, 10, (100, 200)) # elements are random integers between 5 and 10

#init with specified data type and device
w = torch.empty((100, 200), dtype=torch.float64, 
                device='cuda')

#init to have the same szie data type;
x = torch.empty_like(w)

#specify type using dtype
w = torch.tensor([1, 2, 3], dtype=torch.float32)

#use casting method to cast to a new data type
w.int() # w remains a float32 after the cast
w = w.int() # w changes to an int 32 after the cast

#use the to() method to cast to a new type
w = w.to(torch.float64)
w = w.to(dtype=torch.float64)

#python converts data types in ops