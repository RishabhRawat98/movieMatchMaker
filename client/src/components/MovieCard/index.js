import React, { Component } from 'react';
import { LikeButton, DislikeButton } from '..';

class MovieCard extends Component {

    state={}

    render() {
        return (
                <div className="container movie-card">           
                    <div id={this.props.movieID} className="card">
                        <img src={this.props.movieImageURL} className="card-img-top" alt="Movie Photo"/>
                        <div className="card-body">
                            <h5 className="card-title">{this.props.movieTitle}</h5>
                            <p className="card-text">{this.props.movieBrief}</p>
                            <div className="card-buttons">
                                <LikeButton />                                
                                <DislikeButton />
                            </div>
                        </div>
                    </div>
                </div>           
        );
    }
}

export default MovieCard;