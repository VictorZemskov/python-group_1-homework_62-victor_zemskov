import React from 'react';
import {Redirect, Route} from 'react-router';
import {connect} from 'react-redux';


// const AuthRoute = (props) => {
//     const {Component, path, ...other} = props;
//
//     if(localStorage.getItem('auth-token')) {
//         return <Route path={path} {...other}><Component/></Route>
//     } else {
//         return <Redirect to={{
//             pathname: "/login",
//             state: {next: path}
//         }}/>
//     }
// };


const AuthRoute = (props) => {
    if(props.auth.user_id) {
        return <Route {...props} />
    } else {
        return <Redirect to={{
            pathname: "/login",
            state: {next: props.location}
        }}/>
    }
};

const mapStateToProps = state => ({auth: state.auth});
const mapDispatchToProps = dispatch => ({});

export default connect(mapStateToProps, mapDispatchToProps) (AuthRoute);