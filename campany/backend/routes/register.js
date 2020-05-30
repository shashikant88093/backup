const connection = require('../database/connection');
const express = require('express')
const Router = express.Router();
const bcrypt = require('bcrypt')


Router.post('/', (req, res, next) => {
    let list = {
        "username": req.body.username,
        "email": req.body.email,
        "password": req.body.password,
        "id": req.body.id,
        "phone": req.body.phone,
        "gender": req.body.gender

    }
    var user = list;
    bcrypt.hash(req.body.password, 10, (err, hash) => {
        if (err) console.log(err);
        user.password = hash;
        connection.query('INSERT INTO list SET ?', list,
            (error, results, fields) => {
                if (error) {
                    console.log(error)
                    res.status(404).json({
                        status: false,
                        message: 'there are some error with query'
                    })
                } else {
                    console.log(results)
                    res.json({
                        status: true,
                        data: results,
                        message: 'user registered sucessfully'
                    })
                }
            })

    })
})
module.exports = Router;