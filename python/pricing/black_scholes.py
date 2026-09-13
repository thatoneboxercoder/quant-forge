import numpy as np
from scipy.stats import norm

def black_scholes_price (S, K, r, sigma, T, option_type ='call'):
    d1 = (np.log(S/K) + (r + ((sigma ** 2) / 2)) * T ) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))
 
    if option_type == 'call':
        price = (S * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))
    elif option_type == 'put':
        price = (K * np.exp(-r * T) * (norm.cdf(-d2))) - (S * norm.cdf(-d1))
    else:
        raise ValueError(f"option_type must be 'call' or 'put', got '{option_type}'")
    
    return price

print(black_scholes_price(100, 100, 0.05, 0.2, 1, option_type='call')) #10.450583572185565
print(black_scholes_price(100, 100, 0.05, 0.2, 1, option_type='put'))  #5.573526022256971

print(black_scholes_price(150, 100, 0.05, 0.2, 1, option_type='call')) #54.970140137999195
print(black_scholes_price(110, 100, 0.05, 0.0001, 1, option_type='call')) #14.877057549928594

