import React, { Component } from 'react';
import { LikeButton, SeenButton, WatchTrailer, DislikeButton } from '..';

class MovieCard extends Component {

    state={}

    render() {
        return (
                <div className="container">           
                    <div id={this.props.movieID} className="card h-100">
                        <img src={this.props.movieImageURL} className="card-img-top" alt="Movie Photo"/>
                        <div className="card-body">
                            <h5 className="card-title">{this.props.movieTitle}</h5>
                            <p className="card-text">{this.props.movieBrief}</p>
                            <div className="img-card-wrap">
                                <LikeButton />
                                <SeenButton />
                                <WatchTrailer />
                                <DislikeButton />
                            </div>
                        </div>
                    </div>
                </div>           
        );
    }
}

export default MovieCard;