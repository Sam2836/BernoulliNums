# Experimentation with the power series of the generating function f(x) = x / (e^x - 1) which has been researched throroughly (see
# https://en.wikipedia.org/wiki/Bernoulli_number) prompted the development of this algorithm to take derivatives and evaluate
# their limits as the argument tends to 0; the result is the sequence of Bernoulli Numbers.

# No calculus is actually performed since the coefficients of the powers of e that appear in the derivatives follow a predictable
# pattern, as has been proven separately.

# The lists 'exp' and 'xexp' refer to the coefficients of e^x and xe^x respectively. For example, suppose exp[3] = 4 and xexp[2] = 5; then
# in the current derivative iteration we would see the terms 4e^3x and 5xe^2x appear. The lists encapsulate this behaviour.



iteration = 1       # Begins at the first derivative (i.e. "first iteration")

exp_list = [0, 1]   # Values for iteration 1 are preloaded
xexp_list = [0, -1] # Everything is effectively 1-indexed (although ce^0 and cxe^0 are simply constant and linear terms respectively)

def deriv_iterate(n: int,
                  exp: list,
                  xexp: list,
                  ) -> list:
    
    newexp = list(range(v+1))
    newxexp = list(range(v+1))
    
    newexp[0] = 0
    newxexp[0] = 0
    
    

    n+=1
    
    return [newexp, newxexp, n]