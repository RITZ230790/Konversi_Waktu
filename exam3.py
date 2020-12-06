def Urai (kata):
    hasil = ''
    for i in range(len(kata)+1):
        for j in range(i): 
            hasil += kata[j]
    return hasil

def Rajut (kata):
    hasil1 =''
    hasil = kata
    hasil1 += str(hasil[0])
    hasil = kata.split(kata[0])
    hasil1 += hasil[-1]
    return hasil1
    
    # for i in range(-1,-1 * len(kata)):
    #     for j in range(i):
    #         hasil -= kata[j]
    # return hasil

print(Urai('Code')) #=======> CCoCodCode 
print(Urai('Python')) #=====> PPyPytPythPythoPython
print(Urai('Purwadhika')) #=> PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika

print(Rajut('CCoCodCode')) #=============================================> Code
print(Rajut('PPyPytPythPythoPython')) #==================================> Python
print(Rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika')) #> Purwadhika