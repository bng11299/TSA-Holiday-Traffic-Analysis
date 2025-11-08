Analyzing U.S. Holiday Air Travel: A Comparative Study of Departure and Return Flight Concentration


Introduction: 

Our research aims to explore the question: Is the traffic of departure flights more concentrated than that of return flights around major U.S. holidays? 

This question investigates how U.S. air travel volume fluctuates before and after key holidays in the United States. We also aim to identify which days offer the optimal balance between proximity to the holiday and lower traveler congestion. This information is helpful for both travelers who wish to find cheaper tickets/less crowded airports and also the airport and TSA for staffing and security purposes. 

While there is a lot of data out there suggesting that airports are generally busier on the days leading up to holidays, there is limited quantitative analysis comparing departure versus return travel concentration. Understanding these dynamics can reveal behavioral patterns in how Americans plan their travel relative to holiday timing and also how TSA approaches these seasons. 

We will test the following hypotheses:

H₀: The concentration of departure flight traffic above normal is the same as return traffic for major U.S. holidays.

Hₐ: The concentration of departure flight traffic above normal is more concentrated than return traffic for major U.S. holidays.

Our inclination is that the concentration of departure flight traffic is more concentrated than return traffic. 


Statement of Significance:

In a hypothetical situation, our friend Mateo is a manager working for the TSA. While most days, he can get away with understaffing his airports, he is forced to schedule more people to work around major holidays. In order to cut costs, he wants to understand whether the surge in travelers tends to occur more before or after holidays, so he can better allocate staff and resources. By analyzing patterns in TSA checkpoint data, this study seeks to determine whether the traffic of departure flights is more concentrated than that of return flights around major U.S. holidays. The findings could help airport managers like Mateo plan staffing more efficiently and provide insights into national travel behaviors during peak seasons.

Additionally, travelers could identify “sweet spot” dates that balance proximity to the holiday with lower congestion, improving trip planning and potentially lowering costs.


Data

We will pull the data of TSA checkpoint passenger volumes off the official TSA website. It covers January 1, 2019 to the current date, which is updated constantly Mondays to Fridays. We will use all data from 2019–2024. Because we are looking at U.S. holidays, it is appropriate to use the TSA numbers, keeping our statistics restricted to the United States

Access & filtering criteria:

• Source: TSA Checkpoint Passenger Volumes

• Time window: 2019–2024 

• Holidays we are planning to analyze (initial set): Thanksgiving (Thu), Christmas (Dec 25), New Year’s Day (Jan 1), Memorial Day (last Mon in May), Independence Day (Jul 4), Labor Day (first Mon in Sep), and Spring Break (second half of March; exploratory).

• Holiday window: 10 days before through 10 days after each holiday (−10…+10)

Exclusions/adjustments: We will take into account that weekends generally have more air traffic,  counts flag extreme weather weeks where known, and dates where holidays shift. 

We plan to analyze whether departure flight traffic is more concentrated than return traffic around major U.S. holidays using the TSA Checkpoint Passenger Volume dataset from 2019 to 2024. First, we’ll clean and organize the data to make sure it’s consistent across years and account for possible outliers and confounding variables, such as pandemic-related dips or ethnic holidays. The data availability should not be an issue, since the website is consistent and regularly updated. For each major holiday, we’ll define a time window (for example, ten days before and after) and create two main variables: the total number of passengers screened each day and the number of days relative to the holiday. This will let us compare how traffic builds up before holidays versus how it declines after.

To measure travel surges, we’ll calculate how much each day’s passenger volume deviates from a baseline average. Then we’ll visualize the patterns using line plots to see how travel intensity changes over time. After that, we’ll use statistical methods to compare the two sides of the holiday period. Metrics like variance and mean will help us see whether the pre-holiday spike is more tightly packed than the post-holiday one. If time allows, we might apply simple time-series modeling to highlight consistent trends across multiple holidays and years. Overall, our goal is to understand whether travelers tend to leave in a concentrated rush before holidays or return more gradually afterward.
