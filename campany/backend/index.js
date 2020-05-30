const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors")

//use express
var app = express();
//use cors
app.use(cors)



app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}))


//routers
const registerRoutes = require("./routes/register");
const signinRoutes = require("./routes/signin");
const listRoutes = require("./routes/list");
const listPostRoutes = require("./routes/listPost");
const listPutRoutes = require("./routes/listPut");
//session
const { checkToken } = require("./token/token_validation");


//files
app.use("/register",registerRoutes);
app.use("/signin",signinRoutes);
app.use("/list",listRoutes);
app.use("/listPost",checkToken,listPostRoutes);
app.use("/listPt",checkToken,listPutRoutes);

app.use((req,res)=>{
    res.status(404).send("<h1>Page not found</h1>");
})

app.listen(4000);
