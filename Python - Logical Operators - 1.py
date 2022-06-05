# Logical Operators

# Use the logical AND operator to combine two conditions.

# Set boolean variables to True or False.
has_high_income = False
has_good_credit = True
has_criminal_record = True

# Use the AND operator to determine if the buyer has a high income (has_high_income) AND good credit (has_good_credit). If both are True then print "Eligible for loan". Otherwise if either one is False then print "Not eligible for loan".
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# Use the OR operator to determine if the buyer has a high income (has_high_income) OR good credit (has_good_credit). If either is True then print "Eligible for loan". Otherwise, if both are False then print "Not eligible for loan".
if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# Use the AND NOT operator to determine if the buyer has a good credit (has_good_credit) AND NOT a criminal record (has_criminal_record). If has_good_credit is True AND has_criminal_record is False (NOT TRUE) then print "Eligible for loan". Otherwise, if has_good_credit is True and has_criminal_record is NOT False (and not) then print "Not eligible for loan".
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
