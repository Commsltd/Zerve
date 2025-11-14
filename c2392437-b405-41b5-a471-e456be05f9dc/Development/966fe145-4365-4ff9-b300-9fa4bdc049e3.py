"""
Dashboard Output 1: ARR/MRR Overview with Trends
Display total ARR/MRR with key growth metrics and milestones
"""
import pandas as pd

# Get latest month metrics (Month 60)
_latest_month = arr_growth_metrics.iloc[-1]
latest_arr = _latest_month['arr']
latest_mrr = _latest_month['mrr']
latest_arr_mom_growth = _latest_month['arr_mom_growth']
latest_mrr_mom_growth = _latest_month['mrr_mom_growth']

# Calculate YoY growth for month 60 vs month 48
_m60_arr = arr_growth_metrics.iloc[59]['arr']
_m48_arr = arr_growth_metrics.iloc[47]['arr']
yoy_growth = (_m60_arr - _m48_arr) / _m48_arr

# Get milestone metrics
m12_arr = arr_growth_metrics.iloc[11]['arr']
m24_arr = arr_growth_metrics.iloc[23]['arr']
m36_arr = arr_growth_metrics.iloc[35]['arr']
m48_arr = arr_growth_metrics.iloc[47]['arr']
m60_arr = arr_growth_metrics.iloc[59]['arr']

# Calculate CAGR (from M12 to M60)
_years = (60 - 12) / 12
cagr = ((m60_arr / m12_arr) ** (1 / _years)) - 1

# Get milestone months from Series - first element is the month number
milestone_1m_month = int(milestone_arr_1m.iloc[0])
milestone_5m_month = int(milestone_arr_5m.iloc[0])
milestone_10m_month = int(milestone_arr_10m.iloc[0])

print("=" * 70)
print("📊 ARR/MRR OVERVIEW - MONTH 60 (END OF YEAR 5)")
print("=" * 70)
print()
print(f"💰 Current ARR:        £{latest_arr:,.0f}")
print(f"💰 Current MRR:        £{latest_mrr:,.0f}")
print()
print("📈 Growth Trends:")
print(f"   MoM Growth:         {latest_arr_mom_growth:.1%}")
print(f"   YoY Growth (M60 vs M48): {yoy_growth:.1%}")
print(f"   4-Year CAGR (M12-M60):   {cagr:.1%}")
print()
print("🎯 Milestone Progress:")
print(f"   Year 1 ARR (M12):   £{m12_arr:,.0f}")
print(f"   Year 2 ARR (M24):   £{m24_arr:,.0f}")
print(f"   Year 3 ARR (M36):   £{m36_arr:,.0f}")
print(f"   Year 4 ARR (M48):   £{m48_arr:,.0f}")
print(f"   Year 5 ARR (M60):   £{m60_arr:,.0f}")
print()
print(f"✅ Reached £1M ARR milestone: Month {milestone_1m_month}")
print(f"✅ Reached £5M ARR milestone: Month {milestone_5m_month}")
print(f"✅ Reached £10M ARR milestone: Month {milestone_10m_month}")
print()
print("=" * 70)