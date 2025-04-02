const express = require('express')
var path = require('path');
var bodyParser = require('body-parser');
const app = express();
const port = 3000;
var a_items = null;
var cl_items = null;
var t_items = null;
var ch_items = null;

const axios = require('axios');
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
//setup public folder
app.use(express.static('./public'));
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
// parse application/json
app.use(bodyParser.json());

//home page
app.get('/',function (req, res) {
    res.render('pages/home')
});

// a test to check applicants
app.get('/allapplicants',function (req, res) {

    //res.send('I made it this far');

    axios.get('http://127.0.0.1:5000/data')
    .then((response)=>{
        a_items = response.data;
        console.log(a_items);
        res.render('pages/all_applicants',{
            Applicants:a_items
        });
    });
})


app.listen(port, () => console.log(`MasterEJS app Started on port ${port}!`));