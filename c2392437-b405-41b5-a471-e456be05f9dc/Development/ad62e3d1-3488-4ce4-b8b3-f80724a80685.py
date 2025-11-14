"""
Master Parameter Configuration Block
Comprehensive editable dictionary containing all major financial model parameters
Extracted from baseline assumptions and calculations
"""

# =============================================================================
# PRICING PARAMETERS BY TIER
# =============================================================================
pricing_params = {
    'Standard': {  # Previously 'Starter'
        'monthly_price_gbp': 495,
        'included_tokens': 300,
        'target_segment': 'Micro/Small businesses testing platform',
        'avg_seats': 1,
        'description': 'Entry tier for companies exploring platform capabilities'
    },
    'Professional': {  # Previously 'Growth'
        'monthly_price_gbp': 1895,
        'included_tokens': 1250,
        'target_segment': 'Small/Medium businesses with active usage',
        'avg_seats': 3,
        'price_per_seat': 632,  # monthly_price / avg_seats
        'description': 'Mid-tier for scaling operations'
    },
    'Scale': {
        'monthly_price_gbp': 4950,
        'included_tokens': 5000,
        'target_segment': 'Large enterprises with significant volume',
        'avg_seats': 10,
        'price_per_seat': 495,
        'description': 'High-volume tier for established users'
    },
    'Enterprise': {
        'monthly_price_gbp': 15000,
        'included_tokens': 'custom',
        'target_segment': 'MNC/Complex organizations',
        'price_per_seat': 500,
        'avg_seats': 30,
        'description': 'Custom pricing with dedicated support and tailored solutions'
    }
}

# =============================================================================
# CUSTOMER ACQUISITION COST (CAC) BY SEGMENT
# =============================================================================
cac_params = {
    'stealth_partnerships': {
        'avg_cac_gbp': 450,
        'phase': 'Stealth (Months 1-6)',
        'channels': ['Direct relationships', 'Industry partnerships', 'Referrals'],
        'target_segments': ['DCAs', 'insurers', 'legal_firms']
    },
    'beta_digital': {
        'avg_cac_gbp': 1200,
        'phase': 'Beta (Months 7-18)',
        'channels': ['Digital marketing', 'Content marketing', 'Self-service'],
        'target_segments': ['consultants', 'SMEs', 'private_equity']
    },
    'launch_mixed': {
        'avg_cac_gbp': 3500,
        'phase': 'Launch SME/Mid-market (Month 19+)',
        'channels': ['Inside sales', 'Marketing automation', 'Webinars', 'Paid media'],
        'target_segments': ['Medium enterprises', 'growing corporates']
    },
    'enterprise_outbound': {
        'avg_cac_gbp': 8500,
        'phase': 'Launch Enterprise (Month 19+)',
        'channels': ['Field sales', 'Account-based marketing', 'Executive engagement'],
        'target_segments': ['Large enterprises', 'MNCs', 'banks']
    }
}

# =============================================================================
# CHURN RATES BY TIER
# =============================================================================
churn_params = {
    'Standard': {
        'monthly_churn_rate': 0.035,  # 3.5% per month
        'annual_retention': 0.66,  # 66% annual retention
        'description': 'Higher churn due to experimentation and budget constraints'
    },
    'Professional': {
        'monthly_churn_rate': 0.022,  # 2.2% per month
        'annual_retention': 0.77,  # 77% annual retention
        'description': 'Moderate churn as customers establish value'
    },
    'Scale': {
        'monthly_churn_rate': 0.011,  # 1.1% per month
        'annual_retention': 0.88,  # 88% annual retention
        'description': 'Low churn with high switching costs and deep integration'
    },
    'Enterprise': {
        'monthly_churn_rate': 0.006,  # 0.6% per month
        'annual_retention': 0.93,  # 93% annual retention
        'description': 'Very low churn with long-term contracts and strategic relationships'
    }
}

# =============================================================================
# VOLUME GROWTH & ACQUISITION ASSUMPTIONS
# =============================================================================
volume_params = {
    'gtm_phases': {
        'stealth': {
            'duration_months': 6,  # Months 1-6
            'base_monthly_acquisition_standard': 20,
            'growth_rate_per_month': 0.10,  # 10% monthly growth
            'tier_mix': {'standard': 1.0, 'professional': 0.0, 'scale': 0.0, 'enterprise': 0.0}
        },
        'beta': {
            'duration_months': 12,  # Months 7-18
            'base_monthly_acquisition_standard': 40,
            'base_monthly_acquisition_professional': 10,
            'base_monthly_acquisition_scale': 2,
            'growth_rate_per_month': 0.08,
            'tier_mix': {'standard': 0.65, 'professional': 0.25, 'scale': 0.10, 'enterprise': 0.0}
        },
        'launch': {
            'duration_months': 42,  # Months 19-60
            'base_monthly_acquisition_standard': 60,
            'base_monthly_acquisition_professional': 25,
            'base_monthly_acquisition_scale': 8,
            'base_monthly_acquisition_enterprise': 2,
            'acceleration_factor': 2.0,  # Growth factor over launch period
            'tier_mix': {'standard': 0.50, 'professional': 0.30, 'scale': 0.15, 'enterprise': 0.05}
        }
    },
    'customer_density_by_segment': {
        'micro': {'avg_customers_per_account': 25, 'segment_size': '1-9 employees'},
        'small': {'avg_customers_per_account': 35, 'segment_size': '10-49 employees'},
        'medium': {'avg_customers_per_account': 210, 'segment_size': '50-249 employees'},
        'large': {'avg_customers_per_account': 1325, 'segment_size': '250-999 employees'},
        'mnc': {'avg_customers_per_account': 23000, 'segment_size': '1000+ employees'}
    }
}

# =============================================================================
# TOKEN FINANCE METRICS
# =============================================================================
token_params = {
    'pricing': {
        'payg_rate_gbp': 2.0,  # £2 per token for pay-as-you-go
        'overage_rate_gbp': 1.5,  # £1.50 per token for overage beyond included
        'rollover_days': 90,
        'rollover_policy': 'Unused tokens roll over for 90 days'
    },
    'consumption_rates': {
        'search_per_query': 1,  # 1 token per search query
        'monitor_per_entity_per_month': 1,  # 1 token per monitored entity per month
        'ai_report_generation': 10  # 10 tokens per AI-generated report
    },
    'typical_usage_by_tier': {
        'Standard': 250,  # Monthly tokens
        'Professional': 1100,
        'Scale': 4500,
        'Enterprise': 'custom'
    }
}

# =============================================================================
# INVOICE FINANCE METRICS
# =============================================================================
invoice_finance_params = {
    'product_timeline': {
        'institutional_pilot_start': 18,  # Month 18 (Y2 Q3)
        'institutional_scale_start': 24,  # Month 24 (Y3)
        'p2p_pilot_start': 39,  # Month 39 (Y3 Q4)
        'p2p_scale_start': 48   # Month 48 (Y4)
    },
    'institutional_take_rates': {
        'low_risk': 0.015,   # 1.5% for <10% prob_late_60
        'mid_risk': 0.022,   # 2.2% for 10-15% prob_late_60
        'high_risk': 0.030   # 3.0% for 15-20% prob_late_60
    },
    'p2p_platform_fees': {
        'low_risk': 0.020,   # 2.0%
        'mid_risk': 0.030,   # 3.0%
        'high_risk': 0.040   # 4.0%
    },
    'avg_invoice_values': {
        'institutional': 8500,  # £8,500 for supply chain factoring
        'p2p': 3200  # £3,200 for SME crowd pool
    },
    'risk_tier_distribution': {
        'low_risk': 0.40,   # 40% of eligible invoices
        'mid_risk': 0.40,   # 40%
        'high_risk': 0.20   # 20%
    },
    'credit_filters': {
        'max_prob_late_60': 0.15,  # 15% max late probability
        'min_confidence_score': 0.6,
        'model_hit_rate': 0.78,
        'credit_pass_rate': 0.65  # 65% of invoices pass credit filters
    },
    'loss_provisioning': {
        'expected_loss_rate': 0.025,  # 2.5% expected loss
        'insurance_coverage': 0.10,  # First-loss insurance covers bottom 10%
        'insurance_cost_bps': 50  # 50 basis points of financed volume
    },
    'attachment_rates': {
        'institutional_y2': 0.05,    # 5% of eligible invoices
        'institutional_y3_target': 0.15,  # 15% target
        'institutional_y5_target': 0.35,  # 35% mature state
        'p2p_y4': 0.03,              # 3% of eligible invoices
        'p2p_y5_target': 0.12        # 12% target
    }
}

# =============================================================================
# REGIONAL EXPANSION COEFFICIENTS
# =============================================================================
regional_params = {
    'uk': {
        'timing': 'Year 1 (Months 1-12)',
        'market_size_multiplier': 1.0,
        'status': 'Primary market - foundation'
    },
    'eu': {
        'timing': 'Year 2 (Months 13-24)',
        'market_size_multiplier': 2.3,
        'status': 'First international expansion',
        'key_markets': ['Germany', 'France', 'Netherlands', 'Ireland']
    },
    'us': {
        'timing': 'Year 3 (Months 25-36)',
        'market_size_multiplier': 4.1,
        'status': 'Major market expansion',
        'considerations': 'Entity setup required, different credit reporting ecosystem'
    },
    'apac': {
        'timing': 'Year 4-5 (Months 37+)',
        'market_size_multiplier': 1.8,
        'status': 'Long-term expansion',
        'key_markets': ['Singapore', 'Australia', 'Japan', 'Hong Kong']
    }
}

# =============================================================================
# TIER UPGRADE & EXPANSION RATES
# =============================================================================
upgrade_params = {
    'tier_upgrade_rates': {
        'standard_to_professional': {
            'conversion_rate': 0.18,  # 18% of eligible customers upgrade
            'avg_lag_months': 6,
            'eligibility_rate': 0.25  # 25% of Standard customers are eligible at any time
        },
        'professional_to_scale': {
            'conversion_rate': 0.09,  # 9% conversion rate
            'avg_lag_months': 9,
            'eligibility_rate': 0.20
        },
        'scale_to_enterprise': {
            'conversion_rate': 0.04,  # 4% conversion rate
            'avg_lag_months': 9,
            'eligibility_rate': 0.15
        }
    },
    'seat_expansion_rates': {
        'Professional': {
            'monthly_expansion_rate_early': 0.02,  # 2% of customers add seats (months <12)
            'monthly_expansion_rate_mature': 0.03,  # 3% mature rate (months 12+)
            'avg_extra_seats': 0.5
        },
        'Scale': {
            'monthly_expansion_rate_early': 0.025,  # 2.5%
            'monthly_expansion_rate_mature': 0.035,  # 3.5%
            'avg_extra_seats': 2.0
        },
        'Enterprise': {
            'monthly_expansion_rate_early': 0.03,  # 3%
            'monthly_expansion_rate_mature': 0.045,  # 4.5%
            'avg_extra_seats': 5.0
        }
    }
}

# =============================================================================
# NETWORK EFFECTS & VELOCITY
# =============================================================================
network_params = {
    'nvm_curve': {
        'year_1': 1.12,  # Network Value Multiplier
        'year_2': 1.35,
        'year_3': 1.68,
        'year_4': 1.98,
        'year_5': 2.34,
        'description': 'Network value multiplier increases as platform reaches critical mass'
    },
    'critical_mass_milestones': {
        'invoices_processed': 35800000,
        'unique_debtors': 1800000,
        'active_contributors': 4500,
        'data_hit_rate': 0.78
    }
}

# =============================================================================
# OTHER KEY DRIVERS
# =============================================================================
other_params = {
    'gross_margin': 0.85,  # 85% gross margin on software
    'start_date': '2025-01-01',
    'planning_horizon_months': 60,  # 5 years
    'currency': 'GBP'
}

# =============================================================================
# CONSOLIDATED PARAMETER OUTPUT
# =============================================================================
master_parameters = {
    'pricing': pricing_params,
    'cac': cac_params,
    'churn': churn_params,
    'volume_growth': volume_params,
    'token_economics': token_params,
    'invoice_finance': invoice_finance_params,
    'regional_expansion': regional_params,
    'upgrades_and_expansion': upgrade_params,
    'network_effects': network_params,
    'other': other_params,
    'metadata': {
        'version': '1.0',
        'created_date': '2025-01-15',
        'description': 'Master parameter configuration extracted from baseline financial model',
        'editable': True,
        'usage': 'Modify these parameters to run scenarios and sensitivity analysis'
    }
}

print("=" * 70)
print("MASTER PARAMETER CONFIGURATION")
print("=" * 70)
print(f"\nTotal Parameter Categories: {len(master_parameters) - 1}")
print(f"\n1. Pricing Parameters: {len(pricing_params)} tiers")
print(f"   • Standard: £{pricing_params['Standard']['monthly_price_gbp']}/mo")
print(f"   • Professional: £{pricing_params['Professional']['monthly_price_gbp']}/mo")
print(f"   • Scale: £{pricing_params['Scale']['monthly_price_gbp']}/mo")
print(f"   • Enterprise: £{pricing_params['Enterprise']['monthly_price_gbp']}/mo")
print(f"\n2. CAC Parameters: {len(cac_params)} acquisition channels")
print(f"   • Range: £{cac_params['stealth_partnerships']['avg_cac_gbp']} - £{cac_params['enterprise_outbound']['avg_cac_gbp']}")
print(f"\n3. Churn Parameters: {len(churn_params)} tiers")
print(f"   • Monthly churn range: {churn_params['Enterprise']['monthly_churn_rate']:.1%} - {churn_params['Standard']['monthly_churn_rate']:.1%}")
print(f"\n4. Volume Growth: {len(volume_params['gtm_phases'])} GTM phases defined")
print(f"\n5. Token Economics: {len(token_params)} parameter sets")
print(f"   • PAYG rate: £{token_params['pricing']['payg_rate_gbp']}/token")
print(f"   • Overage rate: £{token_params['pricing']['overage_rate_gbp']}/token")
print(f"\n6. Invoice Finance: {len(invoice_finance_params)} parameter sets")
print(f"   • Take rates: {invoice_finance_params['institutional_take_rates']['low_risk']:.1%} - {invoice_finance_params['institutional_take_rates']['high_risk']:.1%}")
print(f"   • Expected loss: {invoice_finance_params['loss_provisioning']['expected_loss_rate']:.1%}")
print(f"\n7. Regional Expansion: {len(regional_params)} markets")
print(f"   • Geographic multipliers: 1.0x (UK) → {regional_params['us']['market_size_multiplier']}x (US)")
print(f"\n8. Upgrade & Expansion: {len(upgrade_params['tier_upgrade_rates'])} upgrade paths")
print(f"   • Conversion rates: {upgrade_params['tier_upgrade_rates']['scale_to_enterprise']['conversion_rate']:.0%} - {upgrade_params['tier_upgrade_rates']['standard_to_professional']['conversion_rate']:.0%}")
print(f"\n9. Network Effects: Network Value Multiplier defined")
print(f"   • Year 1: {network_params['nvm_curve']['year_1']:.2f}x")
print(f"   • Year 5: {network_params['nvm_curve']['year_5']:.2f}x")
print(f"\n10. Other Parameters: Gross margin, timeline, currency")
print("\n" + "=" * 70)
print("✓ Parameter configuration complete - ready for scenario modeling")
print("=" * 70)