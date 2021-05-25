# Heuristic_Optimization__Implementation_ex2



2020/2021

Heuristic Optimization

Implementation exercise 02

Dr.T.Stutzle

Federico Pagnozzi

Sif Eddine Boughris

2020







# First Algorithm tabu search

# 1.1 Methodology

I create class called Local search contain 6 algorithm for the local search best and ﬁrst impro-

vement with insert exchange and transpose. the input is the instance and the initial solution the

output is a list of the permutation and the wct .

1. ﬁrst-improvement-Insert

2. ﬁrst-improvement-exchange

3. ﬁrst-improvement-transpose

4. best-improvement-Insert

5. best-improvement-exchange

6. best-improvement-transpose

in the class Tabu-search i create the algorithm based on the information given in the course .

my initial solution was done by random because we will repeat the solution multiple time so if i

did the SRZ it will give me the same initial solution .

for the termination criterion i set a timer that start from 0 and will stop the search when it reach a

given number by second .

i choose to work with best improvement insert it create the neighbors and calculate what is the

best of them and return the ﬁnal solution permutation reached store the solution in a TABU list

and check if we all ready visit that neighborhood so we don’t calculate it again .


To run the algorithm for one instance you need to call the function Tabu-search, write TS give

it the ﬁle name and how many second its gonna run in it .

# example :

. . \ Implimentation\_02>python Tabu\_search . py TS 50\_20\_01 30

the experiment timer is set to 300 for the instance of 100 jobs and 150 for the instance of 50

jobs. the number of repetition is 5 for each instance.

To run the experement just call the function get-experement-Tabu-search-result-100,get-experement-

Tabu-search-result-50. by just calling Tabu100 and Tabu50.

. . \ Implimentation\_02>python Tabu\_search . py Tabu100

. . \ Implimentation\_02>python Tabu\_search . py Tabu50






# Second Algorithm Iterated Local Search

# 2.1 Methodology

I create class called Local search contain 6 algorithm for the local search best and ﬁrst impro-

vement with insert exchange and transpose. the input is the instance and the initial solution the

output is a list of the permutation and the wct .

\1. ﬁrst-improvement-Insert

\2. ﬁrst-improvement-exchange

\3. ﬁrst-improvement-transpose

\4. best-improvement-Insert

\5. best-improvement-exchange

\6. best-improvement-transpose

FIGURE 2.1: Iterated-Local-search

In the class Iterated-Local-search i create the algorithm based on the information given in the

course .

my initial solution was done by random then i give it to the algorithm best-improvement-Insert

and get the permutation solution from it then enter the exit condition and preform a best-improvement-

exchange while exploring new neighbors if we ﬁne a new best solution we set it as the best solution


To run the algorithm for one instance you need to call the function Iterated-Local-Search.py,

write ILS give it the ﬁle name and how many second its gonna run in it .

# example :

. . \ Implimentation\_02>python Iterated\_Local\_Search . py ILS 50\_20\_01 30

the experiment timer is set to 300 for the instance of 100 jobs and 150 for the instance of 50

jobs. the number of repetition is 5 for each instance.

To run the experement just call the function get-experement-ILS-result-100,get-experement-

ILS-result-50. by just calling ILS100 and ILS50.

. . \ Implimentation\_02>python Iterated\_Local\_Search . py ILS100

. . \ Implimentation\_02>python Iterated\_Local\_Search . py ILS50





# Results

i run the 4 experement (ILS50,ILS100,TABU50,TABU100) at the same time i elemenate the ac-

cese of both algo to the same ﬁle by working with view of the instance my PC is not great with out

the computation power so the 2 algorithm did not explore alot of nighbores.

FIGURE 3.1: The algorithm solution compare to the best solution



# 3.1 Average

FIGURE 3.2: Avrage RPD

from the plot we can see that the ILS is the one that gave us the best result for the 100 jobs the

avrage was almost 27 percent the 50 job it was 10 percent and in all the instance the avrage was 19

percent.


3.3 Wilcoxon test

the result obtined by wilcoxon test on the RPD was p-value = 1.758e-11 a strong indication that

the RPD medians are signiﬁcantly different.



# Conclusion

we can see from the result we got that for our experiment that the ILS is better then Tabu search

and the 50 jobs are butter then the 100 because i think it take less time to calculate and therefore

we have more time to explore .

adding more repetition and more search time improved our result signiﬁcantly .

