import streamlit as st

st.title('Pumped Storage Hydropower Energy Model App')

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
upper_reservoir_level = st.number_input('Upper Reservoir Level (m)', value=10000.0)  # meters
lower_reservoir_level = st.number_input('Lower Reservoir Level (m)', value=2000.0)  # meters
upper_reservoir_volume = st.number_input('Upper Reservoir Volume (cubic meters)', value=120000.0)  # cubic meters
lower_reservoir_volume = st.number_input('Lower Reservoir Volume (cubic meters)', value=40000.0)  # cubic meters
pump_efficiency = st.number_input('Pump Efficiency (decimal)', value=0.8)  # decimal
generator_efficiency = st.number_input('Generator Efficiency (decimal)', value=0.9)  # decimal

if st.button('Calculate'):
    # calculate the net head and overall efficiency
    net_head = upper_reservoir_level - lower_reservoir_level  # meters
    overall_efficiency = pump_efficiency * generator_efficiency

    # calculate the available energy
    available_energy = ((upper_reservoir_volume - lower_reservoir_volume) * net_head * water_density * gravity * overall_efficiency) / 3600 / 1000 # MWh

    # print variables and results for debugging
    st.markdown(f"### Input variables:")
    st.markdown(f"- Upper reservoir level: {upper_reservoir_level} m")
    st.markdown(f"- Lower reservoir level: {lower_reservoir_level} m")
    st.markdown(f"- Upper reservoir volume: {upper_reservoir_volume} m³")
    st.markdown(f"- Lower reservoir volume: {lower_reservoir_volume} m³")
    st.markdown(f"- Pump efficiency: {pump_efficiency}")
    st.markdown(f"- Generator efficiency: {generator_efficiency}")

    st.markdown(f"### Calculations:")
    st.markdown(f"- Net head: {net_head} m")
    st.markdown(f"- Overall efficiency: {overall_efficiency}")
    st.markdown(f"- Available energy: {available_energy} MWh")

    # format available energy to one decimal place
    formatted_energy = "{:.1f}".format(available_energy)

    # display the available energy
    st.markdown(f'### Available Energy: {formatted_energy} MWh')
