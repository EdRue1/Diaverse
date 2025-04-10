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
//home page
app.get('/home',function (req, res) {
    res.render('pages/home')
});

app.get('/success', function (req, res) {
    res.render('pages/success');
});

// a test to check applicants
app.get('/allapplicants',function (req, res) {

    //res.send('I made it this far');

    axios.get('http://18.227.183.161:5000/data')
    .then((response)=>{
        a_items = response.data;
        console.log(a_items);
        res.render('pages/all_applicants',{
            Applicants:a_items
        });
    });
})

// ADD APPLICANT
// First display the page
app.get('/applicantform', function (req, res) {
    res.render('pages/applicantform');
});

// Then send the information
app.post('/applicantform', function (req, res) {
    var message1 = req.body.AFirstName;
    var message2 = req.body.ALastName;
    var message3 = req.body.DOB;
    var message4 = req.body.Address;
    var message5 = req.body.ACity;
    var message6 = req.body.AState;
    var message7 = req.body.ZipCode;
    var message8 = req.body.Email;
    var message9 = req.body.APhone;
    var message10 = req.body.SSN;
    var message11 = req.body.USCitizen;
    var message12 = req.body.EligWork;
    var message13 = req.body.CertifyTrue;
    var message14 = req.body.Authorize;
    var message15 = req.body.NoFalseInfo;
    var message16 = req.body.DigitalSign;
    var message17 = req.body.SchoolName;
    var message18 = req.body.ECity;
    var message19 = req.body.EState;
    var message20 = req.body.Degree;
    var message21 = req.body.Major;
    var message22 = req.body.EStartYear;
    var message23 = req.body.EEndYear;
    var message24 = req.body.OtherCerts;
    var message25 = req.body.PCompanyName;
    var message26 = req.body.PCity;
    var message27 = req.body.PState;
    var message28 = req.body.Position;
    var message29 = req.body.Duties;
    var message30 = req.body.PStartYear;
    var message31 = req.body.PEndYear;
    var message32 = req.body.Supervisor;
    var message33 = req.body.ReaForLeav;
    var message34 = req.body.MayContact;
    var message35 = req.body.RFirstName;
    var message36 = req.body.RLastName;
    var message37 = req.body.Title;
    var message38 = req.body.RCompanyName;
    var message39 = req.body.RPhone;

    var initial_api = 'http://127.0.0.1:5000/add'

    axios.post(initial_api, {
        AFirstName: message1, 
        ALastName: message2, 
        DOB: message3, 
        Address: message4,
        ACity: message5,
        AState: message6,
        ZipCode: message7,
        Email: message8,
        APhone: message9,
        SSN: message10,
        USCitizen: message11,
        EligWork: message12,
        CertifyTrue: message13,
        Authorize: message14, 
        NoFalseInfo: message15,
        DigitalSign: message16,
        SchoolName: message17,
        ECity: message18,
        EState: message19,
        Degree: message20,
        Major: message21,
        EStartYear: message22,
        EEndYear: message23,
        OtherCerts: message24,
        PCompanyName: message25,
        PCity: message26,
        PState: message27,
        Position: message28,
        Duties: message29,
        PStartYear: message30,
        PEndYear: message31,
        Supervisor: message32,
        ReaForLeav: message33,
        MayContact: message34,
        RFirstName: message35,
        RLastName: message36,
        Title: message37,
        RCompanyName: message38,
        RPhone: message39
    })
    .then((response) => {
        console.log(response.data);
        res.render('pages/success');
    })

});

//LOGIN
// First display the page
app.get('/login', function (req, res) {
    res.render('pages/login');
});

//send login to backend
app.post('/process_login', function(req, res){
    var user = req.body.username;
    var password = req.body.password;

    var initial_api = "http://127.0.0.1:5000/process_login"
    axios.post(initial_api, {
        Username: user, 
        Pword: password
      
    })
    .then((response) => {
        console.log(response.data);

        if (response.data.message == 'Login Successful') {
            res.render('pages/continue');
        }
        else {
            res.render('pages/error', { message: 'Incorrect password' });
        }
        
    })
    .catch((error) => {
        console.log(error);
        res.render('pages/error', { message: 'An error occurred while logging in' });
    });


  });

app.listen(port, () => console.log(`MasterEJS app Started on port ${port}!`));