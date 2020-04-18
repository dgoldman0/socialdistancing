# Rolling Social Distancing Efforts

The initial analysis described in this project suggests that extreme social distancing efforts are ineffective unless maintained indefinitely. Moderate social distancing efforts can be maintained for as long as they need to be, however, these extreme measures appear to be quite brittle. Aside from the economic devastation, and in part because of it, these measures are resulting in societal unrest. While still small at the time of writing, the number of protests are growing. And according to [CNN](https://www.cnn.com/2020/04/10/us/disaster-hotline-call-increase-wellness-trnd/index.html), March 2020 saw a 338% increase in calls to suicide hotlines, leading to more than an 800% increase in calls in March, year over year. Sadly, all of this unrest may be just the beginning if social distancing isn't relaxed soon.

# Voluntary Cyclical Social Distancing

Rather than implementing a stay-at-home orders around the country, and around the world, there may be a better solution. This solution relies on wide scale surveillance of the epidemic and distribution of that information to a wide audience. Thankfully, modern technology, including broadcast media and the internet, allow for easy distribution of current figures of the COVID-19 epidemic. Indeed, we are already being bombarded with information about the ongoing "crisis" through these channels.

## The Model

The model used for this analysis can be found in [seir6.py](https://github.com/dgoldman0/socialdistancing/blob/master/seir6.py) and was made by modifying the model found in [seir2.py](https://github.com/dgoldman0/socialdistancing/blob/master/seir2.py). Rather than starting and stopping the social distancing at a fixed time, a 14 day rolling average for the infection rate was calculated. Whenever this average was above the set threshold, social distancing would engage. This dynamic models the voluntary social distancing resulting from reporting. The more social foundations put into place to make it easier to adjust social distancing on a daily or weekly basis, the closer this model will fit reality.

The model analysis assumes more extreme social distancing than the roughly 50% reduction suggested in other models. I justify this assumption by the voluntary and cyclical nature of the distancing. When force is applied, people will push back and defy orders. The voluntary nature of the measure should reduce the pushback. Additionally, since people know that the measure will not be maintained indefinitely, and because they can understand how the decision to distance is being made, the distancing will be less stressful.

And so, this model assumes that a distancing of 60% for the low risk population, and 75% distancing for the high risk population and between the low and high risk populations will occur, whenever the 14 day rolling average of infections is greater than 1% of the population.

## Results

There was an initial ramping up of the infection as the rolling average moved towards the 1% rate. Once it reached that rate, social distancing was engaged six times during the outbreak period. Adjusting seir2.py to the distancing values used in seir6.py, a peak infection rate within the low risk population was roughly 7.6% and occurred on day 91, showing a post-relaxation spike (relaxation occurred on day 50). However, for the cyclical model, the maximum infection rate occurred a little after day 40, and the maximum infection rate within the low risk population was only 2.4%, which indicates that a prolonged cyclical distancing effort can be far more effective than a short term continuous distancing effort of the same severity. Below is a graphical result showing total population statistics for susceptible, exposed, infected, recovered, and dead, as well as the rolling average. 

![Graphical Analysis: Cyclical Distancing](/Figure_3.png "Cyclical Distancing")

# The New Normal

A lot of talk has been mentioned about a "new normal" resulting from the COVID-19 epidemic. This information can be utilized to help create that new normal, with limited negative impact to our lives. While it may be too late to implement such a solution, now that such extreme measures have been taken for COVID-19, this information can be useful in informing future public health policy.

## Infection Reporting

Consider an altered version of this model that utilizes an aggregate measure of infectious disease load. This model can produce a single metric that can be released daily, much like a daily weather report. Based on this figure, people can plan the next few days accordingly. Over time, especially with proper education, this system could be used to help reduce infectious load across coronaviruses influenza, and others.

Of course, there is a question of who should be responsible for the reporting, and how trustworthy that reporting is. However, crowd based wisdom is more powerful than one might think. It may not be a perfect system, but it should be fairly effective. Moreover, it is a voluntary system, which is the only system that is viable in public health, especially in the absence of scientific justification for a protocol.

## Core "Distancing"

While a lot of the social distancing effort will have to be temporary, there are some core social distancing efforts that should always be maintained. Here, social distancing does not have to be a physical distancing, but any reduction in the potential transmission rate due to non-pharmaceutical means. It includes physical distancing, reduction in contact rate, but also includes better sanitation and hygiene. It includes making sure that if a person feels sick, they stay at home. It means a change in how accepting employers are to employees calling in sick. These changes are in many way common sense changes and are provisions that should already be in place. Therefore they are a core distancing measures that should be permanent.

These core measures are already being implemented, in addition to the shelter-in-place orders being issued around the world. They have a very limited negative impact on our daily lives, but can significantly reduce the spread of infectious disease. Taking these measures into account, the added social distancing effort needed would be greatly reduced to generate the net effective distancing coefficients discussed earlier.
