import java.rmi.Remote; 
import java.rmi.RemoteException; 

public interface Aluno extends Remote { 
    public void setNome(String nome) throws RemoteException; 
    public void setNotas(double n1, double n2, double n3) throws RemoteException;
    
    public String getNome() throws RemoteException; 
   
    public boolean aprovado() throws RemoteException;
}

    