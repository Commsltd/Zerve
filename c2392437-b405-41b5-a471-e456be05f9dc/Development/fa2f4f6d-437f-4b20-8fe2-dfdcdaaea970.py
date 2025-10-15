"""
Contributor Token Reward Mechanism
Models token credits earned by data contributors, reducing net consumption
"""
import pandas as pd

# Contributor reward assumptions
# Contributors earn tokens for submitting invoice data
contributor_reward_structure = {
    'tokens_per_invoice': 0.05,  # Small reward per invoice submitted
    'tokens_per_verified_debtor': 0.25,  # Larger reward for new debtor data
    'monthly_cap_per_contributor': 50,  # Max tokens earned per month
}

# Contributor activity by segment (invoices submitted per month)
contributor_activity = {
    'micro': {'avg_invoices_submitted': 15, 'avg_new_debtors': 2},
    'small': {'avg_invoices_submitted': 25, 'avg_new_debtors': 3},
    'medium': {'avg_invoices_submitted': 80, 'avg_new_debtors': 8},
    'large': {'avg_invoices_submitted': 250, 'avg_new_debtors': 15},
    'mnc': {'avg_invoices_submitted': 800, 'avg_new_debtors': 35}
}

# Calculate token rewards earned
contributor_rewards_by_segment = {}

for _seg, _activity in contributor_activity.items():
    _invoice_tokens = _activity['avg_invoices_submitted'] * contributor_reward_structure['tokens_per_invoice']
    _debtor_tokens = _activity['avg_new_debtors'] * contributor_reward_structure['tokens_per_verified_debtor']
    _total_earned = _invoice_tokens + _debtor_tokens
    
    # Apply monthly cap
    _capped_tokens = min(_total_earned, contributor_reward_structure['monthly_cap_per_contributor'])
    
    contributor_rewards_by_segment[_seg] = {
        'invoices_submitted': _activity['avg_invoices_submitted'],
        'new_debtors': _activity['avg_new_debtors'],
        'tokens_from_invoices': _invoice_tokens,
        'tokens_from_debtors': _debtor_tokens,
        'total_tokens_earned': _total_earned,
        'capped_tokens_earned': _capped_tokens,
        'cap_applied': _total_earned > contributor_reward_structure['monthly_cap_per_contributor']
    }

rewards_df = pd.DataFrame.from_dict(contributor_rewards_by_segment, orient='index')

# Calculate net consumption offset (assume 45% of customers are active contributors)
contributor_participation_rate = 0.45
avg_reward_offset_pct = (rewards_df['capped_tokens_earned'].mean() / 
                         consumption_by_segment['medium']['total_monthly_tokens']) * contributor_participation_rate

print("Contributor Token Reward Mechanism")
print("="*70)
print(f"Rewards: {contributor_reward_structure['tokens_per_invoice']:.2f} tokens/invoice")
print(f"         {contributor_reward_structure['tokens_per_verified_debtor']:.2f} tokens/new debtor")
print(f"Monthly cap: {contributor_reward_structure['monthly_cap_per_contributor']} tokens\n")

for _seg in rewards_df.index:
    _row = rewards_df.loc[_seg]
    print(f"{_seg.upper()}: {_row['capped_tokens_earned']:.1f} tokens/month earned")

print(f"\nNet Consumption Offset: ~{avg_reward_offset_pct:.1%} (at {contributor_participation_rate:.0%} participation)")