"""
Network Effect Value Multiplier (NVM) Curve
Source: Schema network effects - value multiplier tied to critical mass milestones
"""

network_effects = {
    'nvm_curve': {
        'year_1': 1.12,
        'year_2': 1.35,
        'year_3': 1.68,
        'year_4': 1.98,
        'year_5': 2.34,
        'description': 'Network value multiplier increases as platform reaches critical mass'
    },
    'critical_mass_milestones': {
        'invoices_processed': 35_800_000,  # 35.8M invoices
        'unique_debtors': 1_800_000,  # 1.8M debtors
        'active_contributors': 4_500,  # 4.5k contributors
        'data_hit_rate': 0.78,  # 78% hit rate
        'description': 'Target metrics for full network effect realization by Year 5'
    },
    'value_drivers': {
        'data_completeness': 'More invoices = better credit intelligence',
        'debtor_coverage': 'More debtors = higher query hit rates',
        'contributor_network': 'More contributors = fresher data and broader coverage',
        'predictive_accuracy': 'Larger dataset = more accurate risk models'
    },
    'compounding_mechanics': {
        'data_flywheel': 'Each new customer adds data, improving value for all users',
        'virality_coefficient': 'Users invite suppliers/customers, creating organic growth',
        'switching_costs': 'Unique data moat increases retention as network grows'
    }
}

print("Network Effects Model Defined")
print("\nNetwork Value Multiplier (NVM) Curve:")
for _nvm_year, _nvm_val in network_effects['nvm_curve'].items():
    if _nvm_year != 'description':
        print(f"  {_nvm_year.replace('_', ' ').title()}: {_nvm_val}x")

print("\nCritical Mass Targets (Year 5):")
_critical_milestones = network_effects['critical_mass_milestones']
print(f"  Invoices: {_critical_milestones['invoices_processed']:,.0f}")
print(f"  Debtors: {_critical_milestones['unique_debtors']:,.0f}")
print(f"  Contributors: {_critical_milestones['active_contributors']:,.0f}")
print(f"  Hit Rate: {_critical_milestones['data_hit_rate']:.0%}")