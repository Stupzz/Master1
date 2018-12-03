public class Personne {
    private String nom;
    private String prenom;
    private InformationEmployer info;

    public Personne(String nom, String prenom) {
        this.nom = nom;
        this.prenom = prenom;
    }

    public Personne(String nom, String prenom, InformationEmployer info) {
        this.nom = nom;
        this.prenom = prenom;
        this.info = info;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public InformationEmployer getInfo() {
        return info;
    }

    public void setInfo(InformationEmployer info) {
        this.info = info;
    }

    public boolean estJourAnniverssaire(Date date){
        //donne une date, et dit si cette date correspond à son anniversaire
        if (date.getMois() == info.getDateNaissance().getMois()) {
            if (date.getJour() == info.getDateNaissance().getJour()) return true;
        }
        return false;
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append(nom).append(" ").append(prenom);
        return sb.toString();
    }
}
