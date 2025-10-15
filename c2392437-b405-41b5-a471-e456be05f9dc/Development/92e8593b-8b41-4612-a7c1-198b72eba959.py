"""
Network Effect Multiplier on Token Velocity
Models how NVM increases token consumption as data quality improves
"""
import pandas as pd

# NVM curve from network effects assumptions
nvm_by_year = {
    'year_1': 1.12,
    'year_2': 1.35,
    'year_3': 1.68,
    'year_4': 1.98,
    'year_5': 2.34
}

# Data quality progression (drives NVM effectiveness)
data_quality_progression = {
    'year_1': {'hit_rate': 0.35, 'consensus_conf': 0.45, 'freshness': 0.50},
    'year_2': {'hit_rate': 0.48, 'consensus_conf': 0.52, 'freshness': 0.62},
    'year_3': {'hit_rate': 0.62, 'consensus_conf': 0.58, 'freshness': 0.72},
    'year_4': {'hit_rate': 0.72, 'consensus_conf': 0.62, 'freshness': 0.78},
    'year_5': {'hit_rate': 0.78, 'consensus_conf': 0.68, 'freshness': 0.82}
}

# Token velocity: queries per customer per month increases with NVM
# Base velocity = 1.0 (baseline month 0)
# NVM multiplier increases velocity as network effects kick in
base_velocity = 1.0

nvm_velocity_model = {}

for _yr in range(1, 6):
    _yr_key = f'year_{_yr}'
    _nvm = nvm_by_year[_yr_key]
    _quality = data_quality_progression[_yr_key]
    
    # Velocity increases with NVM and data quality
    _token_velocity = base_velocity * _nvm
    _quality_boost = (_quality['hit_rate'] + _quality['consensus_conf'] + _quality['freshness']) / 3
    _effective_velocity = _token_velocity * (0.7 + 0.3 * _quality_boost / 0.8)  # Quality adds up to 30% boost
    
    nvm_velocity_model[_yr_key] = {
        'year': _yr,
        'nvm': _nvm,
        'hit_rate': _quality['hit_rate'],
        'consensus_confidence': _quality['consensus_conf'],
        'freshness_index': _quality['freshness'],
        'token_velocity': _effective_velocity,
        'velocity_increase_pct': (_effective_velocity - 1.0) * 100
    }

velocity_df = pd.DataFrame.from_dict(nvm_velocity_model, orient='index')

print("Network Effect Token Velocity Model")
print("="*70)
print("Token velocity = queries per customer per month\n")
for _yr in velocity_df.index:
    _row = velocity_df.loc[_yr]
    print(f"Year {_row['year']:.0f}:")
    print(f"  NVM: {_row['nvm']:.2f}x | Hit Rate: {_row['hit_rate']:.0%} | Velocity: {_row['token_velocity']:.2f}x")
    print(f"  Velocity increase: +{_row['velocity_increase_pct']:.1f}%")