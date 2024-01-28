yearly_sum=27500

YPHS_first_year_yield=0.16
YPHS_other_years_yield=0.06

GloFund_yearly_yield_min=0.05
GloFund_yearly_yield_max=0.10

YPHS=[yearly_sum*(1+YPHS_first_year_yield)]
# YPHS - No risk
for i in range(10):
    for j in range(len(YPHS)):
        YPHS[j]=YPHS[j]*(1+YPHS_other_years_yield)
    YPHS.append(yearly_sum*(1+YPHS_first_year_yield))

print(YPHS)
print(sum(YPHS))


print("")

GloFund_min=[yearly_sum*(1+GloFund_yearly_yield_min)]
GloFund_max=[yearly_sum*(1+GloFund_yearly_yield_max)]

# GloFund - Risky, but over time less risk
for i in range(10):
    for j in range(len(GloFund_min)):
        GloFund_min[j]=GloFund_min[j]*(1+GloFund_yearly_yield_min)
        GloFund_max[j]=GloFund_max[j]*(1+GloFund_yearly_yield_max)
    GloFund_min.append(yearly_sum*(1+GloFund_yearly_yield_min))
    GloFund_max.append(yearly_sum*(1+GloFund_yearly_yield_max))

print(GloFund_min)
print(sum(GloFund_min))
print(GloFund_max)
print(sum(GloFund_max))
