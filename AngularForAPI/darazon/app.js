// Create main Angular module
var app = angular.module('Darazon', ['ngRoute'])
            .constant('apiUrl', "http://localhost:8000");

angular.module('Darazon').config(
[
  '$interpolateProvider',
  '$routeProvider',
  function($interpolateProvider, $routeProvider) {

    $interpolateProvider.startSymbol('((');
    $interpolateProvider.endSymbol('))');

    $routeProvider
      .when('/home', {
        controller: 'HomeController',
        templateUrl: 'darazon/partials/homepage.html'
      })
      .when('/login', {
        controller: 'AuthController',
        templateUrl: 'darazon/partials/login.html'
      })
      .when('/register', {
        controller: 'RegisterController',
        templateUrl: 'darazon/partials/register.html'
      })
      .when('/products', {
        controller: 'ProductsController',
        templateUrl: 'darazon/partials/products.html'
      })
      .when('/types', {
        controller: 'ProductTypesController',
        templateUrl: 'darazon/partials/producttypes.html'
      })
      .when('/selectedproduct', {
        controller: 'SingleProductController',
        templateUrl: 'darazon/partials/singleproduct.html'
      })
      .when('/cart', {
        controller: 'CartController',
        templateUrl: 'darazon/partials/cart.html'
      });
  }
]);