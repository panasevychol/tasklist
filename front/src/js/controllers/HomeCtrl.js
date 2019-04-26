angular.module('tasklistApp')
.controller('HomeCtrl', [
  '$scope',
  function($scope) {
    $scope.message = 'Works!';
  }
]);
