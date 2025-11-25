def generate_test_cases(query, context):

    output = f"""
### Test Cases for: {query}

Using Context:
{context}

1. **Valid Discount Code**
   - Step: Enter SAVE15
   - Expected: 15% discount applied
   - Source: product_specs.md

2. **Invalid Discount Code**
   - Step: Enter WRONG
   - Expected: 'Invalid discount code'
   - Source: product_specs.md

3. **Empty Required Fields**
   - Step: Submit without Name/Email/Address
   - Expected: Red validation errors
   - Source: ui_ux_guide.txt
    """

    return output
