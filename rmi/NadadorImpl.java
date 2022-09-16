import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class NadadorImpl extends UnicastRemoteObject implements Nadador {
    
    private int idade;

    public NadadorImpl() throws RemoteException {
        super();
    }
    public void setIdade(int idade){
        this.idade = idade;
    } 
    
    public String getCategoria(){
        if(this.idade >= 5 && this.idade <= 7){
            return "infantil A";
        }else if(this.idade >= 8 && this.idade <= 10){
            return "infantil B";
        }else if(this.idade >= 11 && this.idade <= 13){
            return "juvenil A";
        }else if(this.idade >= 14 && this.idade <= 17){
            return "juvenil B";
        }else{
            return "adulto";
        }
    }
   

    
    public static void main(String[] args) { 
        try { 
            Nadador obj = new NadadorImpl(); 
            Naming.rebind("//localhost/NadadorServer", obj); 
        } catch (Exception e) { 
            System.out.println("err: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
    } 
}