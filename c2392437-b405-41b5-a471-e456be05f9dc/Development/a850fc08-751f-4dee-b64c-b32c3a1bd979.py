"""
Customer Acquisition Cost (CAC) by Channel and Phase
Source: Schema GTM economics - acquisition costs by channel and customer segment
"""

cac_by_channel = {
    'stealth_partnerships': {
        'avg_cac_gbp': 450,
        'phase': 'Stealth',
        'channels': ['Direct relationships', 'Industry partnerships', 'Referrals'],
        'description': 'Low CAC through warm introductions and partnerships',
        'target_segments': ['DCAs', 'insurers', 'legal_firms']
    },
    'beta_digital': {
        'avg_cac_gbp': 1200,
        'phase': 'Beta',
        'channels': ['Digital marketing', 'Content marketing', 'Self-service'],
        'description': 'Moderate CAC through digital acquisition and PLG motion',
        'target_segments': ['consultants', 'SMEs', 'private_equity']
    },
    'launch_mixed': {
        'avg_cac_gbp': 3500,
        'phase': 'Launch (SME/Mid-market)',
        'channels': ['Inside sales', 'Marketing automation', 'Webinars', 'Paid media'],
        'description': 'Higher CAC for proactive mid-market acquisition',
        'target_segments': ['Medium enterprises', 'growing corporates']
    },
    'enterprise_outbound': {
        'avg_cac_gbp': 8500,
        'phase': 'Launch (Enterprise)',
        'channels': ['Field sales', 'Account-based marketing', 'Executive engagement'],
        'description': 'High CAC for strategic enterprise deals with large lifetime value',
        'target_segments': ['Large enterprises', 'MNCs', 'banks']
    }
}

print("CAC by Channel Model Defined")
print("\nCustomer Acquisition Cost by Channel:")
for _cac_channel, _cac_info in cac_by_channel.items():
    _cac_val = _cac_info['avg_cac_gbp']
    _cac_phase = _cac_info['phase']
    print(f"  {_cac_channel}: £{_cac_val:,} ({_cac_phase})")