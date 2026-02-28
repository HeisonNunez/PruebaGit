import torch

#crear tensores de una lista
a = torch.tensor([1, 2, 3])
print(a)

#crear tensor de ceros
b = torch.zeros(2, 3)
print(b)

#crear tensor aleatorio
c = torch.rand(2, 3)
print(c)


#OPERACION BASICAS
print("OPERACION BASICAS")

x = torch.tensor([1.0, 2.0, 3.0, 4.0])
y = torch.tensor([5.0, 6.0, 7.0, 8.0])

suma = x + y
producto = x * y

print(suma)
print(producto)

z = torch.tensor(2.0, requires_grad=True)
t = z**2 + 3*z
t.backward()
print(z.grad)