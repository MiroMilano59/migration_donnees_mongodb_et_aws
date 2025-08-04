// On se connecte à la base healthcare_db (elle sera créée si elle n'existe pas)
db = db.getSiblingDB("healthcare_db");

// On crée un utilisateur en lecture seule
db.createUser({
  user: "readonly_user",
  pwd: "readonly123",
  roles: [
    {
      role: "read",
      db: "healthcare_db"
    }
  ]
});
