"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
import math 

cateto_oposto = float(input("Cateto Oposto: "))
cateto_adjacente = float(input("Cateto Adjacente: "))
print(f"A hipotenusa é: {math.hypot(cateto_oposto, cateto_adjacente)}")