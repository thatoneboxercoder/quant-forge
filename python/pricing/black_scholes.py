import numpy as np
from scipy.stats import norm

def black_scholes_price(S, K, r, sigma, T, option_type ='call'):
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

    if option_type == 'call':
        delta = norm.cdf(d1)
    elif option_type == 'put':
        delta = norm.cdf(d1) - 1
    else:
        raise ValueError(f"option_type must be 'call' or 'put', got '{option_type}'")

    return delta

def black_scholes_gamma(S, K, r, sigma, T):
    d1 = (np.log(S/K) + (r + ((sigma ** 2) / 2)) * T ) / (sigma * np.sqrt(T))

    gamma = (norm.pdf(d1)) / (S * sigma * np.sqrt(T))

    return gamma

def black_scholes_vega(S, K, r, sigma, T):
    d1 = (np.log(S/K) + (r + ((sigma ** 2) / 2)) * T ) / (sigma * np.sqrt(T))

    vega = S * norm.pdf(d1) * np.sqrt(T)

    return vega

def black_scholes_theta(S, K, r, sigma, T, option_price='call'):
    d1 = (np.log(S/K) + (r + ((sigma ** 2) / 2)) * T ) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))

    if option_price == 'call':
        theta = -(
            (S * norm.pdf(d1) * sigma )
            / (2 * np.sqrt(T))) - (r * K * np.exp(-r * T) * norm.cdf(d2))
    elif option_price == 'put':
        theta = -(
            (S * norm.pdf(d1) * sigma )
            / (2 * np.sqrt(T))) + (r * K * np.exp(-r * T) * norm.cdf(-d2))     
    else:
        raise ValueError(f"option_type must be 'call' or 'put', got '{option_price}'")  

    return theta

def black_scholes_rho(S, K, r, sigma, T, option_price='call'):
    d1 = (np.log(S/K) + (r + ((sigma ** 2) / 2)) * T ) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))

    if option_price == 'call':
        rho = (K * T * np.exp(-r * T) * norm.cdf(d2))
    elif option_price == 'put':
        rho = (-K * T * np.exp(-r * T) * norm.cdf(-d2))
    else:
        raise ValueError(f"option_type must be 'call' or 'put', got '{option_price}'")  
    return rho
