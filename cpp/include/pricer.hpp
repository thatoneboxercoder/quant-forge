#ifndef PRICER_HPP
#define PRICER_HPP

#include <string>
#include <iostream>

using namespace std;

double black_scholes_price(
    double S,
    double K,
    double r, 
    double sigma,
    double T,
    string option_type = "call" 
);

double black_scholes_delta(
    double S,
    double K, 
    double r,
    double sigma,
    double T,
    string option_type 
);

double black_scholes_gamma(
    double S,
    double K, 
    double r,
    double sigma,
    double T 
);

double black_scholes_vega(
    double S,
    double K, 
    double r,
    double sigma,
    double T 
);

double black_scholes_theta(
    double S,
    double K, 
    double r,
    double sigma,
    double T,
    string option_type
);

double black_scholes_rho(
    double S,
    double K, 
    double r,
    double sigma,
    double T,
    string option_type
);

double norm_cdf(double x);
double norm_pdf(double x);

#endif
