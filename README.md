Implement three algorithms:
– Iterative Matrix Multiplication algorithm.
– Divide-and-Conquer Matrix Multiplication algorithm.
– Strassen’s Algorithm.
Assume that all matrix multiplication operations will take two square n×n matrices
as input.
In implementing these algorithms you are only allowed to use the following language
features:
– Integer variables
– Integer arrays of any dimensionality.
– Addition and subtraction of integers.
– Multiplication of integers.
– Control structures of your programming language (loops and conditionals) as well
as function calls and user-defined functions.

You are not allowed to use any matrix arithmetics operations or any vector arith-
metics operations.
In addition, implement a testing mechanism that allows you to collect the infor-
mation about the run time of your implementation. The testing mechanism, at a
minimum, shall consist of the following:

– A procedure for generating a random n × n matrix with n^2 integer values in it.

– Archive any generated matrices (this is needed to make sure that your algorithms
are tested on the same set of matrix multiplication operations).

– Find the execution time of each of the matrix multiplication algorithms you im-
plement.

– A procedure that takes as input a set of experimental parameters, performs the
desired run-time experiment (see below), and collects the run-time data.

– Save the results of the experiment in a way that can be used for further analysis
Performing Experiments

With the three implementations of the Matrix Multiplication algorithms, and with the
test mechanism you build to test them, you perform a run-time experiment designed
to understand how the performance of the algorithms changes with the increase in the
input size.

The experiment should have the following parameters:

(a) Matrix sizes. Select between 10 and 20 different matrix sizes starting with some-
thing relatively small (e.g., n = 10, and ending with a reasonably large matrix size
that still can fit comfortably in RAM (e.g., n = 1000). Matrix sizes is the first
parameter of your experiment.

(b) Repetitions. For each matrix size, you generate a number of pairs of matrices
to be multiplied using your algorithm implementations. This is controlled by the
second parameter called Repeats. We want Repeats > 1, because we want to
convince ourselves that the runtime of your implementation observed for a specific
pair of matrices of size n×n is consistent with the run-times observed on all other
pairs of matrices of the same size.

(c) Measurement. For each matrix size and for each repetition step, generate two
matrices of the appropriate size and compute their product using all three of your
methods. Find the running time for each computation. For each matrix size, aggre-
gate the results by computing the average running time, and standard deviation
of the running time for each of the three algorithm implementations.

(d) Reporting. For each algorithm, you should obtain a set of average run-times for
each input size considered. Plot these runtime numbers vs input size. If possible,
fit a curve to them to see if they follow the expected algorithm run-times.

(e) Analysis. Observe the results and answer the following questions.
– What is the observed run-time behavior for each algorithm?
– Which algorithm is the fastest in your experiment? Which is the slowest?
– What are the asymptotic trends for each algorithm? Can you observe or predict
if Strassen’s Algorithm overtakes one or both of the remaining ones at some
point?

(f) Report. Prepare a properly formatted, and presentable report describing your
work. The report shall contain the precise description of the experiment your im-
plemented, and the experimental results both in tabular and in graphical form,
and it shall contain your analysis.
