"""
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. 
It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1. How to 
maximize total profit if only one job can be scheduled at a time.

Examples:
Input: Four Jobs with following deadlines and profits
  JobID    Deadline      Profit
    a        4            20   
    b        1            10
    c        1            40  
    d        1            30
Output: Following is maximum profit sequence of jobs
        c, a   


Input:  Five Jobs with following deadlines and profits
   JobID     Deadline     Profit
     a         2           100
     b         1           19
     c         2           27
     d         1           25
     e         3           15
Output: Following is maximum profit sequence of jobs
        c, a, e

A Simple Solution is to generate all subsets of given set of jobs and check individual subset for feasibility of jobs in 
that subset. Keep track of maximum profit among all feasible subsets. The time complexity of this solution is exponential.

This is a standard Greedy Algorithm problem. Following is algorithm.

1) Sort all jobs in decreasing order of profit.
2) Initialize the result sequence as first job in sorted jobs.
3) Do following for remaining n-1 jobs
.......a) If the current job can fit in the current result sequence 
          without missing the deadline, add current job to the result.
          Else ignore the current job.
"""
# function to schedule the jobs take 2  
# arguments array and no of jobs to schedule 
def printJobScheduling(arr, t): 
  
    # length of array 
    n = len(arr) 
  
    # Sort all jobs according to  
    # decreasing order of profit 
    for i in range(n): 
        for j in range(n - 1 - i): 
            if arr[j][2] < arr[j + 1][2]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    print(arr)
     
    # To keep track of free time slots 
    result = [False] * t 
  
    # To store result (Sequence of jobs) 
    job = ['-1'] * t 
  
    # Iterate through all given jobs 
    for i in range(len(arr)): 
  
        # Find a free slot for this job  
        # (Note that we start from the  
        # last possible slot) 
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1): 
              
            # Free slot found 
            if result[j] is False: 
                result[j] = True
                job[j] = arr[i][0] 
                print('result=' + repr(result))
                print('job=' + repr(job))
                break
  
    # print the sequence 
    print(job) 
  
# Driver COde 
arr = [['a', 2, 100], # Job Array 
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]] 

arr1 = [['a', 2, 60],
       ['b', 2, 100],
       ['c', 3, 20],
       ['d', 2, 40],
       ['e', 1, 20]]  
  
print("Following is maximum profit sequence of jobs") 
printJobScheduling(arr1, 3) # Function Call
