# Program for calculating the degrees of freedom for any given robot using Grubler's Formula

# User inputs for the formula calculation
m = int(input("Indicate the dimension of analysis (2D = 3, 3D = 6): "))
N = int(input("Input number of links: "))
J = int(input("Input number of joints: "))

dof1 = int(input("Input number of single degree of freedom joints: "))
dof2 = int(input("Input number of two degrees of freedom joints: "))
dof3 = int(input("Input number of three degree of freedom joints: "))

Grubler = m*(N-1-J) + (dof1*1+dof2*2+dof3*3)

# Note: this answer will not take into account any internal DoFs, so be sure to do that after
print("The DoF of this system is",Grubler)
