from cuenta_ahorro import CuentaAhorro
def main():
    cuenta1 = CuentaAhorro("Jose Reyes", 1000) # aca creamos el objeto que pertenece a la sub clase CuentaAhorro y por ende hereda los atributos de la clase padre Cuenta
    print(f"El nombre del titular es {cuenta1.titular}")
    print(f"El saldo es: ${cuenta1.saldo}")
    print(f"La tasa de interes es: ${cuenta1.tasa_interes * 100}%")
    
    cuenta1.depositar(500)
    cuenta1.retirar(200)
    cuenta1.aplicar_interes()
    
    print(f"El saldo es: ${cuenta1.saldo}")
    
if __name__ == "__main__":
    main()    