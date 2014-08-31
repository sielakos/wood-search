showProductsModule = angular.module 'wsShowProductsModule', []

showProductsCtrl = ($scope) ->
  $scope.products = PRODUCTS


showProductsCtrl.$inject = ['$scope']
showProductsModule.controller 'wsShowProductsCtrl', showProductsCtrl