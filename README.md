# An Epidemic Model Analyzing Social Distancing

Social distancing is being attempted to limit the impact of the coronavirus, but little has been done to ensure that social distancing of this kind will be safe and effective.

## Models
- [Basic SEIR model](https://github.com/dgoldman0/socialdistancing/blob/master/seir.py)
- [Inclusion of low and high risk categories](https://github.com/dgoldman0/socialdistancing/blob/master/seir2.py)
- [Analysis of curves varying the level of social distancing of low risk group](https://github.com/dgoldman0/socialdistancing/blob/master/seir3.py)
- [Analysis of relative mortality rates at varying levels of social distancing](https://github.com/dgoldman0/socialdistancing/blob/master/seir4.py)
- [Final analysis incorporating healthcare resource overload and specific estimated parameters](https://github.com/dgoldman0/socialdistancing/blob/master/seir5.py)

## Data Sources and Estimates

## Hospital Bed Capacity

Hospital bed capacity is estimated based on figures from [COVIDACTNOW](https://covidactnow.org/). The model assumes that there are roughly enough hospital beds for 0.22% of the population, with 60% capacity, and an emergency capacity build of roughly 200%. As a conservative estimate, I chose 0.1% for my capacity limit.

## Case Fatality Rate

The case fatality rate estimates are all over the board, and seem to vary based on the quality of the health care system, the age of the patient, and so on. Mortality seems to be orders of magnitude higher in at risk populations compared to low risk populations. COVIDACTNOW estimates a case fatality rate of 1.1% with an additional 1% if hospitals are overburdened.

More data is coming in all the time, and I will be able to update my models accordingly as it does, but for now, I've estimated a case fatality rate of 0.1% for low risk populations and 10% for high risk populations.

Assuming that being over-capacity increases the risk of death among the low risk population by 50% and the high risk by 200%, that would yield a case fatality rate of 0.15% and 30% respectively.

## Estimate of Social Distancing Timing

The first case of SARS-CoV-2, within the United States was identified on January 7th, 2020 ([Holshue et al. 2020](https://www.nejm.org/doi/full/10.1056/NEJMoa2001191)). Lockdown orders began going into effect roughly 60 days later. This is used as the estimated start time. A more complex model might include a rolling social distancing process, where the degree of social distancing increases over time. The fifth and final model estimates an approximate lockdown period of 90 days.

Two versions of the model were run. The first uses the 60 day estimate, while the second looks at a rapid lockdown within 15 days of the infection.

## Analysis

The first of the two figures is an analysis varying rho from 0.2 to 1.5 and assumes a lockdown within 15 days, and lasting for 90. Under this scenario, the minimum fatality rate was 0.058%, with the most reduction occuring with a rho of roughly 0.7, or roughly a 30% reduction in contact rate.

![Graphical Analysis: Delayed Lockdown](/Figure_1.png "Delayed Lockdown")

---

The second figure uses the same values of rho, but assumes that it takes 57 days for the lockdown to begin. Under this scenario, the minimum fatality rate was 0.084%. There was little difference between minimum and maximum fatality rates.

![Graphical Analysis: Delayed Lockdown](/Figure_2.png "Delayed Lockdown")

## Summary

While a degree of social distancing seems to be effective at flattening the curve, extreme social distancing simply delays the progression of the epidemic. Furthermore, certain parameters can actually increase the overall mortality level.

The most effective option seems to be to increase social distancing for at risk, and between low and high risk populations. A reduction in contact rate of more than 50% for the low risk population does not seem reasonable, based on the model evaluation. Furthermore, there seems to be little effect if these changes aren't implemented in the first couple of weeks.

## Additional Info
More information can be found at [The Potential Success and Failures of Social Distancing](https://vocal.media/longevity/the-potential-success-and-failures-of-social-distancing)
