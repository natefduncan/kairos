import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RaisedButton from 'material-ui/RaisedButton';
import Login from './Login';
import Register from './Register';

class Loginscreen extends Component {
  
  //Create props: Login Screen, login message, button label, isLogin. 
  constructor(props){
    super(props);
    this.state={
      username:'',
      password:'',
      loginscreen:[],
      loginmessage:'',
      buttonLabel:'Register',
      isLogin:true
    }
    //End of constructor
  }
  
  //Component Will Mount. LifeCycle method.
  //This prepares for the first render. 
  componentWillMount(){
    //Declare login variable. 
    var loginscreen=[]; //You declare a variable that you can then put in the props. 

    //Add the login box to the login screen variable. 
    loginscreen.push(<Login parentContext={this} appContext={this.props.parentContext}/>);
    
    //Create the login message variable. 
    var loginmessage = "Not registered yet, Register Now";
    
    //Set the state of the login screen and the message. 
    this.setState({
                  loginscreen:loginscreen,
                  loginmessage:loginmessage
                 })
//End of Component Will Mount
  }
  
  
  render() {
    //Render the login screen and message. 
    return (
      <div className="loginscreen">
        {this.state.loginscreen}
        <div>
          {this.state.loginmessage}
          <MuiThemeProvider>
            <div>
               <RaisedButton label={this.state.buttonLabel} primary={true} style={style} onClick={(event) => this.handleClick(event)}/>
           </div>
          </MuiThemeProvider>
        </div>
      </div>
    );
  //End of render. 
  }
  
  //this is the function that tells what to do when element is clicked. 
  handleClick(event) {
    // console.log("event",event);
    // Declare variable. Login message. 
    var loginmessage;
    
    
    if(this.state.isLogin){
      var loginscreen=[];
      loginscreen.push(<Register parentContext={this}/>);
      loginmessage = "Already registered.Go to Login";
      this.setState({
                     loginscreen:loginscreen,
                     loginmessage:loginmessage,
                     buttonLabel:"Login",
                     isLogin:false
                   })
    } else {
      var loginscreen=[];
      loginscreen.push(<Login parentContext={this}/>);
      loginmessage = "Not Registered yet.Go to registration";
      this.setState({
                     loginscreen:loginscreen,
                     loginmessage:loginmessage,
                     buttonLabel:"Register",
                     isLogin:true
                   })
    }
//End of handle click 
}

//End of component. 
}
const style = {
  margin: 15,
};
export default Loginscreen;