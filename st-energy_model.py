import streamlit as st

st.title('Energy Model App')

st.markdown("""
This app calculates the available energy (in MWh) in a hypothetical reservoir system. 
The user provides parameters such as the levels and volumes of the upper and lower reservoirs, 
as well as the pump and generator efficiency values. The app then calculates and displays the 
net head, overall efficiency, and the available energy. Enter the values below and click 'Calculate' 
to see the results.
""")

# constants
water_density = 1000  # kg/m³
gravity = 9.81  # m/s²

# get inputs from the user
upper_reservoir_level = st.number_input('Upper Reservoir Level (m)', value=0.0)  # meters
lower_reservoir_level = st.number_input('Lower Reservoir Level (m)', value=0.0)  # meters
upper_reservoir_volume = st.number_input('Upper Reservoir Volume (cubic meters)', value=0.0)  # cubic meters
lower_reservoir_volume = st.number_input('Lower Reservoir Volume (cubic meters)', value=0.0)  # cubic meters
pump_efficiency = st.number_input('Pump Efficiency (decimal)', value=0.0)  # decimal
generator_efficiency = st.number_input('Generator Efficiency (decimal)', value=0.0)  # decimal

if st.button('Calculate'):
    # calculate the net head and overall efficiency
    net_head = upper_reservoir_level - lower_reservoir_level  # meters
    overall_efficiency = pump_efficiency * generator_efficiency

    # calculate the available energy
    available_energy = ((upper_reservoir_volume - lower_reservoir_volume) * net_head * water_density * gravity * overall_efficiency) / 3600 / 1000 # MWh

    # print variables and results for debugging
    st.write(f"Input variables:\nUpper reservoir level: {upper_reservoir_level} m\nLower reservoir level: {lower_reservoir_level} m\nUpper reservoir volume: {upper_reservoir_volume} m³\nLower reservoir volume: {lower_reservoir_volume} m³\nPump efficiency: {pump_efficiency}\nGenerator efficiency: {generator_efficiency}")
    st.write(f"Calculations:\nNet head: {net_head} m\nOverall efficiency: {overall_efficiency}\nAvailable energy: {available_energy} MWh")

    # format available energy to one decimal place
    formatted_energy = "{:.1f}".format(available_energy)

    # display the available energy
    st.write(f'Available Energy: {formatted_energy} MWh')
