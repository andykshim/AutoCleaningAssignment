# AutoCleaningAssignment
Randomized Assignment of House Cleaning duties \
Written July 2023 by Andrew Shim \
For Sigma Nu Gamma Theta


**Inputs:**\
_brothers_master.csv_ \
_cleanings_master.csv_

**Output:**\
_weekly_cleang.csv_


**How to use:**
1. Input chapter members in _brothers_master.csv_ :\
   _First_: First Name \
   _Last_:   Last Name \
   _livesIn_: TRUE/FALSE, Specify live-out brothers for Sunday cleanings only \
   _dishes_: TRUE/FALSE, Specify those for dish duty \
   _num_: Running Count of # of cleanings completed. Set to 0 at start of semester. The script assigns as fairly as possible based on this parameter.

2. Input weekly cleanings in _cleanings_master.csv_ :\
   _Name_: Name of cleaning, ie Sunday Great Hall \
   _day_: Monday-Sunday \
   _canLiveOut_: TRUE/FALSE, Set to TRUE for Sunday Cleanings \
   _isDishes_: TRUE/FALSE

3. Run _main.py_: \
   Output is created in _weekly_cleang.csv_ in the following format: \
   _Column 1_: Name of cleaning \
   _Column 2_: Name of brother assigned to cleaning \
   _Column 3_: Total number of cleanings completed by brother after this week \
   Double Check Schedule for any avoidable scheduling, ie. 2 days in a row of dishes. If unhappy with output, re-run _main.py_. \
   Otherwise, step 4.
   
5. Run _updateNums.py_: \
   This updates the _num_ field under inputs with the value from output \
   In other words, confirms the output schedule and adds the ongoing tally for each person.

6. (Recommended) Copy and paste _weekly_cleang.csv_ to google sheets/excel and auto-format into nice weekly schedule
   

 
