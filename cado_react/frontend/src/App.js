
import React, { Component } from 'react'

class App extends Component {
   state = {
      cados: []
   };

   async componentDidMount() {
      try {
         const res = await fetch('http://127.0.0.1:8000/api/'); //Replace this with global variable at some point. 
	 console.log(res);
	 const cados = await res.json();
	 this.setState({
	    cados
	 });
      } catch (e) {
         console.log(e);
      }
   }

   render() {
      return (
         <div>
	      {this.state.cados.map(item => (
		   <div key = {item.cado_id}>
		   <h1> {item.batch_id}</h1>
		   <span> {item.url} </span>
		   </div>
	      ))}
	</div>
      );
   }
}

export default App;

