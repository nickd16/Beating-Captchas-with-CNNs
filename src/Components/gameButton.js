import React from 'react';
import ReactDom from 'react-dom';
import Header from './Header';
import Board from './Board';
import Button from './Button';


function GameButton(props){

    function GameScreen (){

        var level = 1;
        var currentLevel = 'Level ' + level;

        ReactDom.render(<div>

            <div className='mb-5 '>
                <Header font="game-title" name ="Select All ___"/>
            </div>

            <div className='row justify-content-center mt-5 m-0'>
                <div className='col-md-2 col-lg-5 m-0'>
                    <Board />
                </div>
                <div className='col-md-2 col-lg-5 m-0'>
                    <Board />
                </div>
            </div>

            <div className='mt-5'>
                <Button name = {currentLevel}/>
            </div>
            

        </div>,document.getElementById("root"));
    }


    return <div className='row text-center'>
            <div className='col-lg-12 m-3 mb-2'>
                <button type='submit' onClick={GameScreen} className='wiggle-button button fs-4 main-font text-dark shadow-lg p-3'> {props.name}</button>
            </div>
                
            
    </div>
}

export default GameButton;