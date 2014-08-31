editProductModule = angular.module 'wsEditProductModule', []

editProductCtrl = ($scope) ->
  $scope.name = PRODUCT.name
  $scope.price = PRODUCT.price
  $scope.description = PRODUCT.description

  if PRODUCT.company?
    $scope.company = PRODUCT.company
  else
    $scope.company = COMPANIES[0]

  $scope.companies = COMPANIES

editProductCtrl.$inject = ['$scope']
editProductModule.controller 'wsEditProductCtrl', editProductCtrl