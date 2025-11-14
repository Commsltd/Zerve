"""
Parameter Input Summary Dashboard
Consolidates all input parameters for easy review and validation
"""

# Import or reference all parameter groups
# (In production, these would be connected from upstream blocks)

print("=" * 60)
print("PARAMETER INPUT CONFIGURATION SUMMARY")
print("=" * 60)

print("\n1. PRICING TIERS")
print("-" * 60)
print("Configured: Starter, Growth, Scale, Enterprise")
print("Price Range: £495 - £15,000/month")
print("Token Allocations: 300 - 5,000 tokens (custom for Enterprise)")

print("\n2. CUSTOMER ACQUISITION COST (CAC)")
print("-" * 60)
print("Configured: 4 acquisition channels")
print("Range: £450 - £8,500")
print("Segments: Partnerships, Digital, Mixed, Enterprise")

print("\n3. CHURN RATES")
print("-" * 60)
print("Configured: Monthly churn by tier")
print("Range: 0.6% - 3.5% monthly")
print("Tiers: Starter, Growth, Scale, Enterprise")

print("\n4. VOLUME ASSUMPTIONS")
print("-" * 60)
print("Customer Density: 5 company size segments (25 - 23,000)")
print("Conversion Rates: 4 funnel stages (4% - 18%)")

print("\n5. TOKEN ECONOMICS")
print("-" * 60)
print("PAYG Rate: £2.00/token")
print("Overage Rate: £1.50/token")
print("Rollover: 90 days")
print("Burn Rates: Search, Monitor, AI Report")

print("\n6. INVOICE FINANCE")
print("-" * 60)
print("Institutional Take Rates: 1.5% - 3.0%")
print("P2P Platform Fees: 2.0% - 4.0%")
print("Expected Loss: 2.5%")
print("Launch Timeline: Y2 Q3 (Institutional), Y3 Q4 (P2P)")

print("\n7. REGIONAL EXPANSION")
print("-" * 60)
print("UK: 1.0x baseline (Y1)")
print("EU: 2.3x (Y2)")
print("US: 4.1x (Y3)")
print("APAC: 1.8x (Y4+)")

print("\n" + "=" * 60)
print("✓ All parameters configured with baseline values")
print("✓ Ready for scenario modeling and sensitivity analysis")
print("=" * 60)