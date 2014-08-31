addModule = angular.module 'wsAddProductModule', []

addCtrl = ($scope, $http, $window) ->
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

    promise.success (data) ->
      if data == 'OK'
        $window.location.href = REDIRECT_ADDRESS

addCtrl.$inject = ['$scope', '$http', '$window']
addModule.controller 'wsAddProductCtrl', addCtrl