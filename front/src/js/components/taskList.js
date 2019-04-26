const apiUrl = 'http://localhost:5000';

angular
  .module('tasklistApp')
  .component('taskList', {
    template:
      '<ul>' +
        '<li ng-repeat="task in $ctrl.tasks">{{task.name}}</li>' +
      '</ul>',

    controller: function taskListController($http) {
      $http.get(apiUrl + '/task-lists/1').then(function successCallback(response) {
        this.tasks = response.data.tasks;
      }.bind(this));

    }
  });
