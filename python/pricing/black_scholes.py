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

def black_scholes_delta(S, K, r, sigma, T, option_type='call'):
    d1 = (np.log(S/K) + (r + ((sigma ** 2) / 2)) * T ) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))

    if option_type == 'call':
        delta = norm.cdf(d1)
    elif option_type == 'put':
        delta = norm.cdf(d1) - 1
    else:
        raise ValueError(f"option_type must be 'call' or 'put', got '{option_type}'")

    return delta

print(black_scholes_delta(100, 100, 0.05, 0.2, 1, 'call')) # 0.6368306511756191
print(black_scholes_delta(100, 100, 0.05, 0.2, 1, 'put'))  # -0.3631693488243809




