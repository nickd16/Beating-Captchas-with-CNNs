import React from 'react';



function Button(props){

return <div className='row text-center'>
            <div className='col-lg-12 m-3 mb-2'>
                <button type='submit' className=' button fs-4 main-font text-dark shadow-lg p-3'> {props.name}</button>
            </div>
                
            
    </div>
    
    
    
    


}


export default Button;