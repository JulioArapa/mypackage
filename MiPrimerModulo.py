def Suma5(a,b,c,d,e):
  return a+b+c+d+e

def Potencia5(a,b,c,d,e):  
  return pow(a,2), pow(b,2), pow(c,2), pow(d,2), pow(e,2)

def Raiz5(a,b,c,d,e):  
  return pow(a,0.5), pow(b,0.5), pow(c,0.5), pow(d,0.5), pow(e,0.5)

def Varianza5(a,b,c,d,e):
  med=(a+b+c+d+e)/5
  sum_cuadrados=(a-med)**2 + (b-med)**2 + (c-med)**2 + (d-med)**2 + (e-med)**2
  varianza= sum_cuadrados/4
  return varianza

def asimetria_curtosis5(a,b,c,d,e):
    med=(a+b+c+d+e)/5
    suma_cuadrados=(a-med)**2 + (b-med)**2 + (c-med)**2 + (d-med)**2 + (e-med)**2
    ds=(suma_cuadrados/4)**0.5
    coef_asim=(1/5)*((a-med)/ds)**3 + ((b-med)/ds)**3 + ((c-med)/ds)**3 + ((d-med)/ds)**3 + ((e-med)/ds)**3
    curtosis=(1/5)*((a-med)/ds)**4 + ((b-med)/ds)**4 + ((c-med)/ds)**4 + ((d-med)/ds)**4 + ((e-med)/ds)**4
    return coef_asim, curtosis
