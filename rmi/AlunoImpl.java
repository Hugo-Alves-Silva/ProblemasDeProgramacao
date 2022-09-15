import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class AlunoImpl extends UnicastRemoteObject implements Aluno {
    private String nome;
    private double n1, n2, n3;

    public AlunoImpl() throws RemoteException {
        super();
    }
    public void setNotas(double n1, double n2, double n3){
        this.n1 = n1;
        this.n2 = n2;
        this.n3 = n3;
    } 
    public void setNome(String nome){
        this.nome = nome;
    }
   
    
    public String getNome(){
        return this.nome;
    }
   

    public boolean aprovado(){
        double m = (this.n1 + this.n2)/2;
        if(m >= 7.0) return true;
        else if(m <= 3.0) return false;
        else{
            if((m + this.n3)/2 >= 5.0) return true;
            else return false;
        }
        

        
    }
    
    public static void main(String[] args) { 
        try { 
            Aluno obj = new AlunoImpl(); 
            // Bind this object instance to the name "HelloServer" 
            Naming.rebind("//localhost/AlunoServer", obj); 
            System.out.println("AlunoServer bound in registry"); 
        } catch (Exception e) { 
            System.out.println("AlunoImpl err: " + e.getMessage()); 
            e.printStackTrace(); 
        } 
    } 
}