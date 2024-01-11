# Import necessary libraries
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
poverty_data = pd.read_csv(r'C:\Users\ACER\Downloads\poverty_data.csv')
violence_data = pd.read_csv(r'C:\Users\ACER\Downloads\violent_data.csv')
cepi_data = pd.read_csv(r"C:\Users\ACER\Downloads\cepi_data.csv")
mental_health_data = pd.read_csv(r"C:\Users\ACER\Downloads\mental_health_data.csv")

# Creative Header
st.markdown(
    """
    # 🌈 Explore Social and Environmental Data in India 🌏

    Welcome to the Data Exploration App! This app allows you to dive into various aspects of India's social and environmental landscape.

    Select different options from the sidebar to visualize data on poverty, violence, environmental pollution, and mental health.

    Have a great exploration journey! 🚀
    """
)


# Sidebar for user input
st.sidebar.title('Explore Social and Environmental Data in India')

# Select data to display
selected_data = st.sidebar.multiselect('Select Data:', ['Poverty', 'Violence', 'Environmental Pollution', 'Mental Health','The State of Mental and Emotional Wellbeing in India'])

# Display selected data
if 'Poverty' in selected_data:
    st.header('State-wise Poverty in India (2011-12)')
    st.header('Total Percentage of Persons Below Poverty Line in Each State')

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='State', y='Total - Percentage of Persons', data=poverty_data, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    ax.set_title('Total Percentage of Persons Below Poverty Line in Each State')
    ax.set_xlabel('State')
    ax.set_ylabel('Percentage of Persons Below Poverty Line')
    st.pyplot(fig)
    # Add your poverty visualizations here
    # Example for poverty_data visualization
    # Display subplots for multiple features
    st.header('Poverty Data Visualization')

    features = ['Rural - Percentage of Persons', 'Urban - Percentage of Persons', 'Total - Percentage of Persons']

    fig, axes = plt.subplots(nrows=len(features), ncols=1, figsize=(12, 6 * len(features)))

    for i, feature in enumerate(features):
        sns.barplot(x='State', y=feature, data=poverty_data, ax=axes[i])
        axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=45, ha='right')
        axes[i].set_title(f'{feature} in Each State')
        axes[i].set_xlabel('State')
        axes[i].set_ylabel(f'{feature}')

    plt.tight_layout()
    st.pyplot(fig)


if 'Violence' in selected_data:
    st.header('Incidents of Violence by Anti National Elements (2018)')
    # Add your violence visualizations here
    # Clean the data by removing rows with more than or equal to two zero values
    cleaned_data = violence_data.dropna(thresh=len(violence_data.columns) - 2)

    # Sidebar for user input
    st.sidebar.title('Explore Violence Data in India')

    # Select feature for visualization from cleaned data
    selected_feature = st.sidebar.selectbox('Select Feature:', cleaned_data.columns[1:])

    # Display barplot for the selected feature from cleaned data
    st.header(f'Visualization of {selected_feature} in Cleaned Data')

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='Type-region', y=selected_feature, data=cleaned_data, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    ax.set_title(f'{selected_feature} across Different Regions (Cleaned Data)')
    ax.set_xlabel('Type-region')
    ax.set_ylabel(selected_feature)
    st.pyplot(fig)
    
    
    
    
    
if 'Environmental Pollution' in selected_data:
    st.header('Environmental Pollution Index in Critically Polluted Areas (CEPI)')
    # Add your CEPI visualizations here
    # Display the original dataset
    st.subheader('Original CEPI Data:')
    st.write(cepi_data.head())

    # Clean the data by removing rows with more than or equal to two zero values
    cleaned_cepi_data = cepi_data.dropna(thresh=len(cepi_data.columns) - 2)

    # Display the cleaned dataset
    st.subheader('Cleaned CEPI Data:')
    st.write(cleaned_cepi_data.head())

    # Sidebar for user input
    st.sidebar.title('Explore CEPI Data in India')

    # Select features for visualization from cleaned data
    selected_features_cepi = st.sidebar.multiselect('Select Features:', cleaned_cepi_data.columns[1:])

    # Option to show the graph indicating the highest CEPI SCORE
    show_highest_cepi_graph = st.sidebar.checkbox('Show Graph for Highest CEPI SCORE')

    # Display barplot for the selected features from cleaned data
    st.header('Visualizations for Selected Features in Cleaned CEPI Data')

    # Check if selected_features_cepi is not empty
    if selected_features_cepi:
        for feature in selected_features_cepi:
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.barplot(x='Area', y=feature, hue='Status of Moratorium', data=cleaned_cepi_data, ax=ax)
            ax.set_xticks(range(len(cleaned_cepi_data['Area'])))  # Set ticks first
            ax.set_xticklabels(cleaned_cepi_data['Area'], rotation=45, ha='right')  # Rotate x-axis labels for better visibility
            ax.set_title(f'{feature} across Different Areas by Moratorium Status (Cleaned CEPI Data)')
            ax.set_xlabel('Area')
            ax.set_ylabel(feature)
            st.pyplot(fig)

    # Check if the user wants to show the graph for the highest CEPI SCORE
    if show_highest_cepi_graph:
        cepi_scores_features = ['CEPI SCORE-2009', 'CEPI SCORE-2011', 'CEPI SCORE-2013']
        highest_cepi_scores = cleaned_cepi_data[cepi_scores_features].max(axis=1)
        highest_cepi_scores.index = cleaned_cepi_data['State']

        fig, ax = plt.subplots(figsize=(12, 8))
        sns.barplot(x=highest_cepi_scores.index, y=highest_cepi_scores, ax=ax)
        ax.set_xticks(range(len(highest_cepi_scores.index)))  # Set ticks first
        ax.set_xticklabels(highest_cepi_scores.index, rotation=45, ha='right')  # Rotate x-axis labels for better visibility
        ax.set_title('Highest CEPI SCORE across Different Years for Each State (Cleaned CEPI Data)')
        ax.set_xlabel('State')
        ax.set_ylabel('Highest CEPI SCORE')
        st.pyplot(fig)
   
    
if 'Mental Health' in selected_data:
    st.header('Distribution of Inmates with Mental Illness (2001-2012)')
    # Add your mental health visualizations here
    # Display the original dataset
    st.subheader('Original Mental Health Data:')
    st.write(mental_health_data.head())

    # Clean the data by removing rows where every element is 0
    cleaned_mental_health_data = mental_health_data[(mental_health_data.iloc[:, 2:] != 0).any(axis=1)]

    # Display the cleaned dataset
    st.subheader('Cleaned Mental Health Data:')
    st.write(cleaned_mental_health_data.head())

    # Sidebar for user input
    st.sidebar.title('Explore Mental Health Data in India')

    # Select features for visualization from cleaned data
    selected_features_mental_health = st.sidebar.multiselect('Select Features:', cleaned_mental_health_data.columns[2:])

    # Display barplot for the selected features from cleaned data
    st.header('Visualizations for Selected Features in Cleaned Mental Health Data')

    # Check if selected_features_mental_health is not empty
    if selected_features_mental_health:
        for feature in selected_features_mental_health:
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.barplot(x='YEAR', y=feature, hue='STATE/UT', data=cleaned_mental_health_data, ax=ax)
            ax.set_xticks(range(len(cleaned_mental_health_data['YEAR'].unique())))  # Set ticks first
            ax.set_xticklabels(cleaned_mental_health_data['YEAR'].unique(), rotation=45, ha='right')  # Rotate x-axis labels for better visibility
            ax.set_title(f'{feature} across Different States/UTs over the Years (Cleaned Mental Health Data)')
            ax.set_xlabel('Year')
            ax.set_ylabel(feature)
            st.pyplot(fig)

# Display selected data
if  'The State of Mental and Emotional Wellbeing in India' in selected_data:
    # Display relevant output about the state of mental and emotional wellbeing
    st.header('State of Mental and Emotional Wellbeing in India')
    # Analyze mental health data
    total_convicts = mental_health_data['Total Convicts'].sum()
    total_under_trial = mental_health_data['Total Under trial'].sum()
    total_detenues = mental_health_data['Total Detenues'].sum()

    st.write(f'Total Convicts: {total_convicts}')
    st.write(f'Total Under Trial: {total_under_trial}')
    st.write(f'Total Detenues: {total_detenues}')

    # Generate a bar graph for the state of male or female using features of mental health dataset
    st.header('Bar Graph: State of Male or Female in Mental Health Data')

    # Sidebar for user input
    st.sidebar.title('Explore Mental Health Data in India')

    # Select gender for visualization
    selected_gender = st.sidebar.selectbox('Select Gender:', ['Male', 'Female'])

    # Display barplot for the selected gender from mental health data
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(x='YEAR', y=f'{selected_gender} Convicts', hue='STATE/UT', data=mental_health_data, ax=ax)
    ax.set_xticks(range(len(mental_health_data['YEAR'].unique())))  # Set ticks first
    ax.set_xticklabels(mental_health_data['YEAR'].unique(), rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    ax.set_title(f'State of {selected_gender} in Mental Health Data across Different States/UTs over the Years')
    ax.set_xlabel('Year')
    ax.set_ylabel(f'{selected_gender} Convicts')
    st.pyplot(fig)
