import React from 'react';
import Tile from './Tile';

function Board(props){

return <div className='container text-center shadow-lg mb-2'>
    <div className='row g-0 justify-content-center m-0 mt-5'>
        
        <div className='col-sm-3 col-md-7 col-lg-8'> 
            <Tile img = {props.one}/> 
            <Tile img = {props.two}/> 
            <Tile img = {props.three}/>
        </div>
        <div className='col-sm-3 col-md-7 col-lg-8'> 
            <Tile img = {props.four}/> 
            <Tile img = {props.five}/> 
            <Tile img = {props.six}/>
        </div>
        <div className='col-sm-3 col-md-7 col-lg-8'> 
            <Tile img = {props.seven}/> 
            <Tile img = {props.eight}/> 
            <Tile img = {props.nine}/>
        </div>
        
        
    </div>

</div>


}

export default Board


