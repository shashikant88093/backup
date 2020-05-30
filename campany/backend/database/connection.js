const mysql = require("mysql");
var mysqlConnnection = mysql.createConnection({
    host: 'localhost', 
    user: 'shash',
    password: 'Shash@123',
    database: 'company',
    multipleStatements: true,
    port: 3306,
    

});

mysqlConnnection.connect((err) => {
    if (!err) {
        console.log("db connected")
    } else {
        console.log("connection fail", err)
    }
})

// mysqlConnnection.query = util.promisify(mysqlConnnection.query);

module.exports = mysqlConnnection;