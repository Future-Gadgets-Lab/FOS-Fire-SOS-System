# FOS: Fire SOS System
## Problem Statement

Large fire outbreaks causes chaos and there is no presence of any information system for the public as well as firefighters

There are no updates on micro level of safe and non-safe paths in case of fires other than intuition. Path planning is absent.

The news deliver the fire spread information using satellite data. FIRMS data by NASA takes up 3-5 hours to get updated on average. This causes fatal delays in crucial information.
Information gathering starts only after the fire trucks and personnel reach, which wastes additional time.


## Proposed Solution

We propose a multi-modal real-time fire information system which gathers real-time updates from – NASA Satellite data MODIS and VIIRS, data from crowd sourcing and Grid based information by Unmanned Aerial Vehicles.
We propose an application which allows users to call SOS button on fire distress, which also acts as the information source for the fire departments.

A drone is dispatched consequently (complementary to the fire rescuers) to give data on number of pedestrians trapped along with a grid-map of where they are stuck along with the data on fire spread, using Machine Learning algorithms running on the edge
Based on this data, a real-time fire-map as well as inferenced escape routes are made available to the public as well as the fire-departments.

### Flowchart

![alt text](https://raw.githubusercontent.com/chetanchawla/FOS-Fire-SOS-System/master/flow.png)

## Android Application :

It has 2 modules-

### Fire Rescue

SOS button sends severity and spread of fire information to the firebase server connected to nearest fire department, which in turn dispatches a drone and its personnel according to the distance. The drone, and crowd sourced information along with satellite data helps in making fire spread map and rescue paths as well as inform about pedestrians stuck in different grids of the whole area

### Post Effects

A beacon system based on bluetooth connectivity is used to inform the fire rescuers in case one is stuck. It employs an algorithm which senses the closeness of the stuck person to the rescuers and guide them consequently, by vibration alerts. The distance is also specified as accurate values in meters ( to about 5 decimal places). This helps in relieving the post effects of the fire catastrophe. 

Fundraising for any tragedy using decentralized platform is integrated within the app that allows to raise funds for the areas suffering calamities powered by security and transparency of blockchain.  It not only sends the amount to the right person in authority but also ensures the sense of belief that his money is used for the right purpose. The whole of smart contract and contract page can be seen any instance to ensure the transaction was successful.  We are using the states ranking to have a healthy competition amongst states too. The donation amount can be withdrawn by only 4 persons (decided at the time of deployment) who are in commanding officers of that rescue team. 
Comparison and Applications

The existing methods of fire-reporting uses satellite data, such as in FIRMS, which is extremely unreliable as it gets updated in 3-5 hours.

Other ways of fighting fire includes slower fire-trucks which does not leave enough time for scenario analysis and thus, the rescue operation often relies only on intuition of directions and routes along with survivors.
Thus, the proposed system finds its way to help make public aware of safe routes to follow, help fire-teams employ a faster way of data collection and reduces entropy in rescuing operation, and helps people to get post catastrophe help as well as give them tips and one button emergency contacts as side features.

