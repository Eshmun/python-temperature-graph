import pandas as pd
import matplotlib.pyplot as plt


# Import CSV
df = pd.read_csv("data.csv")
# select desired column
state = df['state']
# Convert no numeric data and drop rows containing NaN
state = pd.to_numeric(state, errors='coerce').dropna()

# state = state.reset_index(drop=True)
# Apply moving average filter
state_filtered = state.rolling(window=10, center=False).mean()
# Calculate the slope over 60 sec
state_slope = state_filtered.rolling(6).apply(lambda x: x[-1]-x[0])

# m2
room_size = 42.5
# kg/m2
density_air = 1.2041
# specific heat capacity of air (cp) J/kg/K
specific_heat_cap = 1012
# Calculating the heat capacity
heat_cap = room_size*density_air*specific_heat_cap
# Divide by 60 to get J/s
state_slope_power = (state_slope/60)*heat_cap

#plot and show
#plt.plot(state_filtered)
plt.plot(state_slope_power)
plt.show()
