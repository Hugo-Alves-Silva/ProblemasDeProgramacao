import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class SaldoImpl extends UnicastRemoteObject implements Saldo {
    
    private double saldoMedio;

    public SaldoImpl() throws RemoteException {
        super();
    }
    public void setSaldoMedio(double saldo){
        this.saldoMedio = saldo;
    } 
    
    public double getCredito(){
        if(this.saldoMedio >= 0.0 && this.saldoMedio <= 200.0)
            return 0.0;    
        else if(this.saldoMedio >= 0.0 && this.saldoMedio <= 200.0)
            return this.saldoMedio * 0.2;    
        else if(this.saldoMedio >= 0.0 && this.saldoMedio <= 200.0)
            return this.saldoMedio * 0.3;    
        else
            return this.saldoMedio * 0.4;    
    }
   

    
    public static void main(String[] args) { 
        try { 
            Saldo obj = new SaldoImpl(); 
            Naming.rebind("//localhost/SaldoServer", obj); 
        } catch (Exception e) { 
            System.out.println("err: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
    } 
}