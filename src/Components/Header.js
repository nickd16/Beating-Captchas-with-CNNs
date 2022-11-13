import React from 'react';


function Header(props){
return <div className='text-center mb-4 fade-in-text-fast'>
    <h1 className={props.font}>{props.name}</h1>
    </div>
};

export default Header;