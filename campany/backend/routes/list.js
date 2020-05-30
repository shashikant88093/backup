const express = require('express');
const Router = express.Router();

const Sequlize = require("../database/connection");

Router.get("/", (req, res, next) => {
    Sequlize.query(
        "SELECT * FROM lists ", (err, rows, fields) => {
            if (!err) {
                res.status(200).send(rows)
            } else {
                res.satus(404).send(err)
            }
        }
    )

})


module.exports = Router;