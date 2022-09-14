import java.rmi.Remote; 
import java.rmi.RemoteException; 

public interface Funcionario extends Remote { 
    public void setNome(String nome) throws RemoteException; 
    public void setCargo(String cargo) throws RemoteException;
    public void setSalario(double salario) throws RemoteException;
    
    public String getNome() throws RemoteException; 
    public String getCargo() throws RemoteException;
    public double getSalario() throws RemoteException;

    public double reajuste() throws RemoteException;
}

    

