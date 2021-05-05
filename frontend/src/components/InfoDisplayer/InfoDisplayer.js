import React, { Component } from 'react';
import './InfoDisplayer.css';

class InfoDisplayer extends Component {

    constructor(props){
        super(props)
        this.state={
            infoList: []
        }
    }

    // transform if json is string and update 
    transform = (response) => {
        if(typeof(response) ==='string'){
            const json = JSON.parse(response)
            response = json
        }
        const keys = Object.keys(response)
        let ref = [...this.state.infoList]
        keys.forEach(key =>{
            if (Array.isArray(response[key])){
                const text = response[key][0]
                ref.push([key, text])
            }else{
                ref.push([key, response[key]])    
            }
        })
        return ref
    }
    
    // at end of animation remove error from list
    excludeInfo = (item) => {
        let ref = this.state.infoList.filter(x => x !== item)
        return ref
    }

    updateInfo = (response) => {
        let updated = this.transform(response)
        this.setState({infoList : updated})
    }

    deleteInfo = (item) => {
        let deleted = this.excludeInfo(item)
        this.setState({infoList : deleted})
    }
    
    render() {
        return (
            <div className='info-box'>
                {this.state.infoList.map((item, index) => {
                    return (
                        <div className="info" 
                            id="info-id"
                            onAnimationEnd={()=> this.deleteInfo(item)}
                            onClick={() => this.deleteInfo(item)}
                            key={index}>
                            <h6>{item[0]}</h6> 
                            <p>{item[1]}</p> 
                       </div>
                    )
                })}
            </div>
        )
    }
}

export default InfoDisplayer;
