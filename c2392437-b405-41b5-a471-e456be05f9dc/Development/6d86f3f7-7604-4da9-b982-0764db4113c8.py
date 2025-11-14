"""
Validation Check for Commercial Assumptions Framework
Verifies all required assumptions are defined and accessible
"""

# Validation checks
validation_results = {
    'checks_passed': [],
    'checks_failed': [],
    'total_checks': 0
}

# Check 1: Tier Pricing exists and has 4 tiers
try:
    assert 'tier_pricing' in dir(), "tier_pricing variable not found"
    assert len(tier_pricing) == 4, f"Expected 4 tiers, found {len(tier_pricing)}"
    assert all(tier in tier_pricing for tier in ['Starter', 'Growth', 'Scale', 'Enterprise']), "Missing pricing tiers"
    validation_results['checks_passed'].append("✓ Tier Pricing: 4 tiers defined")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ Tier Pricing: {str(e)}")
validation_results['total_checks'] += 1

# Check 2: Token Economics
try:
    assert 'token_economics' in dir(), "token_economics variable not found"
    assert 'pricing' in token_economics, "Token pricing not defined"
    assert 'burn_rates' in token_economics, "Token burn rates not defined"
    validation_results['checks_passed'].append("✓ Token Economics: pricing and burn rates defined")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ Token Economics: {str(e)}")
validation_results['total_checks'] += 1

# Check 3: Customer Density
try:
    assert 'customer_density' in dir(), "customer_density variable not found"
    assert len(customer_density) == 5, f"Expected 5 segments, found {len(customer_density)}"
    validation_results['checks_passed'].append("✓ Customer Density: 5 segments defined")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ Customer Density: {str(e)}")
validation_results['total_checks'] += 1

# Check 4: GTM Phases
try:
    assert 'gtm_phases' in dir(), "gtm_phases variable not found"
    assert len(gtm_phases) == 3, f"Expected 3 phases, found {len(gtm_phases)}"
    validation_results['checks_passed'].append("✓ GTM Phases: 3 phases defined")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ GTM Phases: {str(e)}")
validation_results['total_checks'] += 1

# Check 5: Geographic Expansion
try:
    assert 'geographic_expansion' in dir(), "geographic_expansion variable not found"
    assert len(geographic_expansion) == 4, f"Expected 4 markets, found {len(geographic_expansion)}"
    validation_results['checks_passed'].append("✓ Geographic Expansion: 4 markets defined")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ Geographic Expansion: {str(e)}")
validation_results['total_checks'] += 1

# Check 6: Conversion Funnels
try:
    assert 'conversion_funnels' in dir(), "conversion_funnels variable not found"
    assert len(conversion_funnels) >= 4, f"Expected 4+ funnels, found {len(conversion_funnels)}"
    validation_results['checks_passed'].append("✓ Conversion Funnels: defined with segment variations")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ Conversion Funnels: {str(e)}")
validation_results['total_checks'] += 1

# Check 7: Churn Rates
try:
    assert 'churn_rates' in dir(), "churn_rates variable not found"
    assert len(churn_rates) == 4, f"Expected 4 tiers, found {len(churn_rates)}"
    validation_results['checks_passed'].append("✓ Churn Rates: 4 tiers defined")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ Churn Rates: {str(e)}")
validation_results['total_checks'] += 1

# Check 8: CAC by Channel
try:
    assert 'cac_by_channel' in dir(), "cac_by_channel variable not found"
    assert len(cac_by_channel) == 4, f"Expected 4 channels, found {len(cac_by_channel)}"
    validation_results['checks_passed'].append("✓ CAC by Channel: 4 channels defined")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ CAC by Channel: {str(e)}")
validation_results['total_checks'] += 1

# Check 9: Network Effects
try:
    assert 'network_effects' in dir(), "network_effects variable not found"
    assert 'nvm_curve' in network_effects, "NVM curve not defined"
    assert 'critical_mass_milestones' in network_effects, "Critical mass milestones not defined"
    validation_results['checks_passed'].append("✓ Network Effects: NVM curve and milestones defined")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ Network Effects: {str(e)}")
validation_results['total_checks'] += 1

# Check 10: Consolidated Dashboard
try:
    assert 'consolidated_assumptions' in dir(), "consolidated_assumptions variable not found"
    assert 'metadata' in consolidated_assumptions, "Metadata not found"
    assert consolidated_assumptions['metadata']['ready_for_downstream'] == True, "Not marked as ready"
    validation_results['checks_passed'].append("✓ Consolidated Dashboard: ready for downstream use")
except AssertionError as e:
    validation_results['checks_failed'].append(f"✗ Consolidated Dashboard: {str(e)}")
validation_results['total_checks'] += 1

# Print results
print("=" * 60)
print("ASSUMPTIONS FRAMEWORK VALIDATION")
print("=" * 60)
print(f"\nTotal Checks: {validation_results['total_checks']}")
print(f"Passed: {len(validation_results['checks_passed'])}")
print(f"Failed: {len(validation_results['checks_failed'])}")
print("\nPassed Checks:")
for check in validation_results['checks_passed']:
    print(f"  {check}")

if validation_results['checks_failed']:
    print("\nFailed Checks:")
    for check in validation_results['checks_failed']:
        print(f"  {check}")
else:
    print("\n✅ ALL CHECKS PASSED - Framework is complete and ready!")
print("=" * 60)