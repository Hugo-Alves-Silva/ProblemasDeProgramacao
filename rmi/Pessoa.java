import java.rmi.Remote; 
import java.rmi.RemoteException; 

public interface Pessoa extends Remote { 
    public void setNome(String nome) throws RemoteException; 
    public void setSexo(String sexo) throws RemoteException; 
    public void setAltura(double altura) throws RemoteException; 


    public String getNome() throws RemoteException; 
    public String getSexo() throws RemoteException; 
    public double getAltura() throws RemoteException; 
   
    public double pesoIdeal() throws RemoteException;
}

    