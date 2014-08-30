addModule = angular.module 'wsAddProductModule', []

addCtrl = ($scope) ->
  $scope.name = ''
  $scope.description = ''
  $scope.company = COMPANIES[0]
  $scope.price = 0
  $scope.companies = COMPANIES

addCtrl.$inject = ['$scope']
addModule.controller 'wsAddProductCtrl', addCtrl