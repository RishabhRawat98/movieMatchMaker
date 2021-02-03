import { Component } from 'react';
import LoggedOutRoute from '.';

describe('LoggedOut', () => {
    let component;
    
    beforeEach( () => {
        component = shallow(<LoggedOutRoute isLoggedIn={true} component={Component}/>);
    });

    test('it renders', () => {
        expect(component).toExist;
    });

    test('it has a route', () => {
        expect(component.find('Route')).toHaveLength(1);
    });

    test('the redirect has the correct path', () => {
        let path = component.find('Redirect');        
        expect(path).toHaveLength(0);
    });


});