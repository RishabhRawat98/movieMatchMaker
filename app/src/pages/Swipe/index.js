import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';
import { MovieCard } from '../../components';
import LogOut from './logout2.png';

class Swipe extends Component {

    state={
      movieID: "",
      movieTitle: "",
      movieBrief: "",
      movieImageURL: "",
    }

    redirect = e => {
      e.preventDefault();
      this.props.history.push("/movielist");
    };

    render() {
        return (
          <>
            <Button className="main-buttons" variant="info" onClick={this.redirect}>See all</Button>
            <input type="image" src={LogOut} className="img-card"/>
            <p className="form-header">Hi {this.props.username}</p>
            <MovieCard movieID={this.state.movieID}
                       movieTitle={this.state.movieTitle}
                       movieBrief={this.state.movieBrief}
                       movieImageURL={this.state.movieImageURL} />
          </>
        );
    }
}

export default Swipe;