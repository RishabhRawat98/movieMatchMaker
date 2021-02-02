import React, { Component } from 'react';
import Button from 'react-bootstrap/Button';
import { MovieCard } from '../../components';
import LogOut from './logout.png';

class Swipe extends Component {

    state={
      movieID: "97889",
      movieTitle: "Aladdin",
      movieBrief: "Aladdin, a kind thief, woos Jasmine, the princess of Agrabah, with the help of Genie. When Jafar, the grand vizier, tries to usurp the king, Jasmine, Aladdin and Genie must stop him from succeeding.",
      movieImageURL: "https://lumiere-a.akamaihd.net/v1/images/ct_aladdin2019_aladdin_17975_53d203c9.jpeg",
    }

    redirect = e => {
      e.preventDefault();
      this.props.history.push("/movielist");
    };

    render() {
        return (
          <>
            <div className="top-buttons">
              <Button className="main-buttons" variant="info" onClick={this.redirect}>See all</Button>
              <input type="image" src={LogOut} className="img-logout"/>
            </div>
            <p className="form-header user-welcome">Hi {this.props.username}, welcome back!</p>
            <MovieCard movieID={this.state.movieID}
                       movieTitle={this.state.movieTitle}
                       movieBrief={this.state.movieBrief}
                       movieImageURL={this.state.movieImageURL} />
          </>
        );
    }
}

export default Swipe;