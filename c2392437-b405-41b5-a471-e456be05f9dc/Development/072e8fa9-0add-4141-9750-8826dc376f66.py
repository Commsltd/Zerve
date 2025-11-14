"""
Token Rollover and Expiry Tracking
Models 90-day rollover policy and token expiry
"""
import pandas as pd
import numpy as np

# Rollover parameters
rollover_days = 90
rollover_months = 3

# Simulate token balance over 12 months for a typical customer
# Assume Growth tier customer with fluctuating consumption
months = list(range(1, 13))

# Growth tier: 1,250 tokens/month included
monthly_allocation = 1250

# Simulate monthly consumption with variation (70-130% of allocation)
np.random.seed(42)
consumption_variation = np.random.uniform(0.70, 1.30, 12)

rollover_simulation = []

token_bank = 0  # Starting token bank
tokens_expired = 0

for _m_idx, _month in enumerate(months):
    # Monthly consumption
    _base_consumption = 1100  # Typical Growth tier usage
    _actual_consumption = int(_base_consumption * consumption_variation[_m_idx])
    
    # Add monthly allocation
    _tokens_received = monthly_allocation
    
    # Use tokens (oldest first - FIFO)
    _tokens_used = min(_actual_consumption, token_bank + _tokens_received)
    
    # Calculate rollover
    _tokens_remaining = token_bank + _tokens_received - _tokens_used
    
    # Expire tokens older than 90 days (3 months)
    if _m_idx >= rollover_months:
        # Simple model: tokens from 3+ months ago expire
        _expired_this_month = max(0, int(_tokens_remaining * 0.08))  # ~8% expiry rate
        tokens_expired += _expired_this_month
        _tokens_remaining -= _expired_this_month
    else:
        _expired_this_month = 0
    
    rollover_simulation.append({
        'month': _month,
        'allocation': _tokens_received,
        'consumption': _actual_consumption,
        'tokens_used': _tokens_used,
        'tokens_remaining': _tokens_remaining,
        'tokens_expired': _expired_this_month,
        'cumulative_expired': tokens_expired
    })
    
    token_bank = _tokens_remaining

rollover_df = pd.DataFrame(rollover_simulation)

print("Token Rollover & Expiry Mechanics (90-Day Policy)")
print("="*70)
print("Example: Growth tier customer (1,250 tokens/month)\n")
print(f"{'Month':<6} {'Alloc':<7} {'Used':<7} {'Remaining':<10} {'Expired':<8}")
print("-" * 50)
for _idx, _row in rollover_df.iterrows():
    print(f"{_row['month']:<6} {_row['allocation']:<7} {_row['tokens_used']:<7} "
          f"{_row['tokens_remaining']:<10.0f} {_row['tokens_expired']:<8.0f}")

print(f"\nTotal tokens expired over 12 months: {rollover_df['cumulative_expired'].iloc[-1]:.0f}")
print(f"Expiry rate: {rollover_df['tokens_expired'].sum() / rollover_df['allocation'].sum():.1%}")