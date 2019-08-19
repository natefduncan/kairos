import './App.css';
import Loginscreen from './Loginscreen';
import React, { Component } from 'react';

class App extends Component {
  
  //Constructor Statement
  //Declares the variables. 
  constructor(props){
    super(props);
    this.state={
      loginPage:[],
      uploadScreen:[]
    }
  }
  
  //Component will mount statement.
  //See comments below for LifeCycle Methods. 
  //Adds the login page to the props. 
  componentWillMount(){
    var loginPage =[];
    loginPage.push(<Loginscreen parentContext={this}/>);
    this.setState({
                  loginPage:loginPage
                    })
  }
  
  //Render statement. 
  //Renders the Login page and the Upload screen. 
  //Isn't the upload screen blank, though? 
  render() {
    return (
      <div className="App">
        {this.state.loginPage}
        {this.state.uploadScreen}
      </div>
    );
  }

//End of component  
}

export default App;

/* 
COMPONENT WILL MOUNT

This method is only called one time, which is before the initial render. Since this method is called before render() our 
Component will not have access to the Native UI (DOM, etc.). We also will not 
have access to the children refs, because they are not created yet.

The componentWillMount() is a chance for us to handle configuration, update our state, and in general prepare for the first render. At this point, props and initial state are defined. We can safely query this.props and this.state, knowing with certainty they are the current values. 
This means we can start performing calculations or processes based on the prop values.

https://developmentarc.gitbooks.io/react-indepth/content/life_cycle/birth/premounting_with_componentwillmount.html

*/