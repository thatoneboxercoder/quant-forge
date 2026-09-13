#include "pricer.hpp"
#include <iostream>
#include <string>
#include <cmath>
#include <stdexcept>

using namespace std;

double norm_cdf(double x){

    return 0.5 * erfc(-x / sqrt(2));

}

double norm_pdf(double x){

    const double PI = 3.14159265358979;

    return (1/(sqrt(2 * PI))) * exp((-x * x) / 2);

}

double black_scholes_price(
    double S,
    double K, 
    double r,
    double sigma,
    double T,
    string option_type 
){
    double d1 = (log(S/K) + (r + (sigma * sigma)/2) * T) / (sigma * sqrt(T));
    double d2 = d1 - (sigma * sqrt(T));

    if (option_type == "call"){

        double price = (S * norm_cdf(d1)) - (K * exp(-r * T) * norm_cdf(d2));

        return price;

    }
    else if (option_type == "put"){

        double price = (K * exp(-r * T) * (norm_cdf(-d2))) - (S * norm_cdf(-d1));

        return price;

    }
    else {

        throw invalid_argument("option type must be 'call' or 'put' ");

    }


}

double black_scholes_delta(
    double S,
    double K, 
    double r,
    double sigma,
    double T,
    string option_type 
){

    double d1 = (log(S/K) + (r + (sigma * sigma)/2) * T) / (sigma * sqrt(T));

    if(option_type == "call"){

        double delta = norm_cdf(d1);

        return delta;

    }
    else if (option_type == "put"){

        double delta = norm_cdf(d1) - 1;

        return delta;

    }
    else{

        throw invalid_argument("option type must be 'call' or 'put'");

    }

}

double black_scholes_gamma(
    double S,
    double K, 
    double r,
    double sigma,
    double T 
){
    double d1 = (log(S/K) + (r + (sigma * sigma)/2) * T) / (sigma * sqrt(T));

    double gamma = norm_pdf(d1) / (S * sigma * sqrt(T));

    return gamma;
}

double black_scholes_vega(
    double S,
    double K, 
    double r,
    double sigma,
    double T 
){

    double d1 = (log(S/K) + (r + (sigma * sigma)/2) * T) / (sigma * sqrt(T));

    double vega = (S * norm_pdf(d1) * sqrt(T));

    return vega;

}

double black_scholes_theta(
    double S,
    double K, 
    double r,
    double sigma,
    double T,
    string option_type
){

   double d1 = (log(S/K) + (r + (sigma * sigma)/2) * T) / (sigma * sqrt(T));
   double d2 = d1 - (sigma * sqrt(T));
   if (option_type == "call"){

    double theta = -((S * norm_pdf(d1) * sigma) / (2 * sqrt(T)))
        - (r * K * exp(-r * T) * norm_cdf(d2));

    return theta;

   }
   else if (option_type == "put"){

    double theta = -((S * norm_pdf(d1) * sigma) / (2 * sqrt(T)))
        + (r * K * exp(-r * T) * norm_cdf(-d2));

    return theta;

   }
   else{

    throw invalid_argument("option type must be 'call' or 'pull'");

   }

}

double black_scholes_rho(
    double S,
    double K, 
    double r,
    double sigma,
    double T,
    string option_type
){
   
   double d1 = (log(S/K) + (r + (sigma * sigma)/2) * T) / (sigma * sqrt(T));
   double d2 = d1 - (sigma * sqrt(T));

   if(option_type == "call"){

    double rho = (K * T * exp(-r * T) * norm_cdf(d2));

    return rho;

   }
   else if (option_type == "put"){

    double rho = (-K * T * exp(-r * T) * norm_cdf(-d2));

    return rho;

   }
   else{

    throw invalid_argument("option type must be 'call' or 'put'");

   }

}


