const connection = require("../database/connection");
const express = require("express");
const Router = express.Router();
const bcrypt = require("bcrypt");
const { sign } = require("jsonwebtoken");

Router.post("/", (req, res, next) => {
  var username = req.body.username;
  var password = req.body.password;

  connection.query(
    "SELECT * FROM list WHERE username = ?",
    [username],
    (error, results, fields) => {
      if (error) {
        res.json({
          status: false,
          message: "there are some error with query"
        });
      } else {
        if (results.length > 0) {
          bcrypt.compare(password, results[0].password, function (err, ress) {
            if (!ress) {
              console.log(err);
              res.status(400).json({
                status: false,
                message: "username and password does not match"
              });
            } else {
              results.password = undefined;
              const jsontoken = sign({ results }, "qwe1234", {
                expiresIn: "1h"
              });
              return res.status(200).json({
                status: true,
                message: "successfully authenticated",
                token: jsontoken,
                username: username
              });
            }
          });
        } else {
          res.status(404).json({
            status: false,
            message: "username does not exits"
          });
        }
      }
    }
  );
  //   next();
});

module.exports = Router;
