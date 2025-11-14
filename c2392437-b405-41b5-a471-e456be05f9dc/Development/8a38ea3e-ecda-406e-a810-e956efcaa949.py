"""
Go-To-Market Phase Definitions
Source: Schema GTM strategy - phase definitions with target accounts by segment
"""

gtm_phases = {
    'stealth': {
        'phase_description': 'Initial market entry - focused verticals',
        'target_segments': ['DCAs', 'insurers', 'legal_firms'],
        'estimated_total_accounts': 120,
        'account_breakdown': {
            'dca': 45,
            'insurers': 50,
            'legal_firms': 25
        },
        'timing': 'Year 1 - Months 1-6',
        'focus': 'Proof of concept and early adopters in credit-intensive industries'
    },
    'beta': {
        'phase_description': 'Expansion to adjacent segments',
        'target_segments': ['consultants', 'SMEs', 'private_equity'],
        'estimated_total_accounts': 850,
        'account_breakdown': {
            'consultants': 200,
            'smes': 500,
            'private_equity': 150
        },
        'timing': 'Year 1-2 - Months 6-18',
        'focus': 'Broader B2B market validation and product refinement'
    },
    'launch': {
        'phase_description': 'Full market launch and scaling',
        'target_segments': ['enterprises', 'banks', 'brokers', 'corporates'],
        'estimated_total_accounts_y2': 1800,
        'estimated_total_accounts_y3': 4200,
        'timing': 'Year 2-3 onwards',
        'focus': 'Enterprise sales, channel partnerships, market dominance'
    }
}

print("GTM Phase Strategy Defined")
print("\nPhase Overview:")
for _gtm_phase, _gtm_info in gtm_phases.items():
    print(f"\n{_gtm_phase.upper()}:")
    print(f"  Description: {_gtm_info['phase_description']}")
    print(f"  Timing: {_gtm_info['timing']}")
    if 'estimated_total_accounts' in _gtm_info:
        print(f"  Target Accounts: ~{_gtm_info['estimated_total_accounts']:,}")