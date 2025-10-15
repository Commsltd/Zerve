"""
Customer Density by Segment
Source: Account density model - customers/debtors per account by company size
"""

customer_density = {
    'micro': {
        'avg_customers_per_account': 25,
        'segment_description': 'Micro businesses (1-9 employees)',
        'typical_characteristics': 'Small customer base, local operations'
    },
    'small': {
        'avg_customers_per_account': 35,
        'segment_description': 'Small businesses (10-49 employees)',
        'typical_characteristics': 'Growing customer base, regional presence'
    },
    'medium': {
        'avg_customers_per_account': 210,
        'segment_description': 'Medium businesses (50-249 employees)',
        'typical_characteristics': 'Established customer base, national operations'
    },
    'large': {
        'avg_customers_per_account': 1325,
        'segment_description': 'Large enterprises (250-999 employees)',
        'typical_characteristics': 'Extensive customer base, multi-national'
    },
    'mnc': {
        'avg_customers_per_account': 23000,
        'segment_description': 'Multinational corporations (1000+ employees)',
        'typical_characteristics': 'Massive customer base, global operations'
    }
}

print("Customer Density Model Defined")
print("Average customers/debtors per account by segment:")
for _seg_name, _seg_info in customer_density.items():
    _avg_cust = _seg_info['avg_customers_per_account']
    print(f"  {_seg_name.capitalize()}: {_avg_cust:,} customers/debtors per account")