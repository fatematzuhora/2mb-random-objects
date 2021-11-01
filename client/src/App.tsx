import React from 'react';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import { ReportPage } from 'pages';

const App: React.FC = (props: any) => {
	return (
		<BrowserRouter>
			<Switch>
				<Route path="/report" exact={true} render={() => <ReportPage />} />

				<Redirect from="/" to="/report" />
			</Switch>
		</BrowserRouter>
	);
};

export default App;
