# Ontario Grade 12 Math Problem Generator #

```
Project by Wonjae Lee, Calvin Liew and Yong Le He
Copyright and Usage Information
=================================
(Idk if we need this)

```

## **About** ##

### **Project Goal** ###
  We aim to create an application to aid highschool students who are learning the Ontario Grade 12 curriculum (MHF4U - Advanced Functions & MCV4U - Calculus and Vectors). Our team will use the Sympy library that makes the process of converting Python inputs to mathematical notations conveniently.


### **General Credits** ###

**Backend Calculations**

**Unit 1 - Polynomial Functions:**
* generate_polynomial, generate_factorable_polynomial, find_discriminant, leading_coeff, end_behaviour, function_domain, function_range, x_int, y_int, characteristic by Wonjae Lee
* even_or_odd, points_of_polynomial, all_differences, transformation_of_function, transformation_explanation, average_rate_of_change, instant_rate_of_change, polynomial_degree by Calvin Liew
* turning_points, least_possible_degree, transformation_of_function, sympy_to_mathjax by Yong Le
* Docstring by Calvin Liew, Wonjae Lee, Yong Le

**Unit 2 - Polynomial Equations:**
* quotient, remainder, generate_poly_big_small1, generate_poly_big_small2, generate_cubic, generate_quartic, compare by Wonjae Lee
* is_factor, find_remainder by Yong Le He

**Unit 3 - Rational Functions:**
* rational_domain, rational_range, vertical_asymptote, horizontal_asymptote, x_int, y_int, attribute by Wonjae Lee


**Sqlite3 Database**
* Database setup, degree_and_leading_coeff by Calvin Liew

**Frontend Website**


### **Development Notes** ###

What's Done:

April 30, 2023
* generate_polynomial
* end_behaviour

May 1, 2023
* function_domain
* function_range
* turning_points
* Added requirements.txt

May 2, 2023
* finite_differences
* all_differences
* points_of_polynomials
* polynomial_degree

May 4, 2023
* even_or_odd
* average_rate_of_change
* instant_rate_of_change

May 5, 2023
* transformation_of_function
* sympy_to_mathjax

May 6, 2023
* Added docstring and doctests for several functions

May 11, 2023
* find_discriminant
* generate_factorable_polynomial

May 12, 2023
* characteristic
* transformation_explanantion
* least_possible_degree

May 13, 2023
* Setting up SQL Database
* rational_domain 
* rational_range 
* vertical_asymptote
* horizontal_asymptote 
* x_int for Unit 3
* y_int for Unit 3
* compare
* generate_cubic
* is_factor
* generate_quartic
* attribute
* degree_and_leading_coeff
