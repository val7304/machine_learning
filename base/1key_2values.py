# dictionnaire de dictionnaire
D = {'a':12, 'b':{'t':56,'v':89}, 'c':11}
 
print (D['b']['v'])# 89


acide_amine = {'Phe':('UUU','UUC'),
               'Val':('GUU','GUC','GUA','GUG')}
 
def valid_codons(key,val):
    return val in acide_amine[key]
 
valid_codons('Phe','GUG')
# False
valid_codons('Phe','UUC')
# True