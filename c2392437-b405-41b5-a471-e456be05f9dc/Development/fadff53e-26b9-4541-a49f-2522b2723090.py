"""
Geographic Expansion Timeline and Market Size Multipliers
Source: Schema geographic strategy - regional expansion timing and TAM multipliers
"""

geographic_expansion = {
    'uk': {
        'timing': 'Year 1',
        'market_size_multiplier': 1.0,  # Baseline market
        'status': 'Primary market - foundation',
        'characteristics': 'Home market, regulatory familiarity, initial customer base'
    },
    'eu': {
        'timing': 'Year 2',
        'market_size_multiplier': 2.3,  # EU market is 2.3x UK
        'status': 'First international expansion',
        'characteristics': 'Similar regulatory framework (GDPR), cultural proximity, established B2B markets',
        'key_markets': ['Germany', 'France', 'Netherlands', 'Ireland']
    },
    'us': {
        'timing': 'Year 3',
        'market_size_multiplier': 4.1,  # US market is 4.1x UK
        'status': 'Major market expansion',
        'characteristics': 'Largest market opportunity, different regulatory environment, high adoption rates',
        'considerations': 'Entity setup required, different credit reporting ecosystem'
    },
    'apac': {
        'timing': 'Year 4-5',
        'market_size_multiplier': 1.8,  # APAC addressable market is 1.8x UK
        'status': 'Long-term expansion',
        'characteristics': 'High growth potential, diverse markets, varied regulatory landscapes',
        'key_markets': ['Singapore', 'Australia', 'Japan', 'Hong Kong']
    }
}

print("Geographic Expansion Strategy Defined")
print("\nRegional Expansion Timeline:")
for _geo_region, _geo_info in geographic_expansion.items():
    _geo_mult = _geo_info['market_size_multiplier']
    _geo_timing = _geo_info['timing']
    print(f"  {_geo_region.upper()}: {_geo_timing}, Market Multiplier: {_geo_mult}x")