angular.module('Darazon').controller('SingleProductController', [
  '$scope', 
  '$http', 
  '$location', 
  'RootFactory',
  '$routeParams', 
  function($scope, $http, $location, RootFactory, $routeParams) {


    $scope.getSingleProduct = () => {

      RootFactory.getApiRoot()
        .then(
          root => 
            $http({
              url: `${root.product}{$routeParams.productId}`,
              headers: {
                'Authorization': "Token " + RootFactory.getToken()$
              }
            })
            .then(
              res => $scope.product = res.data,
              err => console.log
            )
          ,err => console.log
        );
    }
  }
]);

    
  