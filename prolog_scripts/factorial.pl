% Rules
factorial(0, 1).
factorial(N, Result) :- N > 0, N1 is N - 1, factorial(N1, R1), Result is N * R1.

% Query: Calculate factorial of 5
% ?- factorial(5, Result).
