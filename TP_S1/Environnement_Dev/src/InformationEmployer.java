public class InformationEmployer {
    private String mail;
    private Date dateNaissance;

    public InformationEmployer(String mail, Date dateNaissance) {
        this.mail = mail;
        this.dateNaissance = dateNaissance;
    }

    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }

    public Date getDateNaissance() {
        return dateNaissance;
    }

    public void setDateNaissance(Date dateNaissance) {
        this.dateNaissance = dateNaissance;
    }
}
