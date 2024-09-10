# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

# we are also using ->
https://react-bootstrap.github.io/

https://react-bootstrap-v4.netlify.app/

# fonts
https://cdnjs.com/

# for templates -> lux theme
https://bootswatch.com/

http://localhost:3000/

# intresting react

in order to use some propr you need to import
`useParams`unlike older versions

`<Product product={product}` -->'' this is in the HomeScreen
and this could be used in the Product component
`{props.product}` this is one way to call the props from the wherever it's being refered to 

this is Route, it takes a path and a component for the hyperlinks
`<Route path='/' Component={HomeScreen}/>` 

# react extension I'm using to speed ti
https://marketplace.visualstudio.com/items?itemName=rodrigovallades.es7-react-js-snippets

- `imd` or `imp`
- `rfce`


# improvements to be done

- INSTALL THE NPM PACKAGE FOR FONTAWESOME
  npm install @fortawesome/fontawesome-free

- Import Font Awesome in your index.js or App.js (have to try both):
  import '@fortawesome/fontawesome-free/css/all.min.css';



- fix the `Rating` component to have just one span if posible with iterating stars
  it makes no sense to copy paste the code, when I can have a dictionary with the name of each 
  className writen properly

- Again, for the `Rating` component, create a constants.js if not already created and put the classNames 
  for the star there
