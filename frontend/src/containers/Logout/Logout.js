import React, {Component} from 'react';
import {connect} from 'react-redux';
import {logout} from '../../store/actions/logout';


class Logout extends Component {
    componentDidMount() {
        // localStorage.removeItem('auth-token');
        // localStorage.removeItem('username');
        // localStorage.removeItem('is_admin');
        // localStorage.removeItem('is_staff');
        this.props.logout();
        this.props.history.replace('/');
    };

    render() { return <h2>Выход</h2>; }
}

const mapStateToProps = state => ({});
const mapDispatchToProps = dispatch => ({logout: () => dispatch(logout())});

export default connect(mapStateToProps, mapDispatchToProps) (Logout);
