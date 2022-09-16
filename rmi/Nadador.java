import java.rmi.Remote; 
import java.rmi.RemoteException; 

public interface Nadador extends Remote { 
    public void setIdade(int idade) throws RemoteException; 
    public String getCategoria() throws RemoteException;
}

    