# Illumio_Coding_Challenge
2018 Illumio Internship challenge (build a firewall validator). I set a timer for 90 minutes before beginning. This solution is not yet complete, but only a **reflection of what I could do in 90 minutes**. If given more time (about 30min-1hr longer, I would have been able to finish).


# How you tested your solution
I tested my solution by running print statements (similar to asserts) on the examples given in the spec sheet. I was 70% satisfied when I passed all those cases, but was not content with 70% satisfaction. I increased that number by writing checks to ensure even edge cases would work. 

Here are a few of the edge cases I was able to think about: 
  1. Empty ranges
  2. Ranges that fall outside of the numerical values accepted
  3. Duplicate values (did not have time to implement)


# Any interesting coding, design, or algorithmic choices you’d like to point out
I used dictionaries in python because they can be accessed in constant O(1) time. An important part of this assignment is ensuring scalability. A typical firewall log can consist of millions of lines, so must be able to lookup and match the rules in constant time. 


# Any refinements or optimizations that you would’ve implemented if you had more time
1. I would have implemented a map of <dicts, ints> to count the number of like entries to keep count of common incoming ports.
2. I would optimize the main `main_utility_function` to work in a smaller polynomial time degree than current. It is a pretty naive approach to this problem and runs in O(n) time to iterate through the rules. I would try to make the algorithm run in O(1) time. 


# My Illumio Role Preference Ranking
I am open to trying to fit into any role that is needed, but here is a ranking of my interests:
1. Data
2. Platform
3. Policy
