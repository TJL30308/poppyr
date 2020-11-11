#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd


# In[3]:


countries = ['US', 'France', 'Germany', 'Italy', 'Spain', 'UK', 'Japan', 'Australia', 'Brazil', 'Canada', 
            'China', 'India', 'Mexico', 'Russia', 'SAfrica', 'SKorea' ]

for country in countries:
    country = country
    read_file = f'data/USCB_{country}.csv'
    data = pd.read_csv(read_file, header=1, sep=r'\s*,\s*', engine='python')
    
    men_population = data['Male Population'][1:22]
    women_population = data['Female Population'][1:22]

    myInt = 1
    myInt2 = -1

    new_men = [x / myInt for x in men_population]

    new_women = [x / myInt2 for x in women_population]
    
    women_bins = np.array(new_women)
    men_bins = np.array(new_men)
    

    y = data['Age'][1:22]

    layout = go.Layout(yaxis=go.layout.YAxis(title='Age'),
                  xaxis=go.layout.XAxis(
                      title='Population'),
                  barmode='overlay',
                  bargap=0.1,
                  plot_bgcolor='rgba(0,0,0,0)'
                  )

    data = [go.Bar(y=y,
              x=men_bins,
              orientation='h',
              name='Men',
              text = men_bins.astype('int'),
              hoverinfo='text',
              marker=dict(color='powderblue')
              ),
        go.Bar(y=y,
               x= women_bins,
               orientation='h',
               name='Women',
               text= -1 * women_bins.astype('int'),
               hoverinfo='text',
               marker=dict(color='seagreen')
              )]

    fig = go.Figure(
        data=data,
        layout=layout
    )

    fig.update_layout(title=f"{country}", title_x=0.475)

    fig.update_layout(
        autosize=False,
        width=600,
        height=600)

    fig.show()
    
    fig.write_image(f'plots/{country}_pyramid.png')


# In[ ]:





# In[ ]:




