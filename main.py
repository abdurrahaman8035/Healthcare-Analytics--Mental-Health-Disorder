import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import altair as alt

# Load the data
df = pd.read_csv("prevalence-by-mental-and-substance-use-disorder.csv")
df1 = pd.read_csv("share-with-mental-and-substance-disorders.csv")
df2 = pd.read_csv("share-with-mental-or-substance-disorders-by-sex.csv")
df3=pd.read_csv("dalys-mental-illnesses-age-standardized.csv")
df4=pd.read_csv("mental-and-substance-use-as-share-of-disease.csv")
df5=pd.read_csv("number-of-people-with-bipolar-disorder.csv")
df6=pd.read_csv("number-of-people-with-depression.csv")
df7=pd.read_csv("number-with-an-eating-disorder.csv")
df8=pd.read_csv("number-with-anxiety-disorders.csv")
df9=pd.read_csv("number-with-schizophrenia.csv")
df10=pd.read_csv("Dalys by age.csv")
df11=pd.read_csv("suicide-rates-vs-prevalence-of-mental-and-substance-use-disorders.csv")



st.set_page_config(layout="wide", page_title=None)

tab1, tab2= st.tabs(["📈 Overview", "Demographic"])

with tab1:

    st.subheader("Estimates of People Suffering from Mental Health Illnesses")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("<h6 style='color: red;'>Anxiety Disorders</h6>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: red;'>301.39 M</h3>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h6 style='color: red;'>Depressive Disorders</h6>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: red;'>279.61 M</h3>", unsafe_allow_html=True)

    with col3:
        st.markdown("<h6 style='color: red;'>Bipolar Disorders</h6>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: red;'>39.55 M</h3>", unsafe_allow_html=True)

    with col4:
        st.markdown("<h6 style='color: red;'>Schizophrenia</h6>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: red;'>23.6 M</h3>", unsafe_allow_html=True)

    with col5:
        st.markdown("<h6 style='color: red;'>Eating Disorders</h6>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: red;'>13.63 M</h3>", unsafe_allow_html=True)

    st.subheader("")
  
    st.write(" Select Country and type of mental Disorder to view the prevalance of each Disorder over time and the total overview of mental health illness for each country upon selection")

    country = st.selectbox("Select Country", df['Entity'].unique())


    filtered_data = df[df['Entity'] == country]



    # Create two columns using st.beta_columns()
    col1, col2 = st.columns(2)

    # Plot line chart in the first column
    with col1:
        tab = st.selectbox("Select Disorder", ('Schizophrenia disorders', 'Bipolar disorders', 'Eating disorders', 'Anxiety disorders',
                                       'Drug use disorders', 'Depressive disorders', 'Alcohol use disorders'))
        st.subheader(f"Prevalence of {tab} in {country}")
        fig, ax = plt.subplots()
        ax.plot(filtered_data['Year'], filtered_data[tab])
        ax.set(xlabel='Year', ylabel='Prevalence', title=f"{tab} Prevalence Over Time")
        ax.grid()

    # Display line chart
        st.pyplot(fig)

# DALYS bar chart
    with col2:
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader(f'Overview of the prevelence of all mental illness in {country}')

        # Filter data based on selections
        df3_filtered = df3[df3['Entity'] == country].copy()
        # Filter DataFrame to include only rows where 'Entity' is 'World'
        df_world = df[df['Entity'] == country].copy()

        # Disorders list
        disorders = ['Schizophrenia disorders', 'Bipolar disorders', 'Eating disorders', 'Anxiety disorders',
                                        'Drug use disorders', 'Depressive disorders']

        # Reformat the DataFrame from wide to long format
        long_df = df_world.melt(id_vars='Year', value_vars=disorders, var_name='Disorder', value_name='Prevalence')
        # Create an animated horizontal bar chart
        fig = px.bar(long_df,
                    y='Disorder',  # Swap x and y
                    x='Prevalence',
                    animation_frame='Year', 
                    color='Disorder',
                    title="Prevalence of Disorders Over Time (World)",
                    labels={'Prevalence':'Prevalence', 'Disorder':'Disorder', 'Year':'Year'},
                    text='Prevalence')  # Display Prevalence values next to the bars

        fig.update_traces(texttemplate='%{text:.2s}', textposition='inside')  # Configure text
        fig.update_layout(autosize=False, width=800, height=600)  # Here, specify your desired width and height values

        st.plotly_chart(fig, use_container_width=True)

       

        # Convert Year to string using .loc
        #df3_filtered.loc[:, 'Year'] = df3_filtered['Year'].astype(str)

        # Melting the DataFrame to have disorders and DALYs in two separate columns
        #df3_filtered = df3_filtered.melt(id_vars=['Entity', 'Code', 'Year'], 
         #                               value_vars=['DALYs Anxiety disorders', 'DALYs  Schizophrenia ', 
          #                                          'DALYs Anxiety disorders', 'DALYs  Eating disorders ', 
           #                                         'DALYs Bipolar disorder '],
            #                            var_name='Disorder', 
             #                           value_name='DALYs')

        # Create a horizontal bar chart using Plotly with animation
        #fig4 = px.bar(df3_filtered, 
         #           x='DALYs', 
          #          y='Disorder', 
           #         labels={'DALYs': 'DALYs', 'Disorder': 'Disorder'},
            #        orientation='h',
             #       animation_frame='Year',
              #      range_x=[df3_filtered['DALYs'].min(), df3_filtered['DALYs'].max()])  # Display the values on the side of the bars

        # Remove the color legend
        #fig4.update_traces(showlegend=False)

        # Hide the x-axis
        #fig4.update_xaxes(showline=False, showticklabels=False)

    # Adjust the size of the plot
        #fig4.update_layout(
         #   autosize=False,
          #  width=700,  # Adjust as needed
           # height=500,  # Adjust as needed
            #title={'text': 'DALYs by disorder over time',
            
             #   'y':1,
              #  'x':0.3,
               # 'xanchor': 'center',
                #'yanchor': 'top'
            #}
        #)

        #st.plotly_chart(fig4)

# Doing Chloropleth world map
# Creating the Choropleth map with animation over the years
    st.subheader("Burder of Diseases in DALYS Globally of Mental Health Illnesses")
    fig = px.choropleth(
    df4, 
    locations='Code',
    locationmode='ISO-3',
    color='DALYs (Disability-Adjusted Life Years) - Mental disorders - Sex: Both - Age: All Ages (Percent)',
    hover_name='Entity',
    animation_frame='Year',  # animation over the years
    color_continuous_scale=px.colors.sequential.Plasma,
    title='DALYs Mental Disorders (%) Over the Years',
    height=600  # adjust as needed
    )
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000  # set the duration of the transition between frames
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 500  # set the duration of the transition between frames

    st.plotly_chart(fig, use_container_width=True)  # make the plot use the full container width

    


with tab2:
    st.subheader("Exploring the Demographic Landscape of Mental Health Disorders Prevalence among Males and Females")

    # Group the data by continent and calculate average values
    df2_agg = df2.groupby('Continent').agg({
        'Prevalence - Mental and substance use disorders - Sex: Male - Age: Age-standardized (Percent)': 'mean',
        'Prevalence - Mental and substance use disorders - Sex: Female - Age: Age-standardized (Percent)': 'mean',
        'Population (historical estimates)': 'sum'
    }).reset_index()

    # Filter out rows with NaN values in 'Population (historical estimates)' column
    df2_agg_cleaned = df2_agg.dropna(subset=['Population (historical estimates)'])

    # Create two columns using beta_columns function
    col1, col2 = st.columns(2)

    # Plot the scatter plot using Plotly Express
    fig = px.scatter(df2_agg_cleaned,
                     x='Prevalence - Mental and substance use disorders - Sex: Male - Age: Age-standardized (Percent)',
                     y='Prevalence - Mental and substance use disorders - Sex: Female - Age: Age-standardized (Percent)',
                     size='Population (historical estimates)',
                     size_max=20,
                     color='Continent',
                     hover_data=['Continent', 'Population (historical estimates)'],
                     labels={'Prevalence - Mental and substance use disorders - Sex: Male - Age: Age-standardized (Percent)': 'Male Prevalence',
                             'Prevalence - Mental and substance use disorders - Sex: Female - Age: Age-standardized (Percent)': 'Female Prevalence',
                             'Population (historical estimates)': 'Population'},
                     title="Relevance of Mental and Substance Use Disorder Prevalence by Gender Accross Continents")

    # Display the scatter plot using Streamlit in the first column
    col1.plotly_chart(fig, use_container_width=True)

    # Group the data by Entity and calculate average values
    df2_agg_entity = df2.groupby('Entity').agg({
        'Prevalence - Mental and substance use disorders - Sex: Male - Age: Age-standardized (Percent)': 'mean',
        'Prevalence - Mental and substance use disorders - Sex: Female - Age: Age-standardized (Percent)': 'mean',
        'Population (historical estimates)': 'mean'
    }).reset_index()

    # Filter out rows with NaN values in 'Population (historical estimates)' column
    df2_agg_entity_cleaned = df2_agg_entity.dropna(subset=['Population (historical estimates)'])

    # Sort the dataframe by Male and Female Prevalence and get the top 30 countries
    df2_agg_entity_sorted = df2_agg_entity_cleaned.sort_values(by=['Prevalence - Mental and substance use disorders - Sex: Male - Age: Age-standardized (Percent)', 
                                                                   'Prevalence - Mental and substance use disorders - Sex: Female - Age: Age-standardized (Percent)'], ascending=False).head(30)

    # Plot the scatter plot using Plotly Express
    fig2 = px.scatter(df2_agg_entity_sorted,
                      x='Prevalence - Mental and substance use disorders - Sex: Male - Age: Age-standardized (Percent)',
                      y='Prevalence - Mental and substance use disorders - Sex: Female - Age: Age-standardized (Percent)',
                      size='Population (historical estimates)',
                      size_max=50,
                      color='Entity',
                     hover_data=['Entity', 'Population (historical estimates)'],
                      labels={'Prevalence - Mental and substance use disorders - Sex: Male - Age: Age-standardized (Percent)': 'Male Prevalence',
                              'Prevalence - Mental and substance use disorders - Sex: Female - Age: Age-standardized (Percent)': 'Female Prevalence',
                              'Population (historical estimates)': 'Population'},
                      title="Top 30 Countries-Relevance of Mental and Substance Use Disorder Prevalence by Gender")

    # Display the scatter plot using Streamlit in the second column
    col2.plotly_chart(fig2, use_container_width=True)

  # Create a columns layout
    col1, col2 = st.columns(2)
    # Assuming all your dataframes are in a dictionary
    dataframes = {
        'Bipolar disorder': df5,
        'Depressive disorders': df6,
        'Eating disorders': df7,
        'Anxiety disorders': df8,
        'Schizophrenia': df9
    }

    disorder_mapping = {
        'Bipolar disorder': 'Bipolar disorder',
        'Depressive disorders': 'Depressive disorders',
        'Eating disorders': 'Eating disorders',
        'Anxiety disorders': 'Anxiety disorders',
        'Schizophrenia': 'Schizophrenia'
    }
    col1.subheader('Prevalence of Mental illnesses based on Sex')
    # Create a select box for the disorder type
    selected_disorder = col1.selectbox('Select a Disorder Type', list(disorder_mapping.keys()))

    # Get the appropriate dataframe based on the selected disorder
    df = dataframes[selected_disorder]

    # Filter the data for the "World" entity
    df_world = df[df['Entity'] == 'World'].copy()

    # Create a new column for the total prevalence by summing the male and female values
    df_world.loc[:, 'Total Prevalence'] = df_world[
        [f'Prevalence - {disorder_mapping[selected_disorder]} - Sex: Male - Age: All Ages (Number)',
        f'Prevalence - {disorder_mapping[selected_disorder]} - Sex: Female - Age: All Ages (Number)']
    ].sum(axis=1)

    # Create a Streamlit app and add a title and a description
    
    col1.write(f'Line chart showing the prevalence of {selected_disorder.lower()} by gender in the World, with a shadow background and total prevalence.')

    # Create the line chart using Plotly Express
    fig = px.line(df_world, x='Year', y=[f'Prevalence - {disorder_mapping[selected_disorder]} - Sex: Male - Age: All Ages (Number)',
                                        f'Prevalence - {disorder_mapping[selected_disorder]} - Sex: Female - Age: All Ages (Number)',
                                        'Total Prevalence'],
                labels={'variable': 'Gender', 'value': 'Prevalence'},
                title=f'Prevalence of {selected_disorder} by Gender and Total')

    # Add a shadow background to the lines
    fig.update_traces(fill='tonexty')

    # Display the chart using Streamlit
    col1.plotly_chart(fig)

    # AGE DALYs
    
    # Define your categories
    categories = {
    'Depressive disorders': ['DALYs  Depressive - Under 5 (Rate)',
                             'DALYs  Depressive disorders - Age: 5-14 years (Rate)',
                             'DALYs  Depressive  - Age: 15-49 years (Rate)',
                             'DALYs  Depressive disorders - Age: 50-69 years (Rate)',
                             'DALYs Depressive disorders- Age: 70+ years (Rate)',
                             'DALYs Depressive disorders - Age: All Ages (Rate)',
                             'DALYs  Depressive disorders - Age: Age-standardized (Rate)'],
    'Eating disorders': ['DALYs Eating disorders - Age: 5-14 years (Rate)',
                         'DALYs Eating disorders - Both - Age: 15-49 years (Rate)',
                         'DALYs Eating disorders - Both - Age: All Ages (Rate)',
                         'DALYs Eating disorders -Age: Age-standardized (Rate)'],
    'Schizophrenia': ['DALYs Schizophrenia - Age: 5-14 years (Rate)',
                      'DALYs Schizophrenia -Age: 15-49 years (Rate)',
                      'DALYs Schizophrenia -Age: 50-69 years (Rate)',
                      'DALYs Schizophrenia -Age: 70+ years (Rate)',
                      'DALYs Schizophrenia - Age: All Ages (Rate)',
                      'DALYs  Schizophrenia - Age: Age-standardized (Rate)'],
    'Bipolar disorder': ['DALYs Bipolar disorder -Age: 5-14 years (Rate)',
                         'DALYs Bipolar disorder -Age: 15-49 years (Rate)',
                         'DALYs Bipolar disorder - Age: 50-69 years (Rate)',
                         'DALYs  Bipolar disorder  - Age: 70+ years (Rate)',
                         'DALYs Bipolar disorder -Age: All Ages (Rate)',
                         'DALYs Bipolar disorder - Age: Age-standardized (Rate)'],
    'Anxiety disorders': ['DALYs Anxiety disorders - Age: Under 5 (Rate)',
                          'DALYs  Anxiety disorders - Age: 5-14 years (Rate)',
                          'DALYs Anxiety disorders - Age: 15-49 years (Rate)',
                          'DALYs  - Anxiety disorders  - Age: 50-69 years (Rate)',
                          'DALYs  Anxiety disorders - Age: 70+ years (Rate)',
                          'DALYs  Anxiety disorders -Age: All Ages (Rate)',
                          'DALYs Anxiety disorders - Age: Age-standardized (Rate)']}


    col2.subheader("Burden of disease from Mental illnesses by age")
    
    # Add a select box for choosing the disorder
    selected_disorder = col2.selectbox('Select a Disorder type', options=list(categories.keys()))

    col2.write(f'Overview Bar chart showing the DALYs rate {selected_disorder.lower()} by Age in the World, the data refers to year of 2019.')

    
    # Filter the data for the selected disorder attributes
    selected_attributes = categories[selected_disorder]
    df_filtered = df10[selected_attributes]

    # Reset the index to include disorder names
    df_filtered = df_filtered.T.reset_index()

    # Assign appropriate column names to the DataFrame
    df_filtered.columns = ['Age Group', 'DALYs Rate']

    # Create a horizontal bar chart
    fig = px.bar(df_filtered,
                x='DALYs Rate',
                y='Age Group',
                title=f'{selected_disorder}: DALYs Rate by Age Group',
                orientation='h',
                labels={'y': '', 'x': 'DALYs Rate'})

    # Display the figure
    col2.plotly_chart(fig)

    col1,col2= st.columns(2)
   
    # Mental disorders based on Income level:
    # Filtering the DataFrame for the selected year and income categories
    
    df_filtered = df4[(df4['Year'] == 2019) & df4['Entity'].isin(['World Bank Low Income', 'World Bank Lower Middle Income', 'World Bank Upper Middle Income', 'World Bank High Income'])]

    col1.subheader(" Burden of Diseases Based on the Income level of countries")
    # Creating the horizontal bar chart
    fig = px.bar(df_filtered,
                y='Entity',
                x='DALYs (Disability-Adjusted Life Years) - Mental disorders - Sex: Both - Age: All Ages (Percent)',
                title='DALYs Mental Disorders (%) for Different Income Levels in 2019',
                labels={
                    'Entity': 'Income Level',
                    'DALYs (Disability-Adjusted Life Years) - Mental disorders - Sex: Both - Age: All Ages (Percent)': 'DALYs (%)'},
                height=400, # Adjust the height as needed
                orientation='h')

    col1.plotly_chart(fig, use_container_width=True)  # make the plot use the full container width

