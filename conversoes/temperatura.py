
def celsius (temp:float):
    result = float(0);

    result = (temp * 1.8 ) +32
    
    print (f" o resultado em celsius é {result}");
    return result;

def fahrenheit(temp:float):
    result = float(0);

    result = (temp - 32 )/ 1.8

    print(f" o resultado em fahrenheit é {result}.");
    return result;

