# bayestheorem.py
# Prometheus111
# Bayes Theorem (the Bayes formula) / Solution of the problem / Elementary probability theory

V = eval(input('Type number of your variant (V): '))
print('\nSolution:')

#calculation of the coefficient k (modulo)
k = abs(14 - V)

#output of calculation
print('\nk =', k)

#calculation of the number of electric motors from the 1st, 2nd and 3rd plants
N1, N2, N3 = (5 + k), (20 - k), (25 - k)
N = (N1 + N2 + N3)  #total electric motors

#output of calculation
print('\nNumber of electric motors delivered:\
      \n1st manufacturing plant (N1):', N1, '\
      \n2nd manufacturing plant (N2):', N2, '\
      \n3rd manufacturing plant (N3):', N3, '\
      \nTotal electric motors (N):', N)

#calculation of the probability of operation of electric motor until the end of the warranty period
#from 1st, from 2nd и from 3rd manufacturing plants
p1, p2, p3 = (0.99 - (k / 100)), (0.9 - (k / 100)), (0.85 - (k / 100))

#output of calculation
print('\nThe probability of operation of electric motor until the end of the warranty period:\
      \nfrom 1st manufacturing plant: p1 =', p1, '\
      \nfrom 2nd manufacturing plant: p2 =', p2, '\
      \nfrom 3rd manufacturing plant: p3 =', p3)

#output the Bayes formula
print('\n\tThe Bayes formula:\n\
\n\t         P(B|A)P(A)\
\n\tP(A|B) = __________\
\n\t            P(B)')

#calculating the numerator
PBA1PA1, PBA2PA2, PBA3PA3 = ((p1 * N1) / N), ((p2 * N2) / N), ((p3 * N3) / N)

#output of calculation
print('\n\tCalculating the numerator P(B|A)P(A):\
      \n\t1: P(B|A1)P(A1) =', PBA1PA1, '\
      \n\t2: P(B|A2)P(A2) =', PBA2PA2, '\
      \n\t3: P(B|A3)P(A3) =', PBA3PA3)

#calculation of the denominator
PB = PBA1PA1 + PBA2PA2 + PBA3PA3

#output of calculation
print('\n\tCalculation of the denominator P(B):\
      \n\tP(B) = P(B|A1)P(A1) + P(B|A2)P(A2) + P(B|A3)P(A3)\n\tP(B) =', PB)

#The probability P(A|B) of operation of electric motors before
#the end of the warranty period is delivered respectively by 1st, 2nd, 3rd manufacturing plants:
PA1B, PA2B, PA3B = (PBA1PA1 / PB), (PBA2PA2 / PB), (PBA3PA3 / PB)

#output of the probability of operation of electric motors before the end of the warranty period
print('\nThe probability P(A|B) of operation of electric motors before\
      \nthe end of the warranty period is delivered respectively:\
      \nby 1st manufacturing plant P(A1|B) =', PA1B, '\
      \nby 2nd manufacturing plant P(A2|B) =', PA2B, '\
      \nby 3rd manufacturing plant P(A3|B) =', PA3B)
# Enjoy lerning new things! Prometheus111 helps you with your studying!
# https://github.com/Prometheus111 
