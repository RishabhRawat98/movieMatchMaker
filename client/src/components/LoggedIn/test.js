import { Component } from 'react';
import PrivateRoute from '.';

describe('LoggedIn', () => {
    let component;
    
    beforeEach( () => {
        component = shallow(<PrivateRoute isLoggedIn={true} component={Component}/>);
    });

    test('it renders', () => {
        expect(component).toExist;
    });

    // test('the redirect has the correct path', () => {
    //     const path = component.find('Redirect');
    //     expect(path.prop('to')).toEqual('/login');
    // });
});