# Pre-interview

Eyuel Woldehanna

Fun Fact: I've been to over 10 countries and counting!

# How to run the code

In order to run this program, make sure that you have python3 installed if on mac and python installed if you are on Windows.

This program does not require any extra libraries to be installed, so all that is needed for you to do is run the following command in the projects src directory:

```
python3 run-queries.py
```

**Before you do any of that**

You'll need to check the paths in the script and update them to match your system:
- `queries_directory`: Path to the folder containing your SMT2 files
- `cvc5_executable`: Path to the cvc5 executable
- `output_csv`: Where you want the results saved

Now simply watch (or dont) as the script runs its course! 

There might be a bunch of debug statements printing in your terminal by now, and also feel free to change the time limit for the SMT solver by modifying the `--tlimit=60000` parameter in the code (time is in milliseconds).