//Import axios and React. 
import React from 'react';
import axios from 'axios';

//Import themes. 
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import RaisedButton from 'material-ui/RaisedButton';
import TextField from 'material-ui/TextField';

class Login extends Component {
  
//Create constructor with username nad password. 
constructor(props){
  super(props);
  this.state={
  username:'',
  password:''
  };
 }
 
//Render variable that updates username and password with each keystroke. 
render() {
    return (
      <div>
        <MuiThemeProvider>
          <div>
          <AppBar
             title="Login"
           />
           <TextField
             hintText="Enter your Username"
             floatingLabelText="Username"
             onChange = {(event,newValue) => this.setState({username:newValue})}
             />
           <br/>
             <TextField
               type="password"
               hintText="Enter your Password"
               floatingLabelText="Password"
               onChange = {(event,newValue) => this.setState({password:newValue})}
               />
             <br/>
             <RaisedButton label="Submit" primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
         </div>
         </MuiThemeProvider>
      </div>
    );
  }
}

//Handle Click Event by attempting to authenticate. 
handleClick(event){
 var login_url = "http://localhost:8000/api/rest-auth/login/";
 var self = this;
 var payload={
   "email":this.state.username,
   "password":this.state.password
 }
 
 componentDidMount() {
 axios.post(login_url, payload)
    .then(function (response) {
        console.log(response);
        if(response.data.code == 200){
            console.log("Login successfull");
            var uploadScreen=[];
            uploadScreen.push(<UploadScreen appContext={self.props.appContext}/>)
            self.props.appContext.setState({loginPage:[],uploadScreen:uploadScreen})
        } else if(response.data.code == 204) {
            console.log("Username password do not match");
            alert("Username/password do not match")
        } else {
            console.log("Username does not exists");
            alert("Username does not exist");
        }
    })
 }
 
 //End of click event. 
 }

const style = {
 margin: 15,
};

export default Login;
