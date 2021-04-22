import React, { Component } from 'react'
import { CardItems } from './CardItems';
import './Cards.css'
 
class Cards extends Component {
    
    render() {
        return (
            <div>
                <div className="cards">
                    {CardItems.map((item, index) => {
                        return (
                            <div key={index} id="card-id" className="item-card">
                                <a href={item.path}>
                                        <figure>
                                            <img src={item.image} alt={item.alt} /> 
                                            <svg id="card" className="main-svg" 
                                                viewBox="0 0 180 320" preserveAspectRatio="none">
                                                <path d="M 180,160 0,218 0,0 180,0 z" />
                                            </svg>
                                            <figcaption>
                                                <div className="icon">
                                                    {item.icon}
                                                </div>
                                                <p>{item.description}</p>
                                            </figcaption>
                                        </figure>
                                </a>
                            </div>
                        )
                    })}
                </div>
            </div>
        )   
    }
}



export default Cards; 
