const express = require('express');
const Router = express.Router();

const Sequlize = require("../database/connection");

Router.put("/:id",(req,res,next)=>{

    let lists ={
        "Task_name":req.body.Task_name,
        "value":req.body.value,
        "Progess":req.body.priority,
        "comment": req.body.comment,
        "priority":req.body.priority
    }
    Sequlize.query(
        "INSERT INTO lists SET ?" ,lists, (err,rows,fields)=>{
            if(!err){
              res.status(200).send(rows)  
            }else{
                res.satus(404).send(err)
            }
        }
    )

})


module.exports = Router;