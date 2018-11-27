#!/usr/bin/evn python

#Produces a scatter plot of the found information of Pc vs Hydrogen production

import matplotlib.pyplot as plt

Pc = [1,3,5,7,9]

Hydrogen_Production = [2,4,7,5,9]

plt.scatter(Pc,Hydrogen_Producetion, label='No_Hydrogen_if_die , color='c', marker='^')



plt.xlabel('Pc')
plt.ylabel('Hydrogen_Production')
plt.title('Hydrogen_Prod vs Pc')
plt.legend()
plt.show()
