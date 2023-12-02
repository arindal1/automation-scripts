% Facts
symptom(john, fever).
symptom(john, cough).
symptom(jane, headache).
symptom(jane, nausea).

% Rules
diagnosis(Person, cold) :- symptom(Person, fever), symptom(Person, cough).
diagnosis(Person, flu) :- symptom(Person, fever), symptom(Person, nausea).
