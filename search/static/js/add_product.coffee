addModule = angular.module 'wsAddProductModule', []

addCtrl = ($scope, $http) ->
  $scope.name = ''
  $scope.description = ''
  $scope.company = COMPANIES[0]
  $scope.price = 0
  $scope.companies = COMPANIES

  $scope.send = ->
    promise = $http.post SEND_ADDRESS,
      name: $scope.name
      description: $scope.description
      company: $scope.company
      price: $scope.price

addCtrl.$inject = ['$scope', '$http']
addModule.controller 'wsAddProductCtrl', addCtrl