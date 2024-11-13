import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import FeedList from './FeedList'; // Your feed component
import OtherComponent from './OtherComponent'; // Any other component

function App() {
    return (
        <Router>
            <div className="App">
                <h1>Your Feed Aggregator</h1>
                <Switch>
                    <Route path="/" exact component={FeedList} />
                    <Route path="/other" component={OtherComponent} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;
