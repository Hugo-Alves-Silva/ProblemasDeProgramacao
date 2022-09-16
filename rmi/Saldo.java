import java.rmi.Remote; 
import java.rmi.RemoteException; 

public interface Saldo extends Remote { 
    public void setSaldoMedio(double saldo) throws RemoteException; 
    public double getCredito() throws RemoteException;
}

    