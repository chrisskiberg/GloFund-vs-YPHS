# Make random statistical experiment and see how often it wins for each year

import matplotlib.pyplot as plt 


yearly_sum=27500

YPHS_first_year_yield=0.16
YPHS_other_years_yield=0.06

GloFund_yearly_yield_min=0.05
GloFund_yearly_yield_max=0.10

YPHS_over_the_years=[]
GloFund_min_over_the_years=[]
GloFund_max_over_the_years=[]

years=10
for year in range(years):

    YPHS_year_i_arr=[yearly_sum*(1+YPHS_first_year_yield)]
    # YPHS - No risk
    for i in range(year):
        for j in range(len(YPHS_year_i_arr)):
            YPHS_year_i_arr[j]=YPHS_year_i_arr[j]*(1+YPHS_other_years_yield)
        YPHS_year_i_arr.append(yearly_sum*(1+YPHS_first_year_yield))

    # print(YPHS_year_i_arr)
    # print(sum(YPHS_year_i_arr))
    YPHS_over_the_years.append(sum(YPHS_year_i_arr))

    # print("")

    GloFund_min_year_i_arr=[yearly_sum*(1+GloFund_yearly_yield_min)]
    GloFund_max_year_i_arr=[yearly_sum*(1+GloFund_yearly_yield_max)]

    # GloFund - Risky, but over time less risk
    for i in range(year):
        for j in range(len(GloFund_min_year_i_arr)):
            GloFund_min_year_i_arr[j]=GloFund_min_year_i_arr[j]*(1+GloFund_yearly_yield_min)
            GloFund_max_year_i_arr[j]=GloFund_max_year_i_arr[j]*(1+GloFund_yearly_yield_max)
        GloFund_min_year_i_arr.append(yearly_sum*(1+GloFund_yearly_yield_min))
        GloFund_max_year_i_arr.append(yearly_sum*(1+GloFund_yearly_yield_max))

    # print(GloFund_min_year_i_arr)
    # print(sum(GloFund_min_year_i_arr))
    # print(GloFund_max_year_i_arr)
    # print(sum(GloFund_max_year_i_arr))

    GloFund_min_over_the_years.append(sum(GloFund_min_year_i_arr))
    GloFund_max_over_the_years.append(sum(GloFund_max_year_i_arr))


# print(YPHS_over_the_years)
print(*map(int, YPHS_over_the_years))
print(*map(int, GloFund_min_over_the_years))
print(*map(int, GloFund_max_over_the_years))

years_x=[i for i in range(years)]

plt.scatter(years_x, YPHS_over_the_years)
plt.scatter(years_x, GloFund_min_over_the_years)
plt.scatter(years_x, GloFund_max_over_the_years)
plt.grid()
plt.show()
