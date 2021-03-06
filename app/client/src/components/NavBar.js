import React from 'react';
import {Link} from "react-router-dom";


/**
 * This component represents the navigation bar for the website. Its meant to be a presentational
 * component. 
 * @class
 * @public 
 */
class NavBar extends React.Component {
    constructor(props) {
        super(props); 
    }
    render() {
        return(
            <div id = "NavBar_Container">
                <div id = "NavBar">
                    <div id = "DescriptionInfo">
                        <h2>Superhero & Pokémon Machine Learning</h2>
                        <img id = "navbarIcon" className="greyscale" src = "https://cloud.githubusercontent.com/assets/1094151/17297177/9f256f96-57d2-11e6-86fc-6eef2ba19fee.png" alt = "Pokeball"></img>
                    </div>
                    <div id = "NavigationLinks">
                        <Link to = "/" id="Recognize">Recognize Images</Link>
                        <Link to = "/getName" id="GenerateNames">Generate Names</Link>
                    </div>
                </div>
                {/* Div to space out rest of content of page from the navbar */}
                <div id = "spacingDiv"></div>
            </div>
        );
    }
}

export default NavBar; 