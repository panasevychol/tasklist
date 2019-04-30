angular
  .module('tasklistApp')
  .component('taskList', {

    templateUrl: 'views/tasklist.html',

    controller: function taskListController($http, $scope, $routeParams) {
      $http.get(apiUrl + '/task-lists/' + $routeParams.taskListId)
      .then(function successCallback(response) {
        $scope.taskList = response.data;
      }.bind(this));

      this.initTaskUpdate = function(task) {
        $scope.taskToUpdate = Object.assign({}, task);
      }

      this.setTaskStatus = function(task) {
        $http.patch(
          apiUrl + '/tasks/' + task.id, {task_finished: task.task_finished}
        ).then(function successCallback(response) {
          console.log('Surprise!');
        }.bind(this));
      }
      this.deleteTask = function(task) {
        $http.delete(apiUrl + '/tasks/' + task.id).then(function successCallback(response) {
          const index = $scope.taskList.tasks.indexOf(task);
          $scope.taskList.tasks.splice(index, 1);
        }.bind(this));
      }
    }
  });
