editProductModule = angular.module 'wsEditProductModule', []

editProductCtrl = ($scope, $http, $window) ->
  $scope.name = PRODUCT.name
  $scope.price = PRODUCT.price
  $scope.description = PRODUCT.description

  if PRODUCT.company?
    for company in COMPANIES
      if company._id == PRODUCT.company._id
        $scope.company = company
  else
    $scope.company = COMPANIES[0]

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

editProductCtrl.$inject = ['$scope', '$http', '$window']
editProductModule.controller 'wsEditProductCtrl', editProductCtrl