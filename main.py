import numpy as np

print(np.array([1, 2, 3]))

odd_number_list = [1, 3, 5, 7]
print(np.array(odd_number_list))  #получится одномерный массив

two_dim_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(np.array(two_dim_list))    #получится многомерный массив (в этом конкретном случае двумерный) или матрица,

print(np.arange(0, 9))

print(np.arange(0, 10, 2))

print(np.zeros(8))

print(np.zeros((2, 3)))

print(np.zeros((3, 2)))

print(np.ones(4))

print(np.ones((2,3)))

print(np.linspace(0,5,5))

print(np.linspace(0,10,5))

print(np.eye(3))       #identity matrix

print(np.eye(6))

#print(np.random.rand(3))

#print(np.random.rand(6))

#print(np.random.rand(3,4))

#print(np.random.randn(6))

#print(np.random.randn(3,4))

#print(np.random.randint(0,50,10))

#rand_arr = np.random.randint(0,50,20)
#print(rand_arr)
#print(rand_arr.max())
#print(rand_arr.argmax())
#print(rand_arr.min())
#print(rand_arr.argmin())

#print(rand_arr.reshape(4,5))
#print(rand_arr.reshape(5,5))
#print(rand_arr.reshape(5,4))

second_arr = np.arange(20)
print(second_arr)
print(second_arr.reshape(2,10))
print(second_arr.max())
print(second_arr.min())
print(second_arr.argmax())
print(second_arr.shape)

reshaped_arr=second_arr.reshape(2,10)
print(reshaped_arr)
print(reshaped_arr.shape)
print(reshaped_arr.dtype)
