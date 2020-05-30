const { verify } = require("jsonwebtoken")

module.exports = {
  checkToken: (req, res, next) => {
    let token = req.headers['x-access-token'] || req.headers['authorization']; // Express headers are auto converted to lowercase
    if (token) {
      // Remove Bearer from string
      token = token.slice(7, token.length);
    }

    // console.log(req.headers['authorization'])
    
    // console.log();
    
    // console.log(token);
    // console.log(req.body);
    

    if (token) {
      verify(token, "qwe1234", (err, decoded) => {
        if (err) {
          let data= {
            success: false,
            message: 'Token is not valid'
          }
          res.status(401).send(data)
        } else {
          req.decoded = decoded;
          next();
        }
      });
    } else {
      return res.json({
        success: false,
        message: 'Auth token is not supplied'
      });
    }
  }
}