angular.module('Darazon').controller('CartController', [
  '$scope', 
  '$http', 
  '$location', 
  'RootFactory', 
  function($scope, $http, $location, RootFactory) {
    // $scope.products = [];


    CartFactory.getCart()






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
            // res => $scope.products = res.data.results,
            err => console.log
          )
        ,err => console.log
      );
  }
]);
