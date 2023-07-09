'''addition'''
import numpy as np   
a1=np.array([11,21,31,41,51,61])
a2=np.array([10,20,30,40,50,60])
print(np.add(a1,a2))
# print(np.array(a1-a2))  #subtraction



'''subtraction'''
a1=np.array([1,2,3,4,5,6])
a2=np.array([10,20,30,40,50,60])
print(np.subtract(a2,a1))


'''#Multiplication'''
a1=np.array([1,2,3,4,5,6]) 
# a2=np.array([10])
a2=np.array([10,20,30,40,50,60])
print(np.multiply(a1,a2))


'''division'''
a1=np.array([2,5,3,7,9,4])
a2=np.array([10,20,30,40,50,60])
print(np.divide(a2,a1))


'''power'''
a1=np.array([2,10,20,13,4])
a2=np.array([5,3,2,2,3])
print(np.power(a1,a2))


'''modulus&Remainder'''
a1=np.array([12,13,14,15,16])
a2=np.array([2,3,4,5,6])
print(np.mod(a1,a2)) #modulus
print(np.remainder(a1,a2))



'''Quotient and Mod(Quotien&remaider)'''
a1 = np.array([10, 20, 30, 40, 50, 60])
a2 = np.array([3, 7, 9, 8, 2, 33])
print(np.divmod(a1,a2))


'''Absolute Values(abs & absolute give same value)'''
a=np.array([-1,-2,1,2,-13,-4])
print(np.abs(a))
print(np.absolute(a))