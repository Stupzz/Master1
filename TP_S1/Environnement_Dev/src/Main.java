import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;
import javax.mail.*;
import javax.mail.internet.AddressException;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class Main {

    public static Personne getNameFromMail(String mail){
        //récupère le nom et le prenom d'une personne en fonction de son mail de type:
        // nom.prenom@xxx.xx
        String nomPrenom = mail.split("@")[0];
        //System.out.println(nomPrenom);
        String[] noms = nomPrenom.split("\\.");
        String prenom = noms[0];
        String nom = noms[1];

        return new Personne(nom, prenom);
    }

    public static List<Personne> lectureFicherEmployer(File fichier){
        //Genere une liste de personne depuis un fichier csv
        List<Personne> listEmployer = new ArrayList<>();
        try {
            BufferedReader br = new BufferedReader(new FileReader(fichier));
            String line;
            line = br.readLine(); //lecture de la première ligne qui indique les catégories
            while ((line = br.readLine()) != null) {
                String[] mots = line.split(",");
                if (mots.length >= 2){
                    String mail = mots[0];
                    System.out.println(mail);
                    String[] dates = mots[1].split("/");
                    if (dates.length == 3){
                        Date dateNaissance = new Date(Integer.parseInt(dates[0]), Integer.parseInt(dates[1]), Integer.parseInt(dates[2]));
                        InformationEmployer infoPersonne = new InformationEmployer(mail, dateNaissance);

                        Personne employer = getNameFromMail(mail);
                        employer.setInfo(infoPersonne);
                        listEmployer.add(employer);
                    }
                }
            }
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return listEmployer;
    }

    static void envoieMail(Personne personne){
        //envoie un mail à la personne spécifier
        try{

            Properties props = new Properties();
            props.put("mail.smtp.auth", "true");
            props.put("mail.smtp.starttls.enable","true");
            props.put("mail.smtp.host","smtp.gmail.com");
            props.put("mail.smtp.port","587");
            Session session = Session.getInstance(props,
                    new javax.mail.Authenticator() {
                        protected PasswordAuthentication getPasswordAuthentication() {
                            return new PasswordAuthentication("m.carbonnier73@gmail.com", "**************");
                            //remplacer les *** par mdp d'application
                        }
                    });


            //Le message
            Message     message     = new MimeMessage(session);
            InternetAddress recipient   = new InternetAddress(personne.getInfo().getMail());//***
            message.setRecipient(Message.RecipientType.TO, recipient);
            message.setSubject("L'entreprise vous souhaite un bon anniversaire!");
            message.setText("Bon anniversaire " + personne.toString() + "!");

            //Transport
            Transport.send(message);
        }catch(NoSuchProviderException e) {
            System.err.println("Pas de transport disponible pour ce protocole");
            System.err.println(e);
        }
        catch(AddressException e) {
            System.err.println("Adresse invalide");
            System.err.println(e);
        }
        catch(MessagingException e) {
            System.err.println("Erreur dans le message");
            System.err.println(e);
        }

    }

    public static Date aujourdhui() {
        //Nous donne la date d'aujourd'hui
        java.util.Date date = new java.util.Date();
        String[] dates = new SimpleDateFormat("dd/MM/yyyy").format(date).split("/");
        return new Date(Integer.parseInt(dates[0]), Integer.parseInt(dates[1]), Integer.parseInt(dates[2]));
    }



    public static void main(String[] args) {

        File fichier = new File("adresse_mail.csv");
        List<Personne> listEmployer = lectureFicherEmployer(fichier);
        for (Personne personne : listEmployer) {
            if (personne.estJourAnniverssaire(aujourdhui())) {
                envoieMail(personne);
            }
        }
    }
}
