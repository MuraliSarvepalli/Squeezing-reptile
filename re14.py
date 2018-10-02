import re
ph=['9789874837','9043540131','8056205399','9442535649','59665','7418281614','866769692']
for i in range(0,len(ph)-1):
    if re.match(r'(^[89]\d{9})',ph[i]):
        print (ph[i])
    else:
        print (ph[i],'Invalid Number')
