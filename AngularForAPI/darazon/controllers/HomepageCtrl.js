angular.module('Darazon').controller('HomeController', [
  '$scope', 
  '$http', 
  '$location', 
  'RootFactory', 
  function($scope, $http, $location, RootFactory) {
    $scope.products = [];

    RootFactory.getApiRoot()
      .then(
        root => 
          $http({
            url: `${root.products}`,
            headers: {
              'Authorization': "Token " + RootFactory.getToken()
            }
          })
          .then(
            res => $scope.products = res.data.results,
            err => console.log
          )
        ,err => console.log
      );
  }
]);
