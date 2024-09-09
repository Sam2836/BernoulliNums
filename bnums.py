# Experimentation with the power series of the generating function f(x) = x / (e^x - 1) which has been researched throroughly (see
# https://en.wikipedia.org/wiki/Bernoulli_number) prompted the development of this algorithm to take derivatives and evaluate
# their limits as the argument tends to 0; the result is the sequence of Bernoulli Numbers.

# No calculus is actually performed since the coefficients of the powers of e that appear in the derivatives follow a predictable
# pattern, as has been proven separately.

# The lists 'exp' and 'xexp' refer to the coefficients of e^x and xe^x respectively. For example, suppose exp[3] = 4 and xexp[2] = 5; then
# in the current derivative iteration we would see the terms 4e^3x and 5xe^2x appear. The lists encapsulate this behaviour.



v = 2   # Begins at the second derivative (i.e. "second iteration")

exp = [0, 2, -2]    # Values for iteration 2 are preloaded
xexp = [0, 1, 1]    # Everything is effectively 1-indexed (although ce^0 and cxe^0 are simply constant and linear terms respectively)

newexp = list(range(3))
newxexp = list(range(3))

def deriv_iterate() -> None:
    global exp
    global xexp
    global v
    
    for n in range(1, len(exp)):
        newexp[n] = xexp[n-1] + exp[n-1] * (n-v-2) - xexp[n] - n * exp[n]
        newxexp[n] = xexp[n-1] * (n-v-2) - n * xexp[n]
        
    newexp.append(xexp[n] + exp[n] * (n-v-1))
    newxexp.append(xexp[n] * (n-v-1))
    
    exp = newexp
    xexp = newxexp
    v+=1
    
    return