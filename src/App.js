import React, {useState, useEffect} from 'react'
import Header from './Components/Header';
import Board from './Components/Board';
import Description from './Components/Description';
import Button from './Components/Button';
import GameButton from './Components/gameButton';

function App() {
  
  const [data,setData] = useState([{}])
  useEffect(()=>{
    fetch('/').then(
      res => res.json()
    ).then(
      data=> {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  

  return (<div>
    <Header name="Beating Captcha" font="title"/> 
    <Description />
    <Board />
    <Button name="AI Demo" post="/"/>
    <GameButton name="Play Now"/>    
  </div>)
  
  

}

export default App;
