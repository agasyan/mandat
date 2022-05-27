db.createUser(
    {
        user: "mandat",
        pwd: "mandat",
        roles:[
            {
                role:"readWrite",
                db:"mandat-db"
            }
        ]
    }
)