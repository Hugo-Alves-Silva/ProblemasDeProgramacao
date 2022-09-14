import java.rmi.Remote; 
import java.rmi.RemoteException; 

public interface Maioridade extends Remote { 
    public void setNome(String nome) throws RemoteException; 
    public void setSexo(String cargo) throws RemoteException;
    public void setIdade(int idade) throws RemoteException;
    
    public String getNome() throws RemoteException; 
    public String getSexo() throws RemoteException;
    public double getIdade() throws RemoteException;

    public boolean atingiuMaioridade() throws RemoteException;
}

    